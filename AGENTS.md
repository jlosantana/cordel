# Repository Guidelines

## Project Structure & Module Organization

This repository packages Cordel, a software-engineering method oriented around context, specifications, and evidence. `method/` contains the portable documentation and JSON schema. `skill/cordel/` is the installable Codex skill: keep its entry point in `SKILL.md`, workflow details in `references/`, reusable Markdown in `assets/templates/`, and tooling in `scripts/`. `example/project.json` demonstrates consumer configuration, while `source/` records the project experiences behind the method and its generalization decisions. Keep project-specific rules out of the portable core.

## Build, Test, and Development Commands

The project has no compilation step or third-party runtime dependencies; use Python 3.8+.

```bash
python skill/cordel/scripts/cordel.py --help
python skill/cordel/scripts/cordel.py init /path/to/project
python skill/cordel/scripts/cordel.py check /path/to/project
python -m py_compile skill/cordel/scripts/cordel.py
```

`init` creates a consumer's `.cordel/` structure without overwriting existing files. `check` validates its configuration and required directories. Run `py_compile` as a quick syntax check after Python changes.

## Coding Style & Naming Conventions

Use four-space indentation, type hints, `pathlib.Path`, and standard-library modules in Python. Follow `snake_case` for functions and variables and `UPPER_SNAKE_CASE` for constants. Markdown should use concise headings, short paragraphs, relative links, and Portuguese terminology consistent with the existing method. Keep JSON at two-space indentation with a trailing newline. Preserve identifier patterns such as `NEED-`, `STORY-`, `SPEC-`, and `ADR-`.

## Testing Guidelines

There is currently no automated test suite or coverage threshold. For script changes, run `py_compile`, then exercise `init` and `check` against a temporary directory; verify that a second `init` is idempotent. For documentation or template changes, check links, examples, and consistency with `method/project.schema.json` and `example/project.json`.

## Commit & Pull Request Guidelines

Git history is not included in this workspace, so use short, imperative commit subjects (for example, `Add validation for source paths`) and keep each commit focused. Pull requests should explain the motivation, list affected method or skill files, include validation commands and results, and call out schema or generated-structure changes. Link the relevant issue or decision record when available.

## Agent-Specific Instructions

Before editing, read `README.md` and the nearest relevant workflow under `skill/cordel/references/`. Do not invent external identifiers, treat claims as implementation evidence, or edit generated projections instead of their source.
