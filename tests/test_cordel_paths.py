from __future__ import annotations

import importlib.util
import io
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPOSITORY_ROOT / "skill" / "cordel" / "scripts" / "cordel.py"
SPEC = importlib.util.spec_from_file_location("cordel", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"não foi possível carregar o módulo Cordel em {SCRIPT_PATH}")
cordel = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cordel)


class CordelPathConfinementTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def initialize(self, root: Path) -> dict:
        with redirect_stdout(io.StringIO()):
            self.assertEqual(cordel.init_project(root, agents=()), 0)
        config_path = root / ".cordel" / "project.json"
        config = cordel.load_config(config_path)
        config["project"]["repositories"] = ["."]
        cordel.write_json(config_path, config)
        return config

    def check(self, root: Path) -> tuple[int, str]:
        output = io.StringIO()
        with redirect_stdout(output):
            result = cordel.check_project(root)
        return result, output.getvalue()

    def test_nested_project_remains_valid_when_cloned_in_isolation(self) -> None:
        aggregator = self.workspace / "aggregator"
        internal = aggregator / "services" / "orders"
        self.initialize(internal)

        result, output = self.check(internal)
        self.assertEqual(result, 0, output)

        isolated = self.workspace / "orders-clone"
        shutil.copytree(internal, isolated)
        result, output = self.check(isolated)
        self.assertEqual(result, 0, output)

    def test_second_init_is_idempotent(self) -> None:
        internal = self.workspace / "orders"
        self.initialize(internal)

        output = io.StringIO()
        with redirect_stdout(output):
            result = cordel.init_project(internal, agents=())

        self.assertEqual(result, 0)
        self.assertIn("Nenhum arquivo alterado", output.getvalue())

    def test_init_rejects_unknown_agent_before_creating_project(self) -> None:
        internal = self.workspace / "orders"

        with self.assertRaisesRegex(ValueError, "agente.*não suportado"):
            cordel.init_project(internal, agents=("unknown",))

        self.assertFalse(internal.exists())

    def test_internal_source_cannot_reference_aggregator(self) -> None:
        aggregator = self.workspace / "aggregator"
        shared_requirements = aggregator / "requirements"
        shared_requirements.mkdir(parents=True)
        internal = aggregator / "services" / "orders"
        config = self.initialize(internal)
        config["sources"]["requirements"]["location"] = "../../../requirements"
        cordel.write_json(internal / ".cordel" / "project.json", config)

        result, output = self.check(internal)

        self.assertEqual(result, 1)
        self.assertIn("fora da raiz Cordel corrente", output)
        self.assertIn("diretórios ancestrais não são permitidas", output)

    def test_absolute_repository_path_is_rejected(self) -> None:
        internal = self.workspace / "orders"
        config = self.initialize(internal)
        external = self.workspace / "external"
        external.mkdir()
        config["project"]["repositories"] = [str(external.resolve())]
        cordel.write_json(internal / ".cordel" / "project.json", config)

        result, output = self.check(internal)

        self.assertEqual(result, 1)
        self.assertIn("deve ser relativo à raiz do projeto", output)

    def test_symbolic_link_resolving_outside_root_is_rejected(self) -> None:
        internal = self.workspace / "orders"
        config = self.initialize(internal)
        external = self.workspace / "external-requirements"
        external.mkdir()
        linked_source = internal / "linked-requirements"
        try:
            linked_source.symlink_to(external, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"criação de link simbólico indisponível: {exc}")
        config["sources"]["requirements"]["location"] = "linked-requirements"
        cordel.write_json(internal / ".cordel" / "project.json", config)

        result, output = self.check(internal)

        self.assertEqual(result, 1)
        self.assertIn("fora da raiz Cordel corrente", output)

    def test_install_rejects_destination_inside_skill_source(self) -> None:
        destination = SCRIPT_PATH.parents[1] / "nested-skills"

        with self.assertRaisesRegex(ValueError, "dentro da origem da skill"):
            cordel.install_skill(destination)

        self.assertFalse((destination / "cordel").exists())


if __name__ == "__main__":
    unittest.main()
