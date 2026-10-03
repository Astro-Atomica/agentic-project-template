# Agent Instructions

This repository is an agentic project scaffold. It is designed to be copied into new projects and adapted.

## First Steps

1. Read this file.
2. Read [README.md](README.md).
3. Read [agents/README.md](agents/README.md).
4. Check for project-specific guidance in [workspace/AGENTS.md](workspace/AGENTS.md).
5. Inspect the current project profile under [templates/profiles](templates/profiles), if one has been selected.
6. Read and customize [agents/privacy-policy.json](agents/privacy-policy.json) before the first project commit.

For the chosen client, consult the dated [agent compatibility notes](agents/rules/agent-compatibility.md). Native entrypoint discovery varies by client, version, and session settings; verify that the linked shared guidance was actually read.

## Core Rules

- `AGENTS.md` is the canonical entrypoint for all coding agents: Codex, Claude, Cursor, Windsurf, and future tools.
- Do not duplicate shared instructions into platform-specific files such as `CLAUDE.md`, `.cursorrules`, or `.windsurfrules`.
- If a platform-specific compatibility file is unavoidable, keep it minimal and make it point back to `AGENTS.md`.
- Keep human-authored agent guidance visible in `agents/`, not hidden in dotfolders unless a tool requires that path.
- Do not commit secrets, tokens, private account data, machine-specific paths, dependency folders, or generated build output.
- Prefer editing existing docs over creating new top-level folders.
- Keep the repo root small and predictable.
- If a tool creates local clutter, add it to `.gitignore` rather than committing it.
- Run the privacy preflight on staged content before committing and on unpublished commits before pushing.
- For networked features, untrusted input, public assets, deployment changes, or security reviews, follow [security watchouts](agents/rules/security-watchouts.md). Convert applicable risks into repeatable tests and record unresolved findings; a passing secret scan is not an application security audit.
- Treat browser captures, local-app state, cookies, storage state, traces, screenshots, videos, and exports as private trust-boundary material unless intentionally reviewed and approved for publication.
- Use project profiles as additive starting points, not mandatory structure.
- No legacy code and no legacy fallbacks unless legacy support has been explicitly opted into. On project startup, ask for the supported version floor or time window before adding compatibility paths.

## Folder Roles

#### Managed Folders 
> tracked by Git and form the public scaffold

- `agents/` - shared rules, workflows, skills, personas, and reusable agent context.
- `docs/` - durable human documentation, decisions, architecture notes, and release notes.
- `packages/` - optional monorepo packages or distributable units.
- `templates/` - reusable scaffold/profile material.
- `workspace/` - default active project surface.

#### Private Local Folders
>  ignored by Git

- `_private/` - local private state; ignored.
  - Use as temp storage for stuff that should not be committed to a repository, like local paths, temp secrets, etc.
  - Use `_private/feature-requests.md` to preserve feature requests, product decisions, and user intent across context compaction and new threads.
- `_code_review/` - local private code review notes and artifacts; ignored.
- `_logs/` - local logs from tools, scripts, agents, and debugging; ignored.
- `_exports/` - local exported files, reports, snapshots, and handoff artifacts; ignored.
- `_tool_results/` - local raw tool outputs, command captures, and intermediate agent results; ignored.
- `_build/` - generated build/release artifacts; ignored.
- `_cache/` - downloaded/generated caches, datasets, model caches, and embeddings; ignored.

## Working Style

- Preserve requested features. When a feature request or product requirement may outlive the current context, record it in `_private/feature-requests.md` unless it belongs in tracked docs.
- Keep explanations concise and grounded in files changed.
- When adding project-specific rules, place durable shared guidance under `agents/` and local implementation notes under `workspace/`.
- When a user makes a design language request, update and maintain `agents/DESIGN.md` and supporting design-system docs under `agents/design/`; do not leave durable design intent only in chat or component code.
- For code reviews, use `_code_review/` for scratch notes and follow [agents/workflows/code-review.md](agents/workflows/code-review.md).
- Track technical debt discovered while working on code in `_code_review/`, even outside formal code reviews. Document issues that should be tracked but not tackled in the current task.
- Put logs in `_logs/`, ad hoc exports in `_exports/`, and raw tool outputs in `_tool_results/`.
- Agent-started tools, MCPs, preview servers, test web services, and temporary local services use the agent port range by default. Start them at `localhost:8100` or higher.
- Before starting an agent service, check whether the intended port is already in use and choose the next available port in the agent range.
- Track every agent-started long-running process in an ignored underscore folder, such as `_logs/processes.md` or `_tool_results/processes.md`, so it can be cleanly exited or force closed across context compaction and new threads.
- Agents cannot reliably converge on a solution without a way to observe the result. Raise a warning when there are not enough tools to close the loop and observe or test the result.
- Do not treat visual or interactive work as complete without an appropriate observation path. For example: do not write HTML without being able to view it in a browser and capture a screenshot, do not draw an image without visual verification, and do not write JavaScript without validating it in a test or in the app.

## Public Template Bias

This repo should stay useful as a public template. Avoid adding personal workflow assumptions unless they are clearly marked as optional.
