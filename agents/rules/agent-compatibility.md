# Agent Compatibility

`AGENTS.md` is the canonical instruction source. The shared files under `agents/` remain ordinary repository documents: an entrypoint being loaded does not prove that all linked files were also loaded or followed.

## Review Date And Scope

The initial scaffold was developed in May–July 2026. Coding-agent discovery and configuration have changed since those initial choices. The notes below reflect vendor documentation checked on **2026-09-29**, rather than a compatibility guarantee inherited from the original scaffold.

No version-pinned end-to-end client matrix has been recorded for this repository. Root guidance was available and followed in the Codex desktop review session, but that session did not isolate automatic file discovery. Claude Code and Cursor guidance below was verified against documentation, not by running those clients. Windsurf discovery could not be reverified against accessible current vendor documentation during this pass.

## Client Setup

| Client | Current evidence and setup |
| --- | --- |
| Codex | Start at the repository root. Official documentation describes discovering `AGENTS.md` along the path from the project root to the working directory, with override precedence and a configurable size limit. Ask it to identify active instructions and explicitly read the linked shared stack. [Official OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md). |
| Claude Code | Current documentation describes native `AGENTS.md` discovery starting with v2.1.277, subject to its instruction settings and session configuration. This repository's existing `CLAUDE.md` contains only `@AGENTS.md`; the import still provides the shared root instructions. A project `CLAUDE.md` can take precedence over native discovery, so check the loaded files with `/context` and explicitly read applicable nested guidance. The import is an existing adapter, not a promise of support for older clients. [Claude Code instructions](https://code.claude.com/docs/en/memory#agentsmd). |
| Cursor Agent | Current documentation supports root and nested `AGENTS.md` files. Open the repository root and confirm the relevant instructions are active. This is guidance for Agent; it does not imply the same behavior for Tab completion or every other Cursor feature. [Cursor rules](https://cursor.com/docs/rules#agentsmd). |
| Windsurf or another client | Do not assume that an older setup recipe still describes the installed client. Open the repository root, explicitly ask it to read `AGENTS.md` and the linked shared stack, then verify the instructions it used. Native discovery for Windsurf was not confirmed in this documentation refresh. Consult the installed client's current vendor help before adding any adapter. |

## Verify Adoption

At the start of a new session, ask:

```text
Identify the instruction files active for this repository. Read root AGENTS.md,
README.md, agents/README.md, agents/PRINCIPLES.md, and applicable workspace
guidance. State the privacy checks and verification commands relevant to this
task before editing.
```

Use the client's loaded-context view or logs when available to corroborate its response. Check that the resulting work follows the instructions; an agent's own statement is not a complete discovery test. Keep raw session captures and local configuration in ignored folders.

When recording a compatibility result, include the date, client version, interface/session mode, launch directory, relevant instruction settings, files actually loaded, and behavior observed. Recheck on client upgrades and when instruction precedence changes. If an adapter is required for the chosen client, keep it minimal and point it to `AGENTS.md`; do not copy the shared rules or add support for older versions without an explicit support decision.
