# 0002 - Use One Agent Document Stack

**Status:** Accepted

## Context

Agentic development tools often encourage their own instruction files, such as `CLAUDE.md` or other platform-specific rule documents.

Those files create drift. A project can end up with different rules for Codex, Claude, and other tools even though they are all working on the same repository.

## Decision

`AGENTS.md` is the canonical entrypoint for all coding agents.

The shared document map is:

1. root `AGENTS.md`
2. `agents/README.md`
3. `agents/PRINCIPLES.md`
4. relevant files under `agents/rules/`, `agents/workflows/`, `agents/skills/`, `agents/personas/`, and `agents/tools/`
5. scoped `AGENTS.md` files in subdirectories when needed, such as `workspace/AGENTS.md`

This map is not a mandatory reading sequence. Root `AGENTS.md` carries the working contract and routes to supporting documents when their topic applies. First-time project customization has its own workflow.

Do not maintain platform-specific instruction files that duplicate the shared contract. If a tool requires a platform-specific file or skill discovery path, keep the adapter minimal and reference the authoritative shared material.

## Consequences

- Humans review one agent contract instead of several.
- Agents have consistent expectations across tools.
- Tool-specific behavior can still live in local ignored settings or small compatibility shims.
- The project avoids split-brain instruction drift.
