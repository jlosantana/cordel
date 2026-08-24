#!/usr/bin/env python3
"""Instala o Cordel e inicializa ou verifica projetos consumidores."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


CONFIG_DIR = ".cordel"
CONFIG_FILE = "project.json"
SOURCE_KEYS = (
    "requirements",
    "asis",
    "decisions",
    "needs",
    "stories",
    "specs",
    "analyses",
    "evidence",
)
AGENT_FILES = {
    "codex": ("AGENTS.md", "agents.md"),
    "claude": ("CLAUDE.md", "claude.md"),
}
MANAGED_BLOCK_START = "<!-- cordel:start -->"
MANAGED_BLOCK_END = "<!-- cordel:end -->"


def default_config(project_name: str) -> Dict[str, Any]:
    return {
        "schema_version": 3,
        "cordel_version": "0.3.0",
        "project": {
            "name": project_name,
            "language": "",
            "repositories": [],
        },
        "sources": {
            "requirements": source(".cordel/product/requirements", "product-owner"),
            "asis": source(".cordel/product/context", "service-team"),
            "decisions": source(".cordel/product/decisions", "service-team"),
            "needs": source(".cordel/work/needs", "product-owner"),
            "stories": source(".cordel/work/stories", "service-team"),
            "specs": source(".cordel/work/specs", "service-team"),
            "analyses": source(".cordel/work/analyses", "service-team"),
            "evidence": source(".cordel/evidence", "service-team"),
        },
        "storage": {
            "archive": ".cordel/archive",
            "generated": ".cordel/generated",
            "local": ".cordel/local",
        },
        "identifiers": {
            "requirements": ["REQ-", "NFR-"],
            "needs": "NEED-",
            "stories": "STORY-",
            "specs": "SPEC-",
            "decisions": "ADR-",
            "analyses": "ANALYSIS-",
        },
        "commands": {"reconcile": "", "build": "", "test": ""},
        "policies": {
            "new_scope_requires_owner_decision": True,
            "ready_requires_gate": True,
            "technical_claims_require_evidence": True,
            "evidence_format": "path:line",
        },
    }


def source(location: str, owner: str) -> Dict[str, str]:
    return {"kind": "path", "location": location, "owner": owner}


def write_json(path: Path, value: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def ensure_inside(root: Path, candidate: Path) -> Path:
    resolved_root = root.resolve()
    resolved = candidate.resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(
            f"caminho fora da raiz Cordel corrente: {candidate}; "
            "referências a diretórios ancestrais não são permitidas"
        ) from exc
    return resolved


def update_managed_block(path: Path, block: str) -> str:
    block = block.strip() + "\n"
    if MANAGED_BLOCK_START not in block or MANAGED_BLOCK_END not in block:
        raise ValueError(f"bloco Cordel inválido: {path.name}")

    if not path.exists():
        path.write_text(block, encoding="utf-8")
        return "created"

    current = path.read_text(encoding="utf-8")
    start_count = current.count(MANAGED_BLOCK_START)
    end_count = current.count(MANAGED_BLOCK_END)
    if start_count == 0 and end_count == 0:
        separator = "" if not current.strip() else "\n\n"
        path.write_text(current.rstrip() + separator + block, encoding="utf-8")
        return "updated"
    if start_count != 1 or end_count != 1:
        raise ValueError(
            f"marcadores Cordel inconsistentes em {path}; corrija-os antes de executar init"
        )

    start = current.index(MANAGED_BLOCK_START)
    end_marker = current.find(MANAGED_BLOCK_END)
    if end_marker < start:
        raise ValueError(
            f"marcadores Cordel fora de ordem em {path}; corrija-os antes de executar init"
        )
    end = end_marker + len(MANAGED_BLOCK_END)
    replacement = block.rstrip()
    updated = current[:start] + replacement + current[end:]
    if updated == current:
        return "unchanged"
    path.write_text(updated, encoding="utf-8")
    return "updated"


def init_project(root: Path, agents: Sequence[str] = ("codex", "claude")) -> int:
    invalid_agents = [agent for agent in agents if agent not in AGENT_FILES]
    if invalid_agents:
        raise ValueError(
            "agente(s) não suportado(s): " + ", ".join(invalid_agents)
        )

    root = root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    config_dir = root / CONFIG_DIR
    config_dir.mkdir(exist_ok=True)
    config_path = config_dir / CONFIG_FILE
    created: List[Path] = []
    updated: List[Path] = []

    if not config_path.exists():
        write_json(config_path, default_config(root.name))
        created.append(config_path)

    config = load_config(config_path)
    sources = config.get("sources", {})
    for key in SOURCE_KEYS:
        value = sources.get(key, {})
        if not isinstance(value, dict) or value.get("kind") != "path":
            continue
        location = value.get("location")
        if not isinstance(location, str) or not location.strip():
            continue
        target = ensure_inside(root, root / location)
        if not target.exists():
            target.mkdir(parents=True)
            created.append(target)

    storage = config.get("storage", {})
    if isinstance(storage, dict):
        for value in storage.values():
            if not isinstance(value, str) or not value.strip():
                continue
            target = ensure_inside(root, root / value)
            if not target.exists():
                target.mkdir(parents=True)
                created.append(target)

    index_path = config_dir / "index.md"
    if not index_path.exists():
        index_path.write_text(index_content(root.name), encoding="utf-8")
        created.append(index_path)

    ignore_path = config_dir / ".gitignore"
    if not ignore_path.exists():
        ignore_path.write_text("generated/\nlocal/\n", encoding="utf-8")
        created.append(ignore_path)

    template_source = Path(__file__).resolve().parents[1] / "assets" / "templates"
    template_target = config_dir / "templates"
    template_target.mkdir(exist_ok=True)
    for source in sorted(template_source.glob("*.md")):
        target = template_target / source.name
        if not target.exists():
            shutil.copy2(source, target)
            created.append(target)

    instruction_source = Path(__file__).resolve().parents[1] / "assets" / "instructions"
    for agent in agents:
        target_name, source_name = AGENT_FILES[agent]
        target = root / target_name
        block = (instruction_source / source_name).read_text(encoding="utf-8")
        result = update_managed_block(target, block)
        if result == "created":
            created.append(target)
        elif result == "updated":
            updated.append(target)

    if created:
        print("Criados:")
        for path in created:
            print(f"  - {path.relative_to(root)}")
    if updated:
        print("Atualizados:")
        for path in updated:
            print(f"  - {path.relative_to(root)}")
    if not created and not updated:
        print("Nenhum arquivo alterado; a estrutura já existia.")
    print(f"Configuração: {config_path}")
    return 0


def install_skill(destination: Optional[Path] = None) -> int:
    source_dir = Path(__file__).resolve().parents[1]
    skills_dir = destination
    if skills_dir is None:
        codex_home = os.environ.get("CODEX_HOME")
        skills_dir = (
            Path(codex_home) / "skills"
            if codex_home
            else Path.home() / ".codex" / "skills"
        )

    skills_dir = skills_dir.expanduser().resolve()
    target_dir = skills_dir / source_dir.name
    if target_dir == source_dir:
        print(f"Nenhum arquivo alterado; a skill já está instalada em {target_dir}")
        return 0
    try:
        target_dir.relative_to(source_dir)
    except ValueError:
        pass
    else:
        raise ValueError(
            f"destino não pode ficar dentro da origem da skill: {target_dir}"
        )
    if target_dir.exists():
        raise ValueError(
            f"destino já existe: {target_dir}. Remova ou renomeie a instalação "
            "existente antes de atualizar."
        )

    skills_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, target_dir)
    print(f"Skill instalada em: {target_dir}")
    return 0


def load_config(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"configuração não encontrada: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON inválido em {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("a raiz da configuração deve ser um objeto JSON")
    return value


def index_content(project_name: str) -> str:
    return f"""# Contexto de {project_name}

