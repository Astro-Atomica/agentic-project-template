# Repo Conventions

## Visible By Default

Human-authored guidance belongs in visible folders. Use `agents/`, `docs/`, `templates/`, `packages/`, and `workspace/`.

Do not create hidden human-facing namespaces such as `.agents/`, `.rules/`, or `.prompts/` unless a tool requires that exact path.

## One Agent Document Stack

All coding agents should start at root `AGENTS.md` and follow the shared document stack from there.

Do not maintain parallel instruction files for individual tools. Platform-specific files such as `CLAUDE.md`, `.cursorrules`, or `.windsurfrules` should not duplicate the shared contract. If a tool requires one, keep it as a compatibility shim that points to `AGENTS.md`.

## Root Hygiene

The root should contain entrypoints and repo-level infrastructure:

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `.editorconfig`
- `.github/`
- `agents/`
- `docs/`
- `packages/`
- `templates/`
- `workspace/`

Avoid adding new top-level folders unless they represent a durable repo-level concept.

## Managed Folders

Managed folders are tracked by Git and form the public project surface:

- `.github/` - GitHub automation and templates.
- `agents/` - visible agent harness guidance.
- `docs/` - durable human documentation.
- `packages/` - optional package/workspace units.
- `templates/` - reusable profile and scaffold material.
- `workspace/` - default active project surface.

## Private Local Folders

Private local folders are ignored by Git and should not appear on GitHub:

- `_private/` is for local private state and is ignored.
- `_code_review/` is for local review scratch notes and is ignored.
- `_logs/` is for local logs and is ignored.
- `_exports/` is for local exported files, reports, snapshots, and handoff artifacts and is ignored.
- `_tool_results/` is for raw tool outputs and intermediate agent results and is ignored.
- `_build/` is for generated local output and is ignored.
- `_cache/` is for downloaded/generated caches, datasets, model caches, and embeddings and is ignored.
- Dependency folders and generated artifacts are not architecture.

## Tool Dotfolders

Tool dotfolders may exist locally, but they should be ignored unless the project intentionally commits a small shared config file.

Examples:
- `.github/` is committed because GitHub requires it.
- `.vscode/`, `.obsidian/`, `.claude/`, `.cursor/`, and `.idea/` are ignored by default.
