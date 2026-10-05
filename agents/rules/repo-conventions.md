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

## Document Directory Hygiene

These guidelines apply to human-facing document directories, not source-code organization.

- About 20 human-facing files in one directory is the high side.
- When 3+ files share a clear theme, consider a subdirectory.
- When only 2 files share a prefix, keep them together and use the prefix; do not create a directory just for two files.
- If a Markdown file grows past 500 lines, split it at `##` sections into topic files and leave a `README.md` or index behind.
- Prefer concise path names because path length limits still matter.
- No strict limits; use judgment.

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

## Build And Documentation Release Versioning

By default, version builds and documentation releases by date and build number. Use `YYYY-MM-DD · Build N` for visible labels and `YYYY-MM-DD-build-N` for filenames, tags, and release identifiers; for example, `2026-10-05 · Build 1` and `2026-10-05-build-1`.

- Use the build or documentation release date, with a consistent project timezone (UTC unless the project specifies another).
- Start each independently released project or document at Build 1 and increment its build number for each subsequent release. Do not reset the counter when the date changes or reuse a released identifier.
- Documentation shipped with a software build uses that build's date and number. Independently released documentation maintains its own counter.
- Keep the identifier consistent across visible version labels, release notes, and artifact metadata. Record the source commit and validation status in release notes when applicable.
- Ordinary working edits do not require a new release number. Assign the identifier when preparing a build or documentation release, and distinguish a prepared candidate from a published release.

Record any explicitly selected alternative in project guidance. If a package manager or platform requires a different version format, retain the date and build number in release metadata and document the mapping.

## Tool Dotfolders

Tool dotfolders may exist locally, but they should be ignored unless the project intentionally commits a small shared config file.

Examples:
- `.github/` is committed because GitHub requires it.
- `.vscode/`, `.obsidian/`, `.claude/`, `.cursor/`, and `.idea/` are ignored by default.