Este índice aponta para conhecimento ativo e canônico. Não replique o conteúdo dos
artefatos aqui; mantenha links, responsáveis e uma descrição curta.

## Contexto canônico

- Requisitos:
- AS-IS:
- Decisões vigentes:

## Trabalho ativo

- Necessidades:
- Stories e specs:
- Análises:

## Fontes externas

- Sistema, responsável e endereço:
"""


def require_object(config: Dict[str, Any], key: str, errors: List[str]) -> Dict[str, Any]:
    value = config.get(key)
    if not isinstance(value, dict):
        errors.append(f"campo obrigatório '{key}' deve ser um objeto")
        return {}
    return value


def check_project(root: Path) -> int:
    root = root.resolve()
    config_path = root / CONFIG_DIR / CONFIG_FILE
    errors: List[str] = []
    warnings: List[str] = []
    try:
        config = load_config(config_path)
    except ValueError as exc:
        print(f"ERRO: {exc}")
        return 1

    if config.get("schema_version") != 3:
        errors.append("schema_version deve ser 3")
    if not isinstance(config.get("cordel_version"), str) or not config.get(
        "cordel_version", ""
    ).strip():
        errors.append("cordel_version deve ser preenchido")

    project = require_object(config, "project", errors)
    if not isinstance(project.get("name"), str) or not project.get("name", "").strip():
        errors.append("project.name deve ser preenchido")
    repositories = project.get("repositories")
    if not isinstance(repositories, list):
        errors.append("project.repositories deve ser uma lista")
    elif not repositories:
        warnings.append("project.repositories está vazio")
    else:
        for index, repository in enumerate(repositories):
            if not isinstance(repository, str) or not repository.strip():
                errors.append(
                    f"project.repositories[{index}] deve ser um caminho relativo não vazio"
                )
                continue
            repository_path = Path(repository)
            if repository_path.is_absolute():
                errors.append(
                    f"project.repositories[{index}] deve ser relativo à raiz do projeto"
                )
                continue
            try:
                resolved = ensure_inside(root, root / repository_path)
            except ValueError as exc:
                errors.append(f"project.repositories[{index}]: {exc}")
                continue
            if not resolved.is_dir():
                errors.append(f"repositório não existe: {repository}")

    sources = require_object(config, "sources", errors)
    for key in SOURCE_KEYS:
        value = sources.get(key)
        if not isinstance(value, dict):
            errors.append(f"sources.{key} deve ser um objeto")
            continue
        kind = value.get("kind")
        location = value.get("location")
        owner = value.get("owner")
        if kind not in ("path", "url"):
            errors.append(f"sources.{key}.kind deve ser 'path' ou 'url'")
            continue
        if not isinstance(location, str) or not location.strip():
            errors.append(f"sources.{key}.location deve ser preenchido")
            continue
        if not isinstance(owner, str) or not owner.strip():
            errors.append(f"sources.{key}.owner deve ser preenchido")
        if kind == "url":
            if not location.startswith(("https://", "http://")):
                errors.append(f"sources.{key}.location deve ser uma URL HTTP(S)")
            continue
        source_path = Path(location)
        if source_path.is_absolute():
            errors.append(f"sources.{key}.location deve ser relativo à raiz do projeto")
            continue
        try:
            resolved = ensure_inside(root, root / source_path)
        except ValueError as exc:
            errors.append(f"sources.{key}: {exc}")
            continue
        if not resolved.is_dir():
            errors.append(f"sources.{key} não existe: {location}")

    storage = require_object(config, "storage", errors)
    for key in ("archive", "generated", "local"):
        value = storage.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"storage.{key} deve ser um caminho relativo não vazio")
            continue
        path = Path(value)
        if path.is_absolute():
            errors.append(f"storage.{key} deve ser relativo à raiz do projeto")
            continue
        try:
            resolved = ensure_inside(root, root / path)
        except ValueError as exc:
            errors.append(f"storage.{key}: {exc}")
            continue
        if not resolved.is_dir():
            errors.append(f"storage.{key} não existe: {value}")

    identifiers = require_object(config, "identifiers", errors)
    for key in ("requirements", "needs", "stories", "specs", "decisions", "analyses"):
        value = identifiers.get(key)
        if isinstance(value, str):
            valid = bool(value.strip())
        elif isinstance(value, list):
            valid = bool(value) and all(isinstance(item, str) and item for item in value)
        else:
            valid = False
        if not valid:
            errors.append(f"identifiers.{key} deve conter prefixo(s) não vazio(s)")

    commands = require_object(config, "commands", errors)
    for key in ("reconcile", "build", "test"):
        value = commands.get(key)
        if not isinstance(value, str):
            errors.append(f"commands.{key} deve ser texto")
        elif not value.strip():
            warnings.append(f"commands.{key} ainda não foi configurado")

    policies = require_object(config, "policies", errors)
    for key in (
        "new_scope_requires_owner_decision",
        "ready_requires_gate",
        "technical_claims_require_evidence",
    ):
        if not isinstance(policies.get(key), bool):
            errors.append(f"policies.{key} deve ser booleano")
    if not isinstance(policies.get("evidence_format"), str) or not policies.get(
        "evidence_format", ""
    ).strip():
        errors.append("policies.evidence_format deve ser preenchido")

    for warning in warnings:
        print(f"AVISO: {warning}")
    for error in errors:
        print(f"ERRO: {error}")
    if errors:
        print(f"NO-GO: {len(errors)} erro(s), {len(warnings)} aviso(s)")
        return 1
    print(f"GO: configuração válida, {len(warnings)} aviso(s)")
    return 0


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Instala o Cordel e inicializa ou verifica projetos consumidores."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    install = subparsers.add_parser(
        "install", help="instala a skill no diretório de skills do Codex"
    )
    install.add_argument(
        "destination",
        nargs="?",
        type=Path,
        help="diretório de skills (padrão: CODEX_HOME/skills ou ~/.codex/skills)",
    )
    init = subparsers.add_parser("init")
    init.add_argument("project", type=Path, help="raiz do projeto")
    agents = init.add_mutually_exclusive_group()
    agents.add_argument(
        "--codex", dest="agents", action="store_const", const=("codex",),
        help="integra somente AGENTS.md",
    )
    agents.add_argument(
        "--claude", dest="agents", action="store_const", const=("claude",),
        help="integra somente CLAUDE.md",
    )
    agents.add_argument(
        "--all", dest="agents", action="store_const", const=("codex", "claude"),
        help="integra AGENTS.md e CLAUDE.md (padrão)",
    )
    agents.add_argument(
        "--no-agent-files", dest="agents", action="store_const", const=(),
        help="não cria nem atualiza arquivos de orientação de agentes",
    )
    init.set_defaults(agents=("codex", "claude"))

    check = subparsers.add_parser("check")
    check.add_argument("project", type=Path, help="raiz do projeto")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    try:
        if args.command == "install":
            return install_skill(args.destination)
        if args.command == "init":
            return init_project(args.project, args.agents)
        return check_project(args.project)
    except ValueError as exc:
        print(f"ERRO: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
