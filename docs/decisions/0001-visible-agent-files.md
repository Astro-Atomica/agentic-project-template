# 0001 - Keep Agent Guidance Visible

**Status:** Accepted

## Context

Many tools use dotfolders for configuration. In public repositories, dotfolders can make human-authored project structure feel hidden or private even when the files are checked in.

Agentic projects need their operating rules to be easy for humans to inspect, review, and improve.

## Decision

Human-authored agent guidance lives in visible folders:

- `AGENTS.md`
- `agents/`
- `docs/`
- `templates/`

Tool-required dotfolders are allowed only when the tool expects that exact path. Local editor/tool state is ignored by default.

## Consequences

- The GitHub project page stays cleaner and more understandable.
- Humans can audit agent behavior without hunting through hidden folders.
- Some tools may still create local dotfolders, but those folders are not part of the public scaffold unless intentionally committed.
