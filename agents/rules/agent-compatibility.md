# Agent Compatibility

`AGENTS.md` is the canonical instruction source. The shared files under `agents/` remain ordinary repository documents: an entrypoint being loaded does not prove that all linked files were also loaded or followed.

## Review Date And Scope

The initial scaffold was developed in May–July 2026. Coding-agent discovery and configuration have changed since those initial choices. The notes below reflect vendor documentation checked on **2026-09-29**, rather than a compatibility guarantee inherited from the original scaffold.

No version-pinned end-to-end client matrix has been recorded for this repository. Root guidance was available and followed in the Codex desktop review session, but that session did not isolate automatic file discovery. Claude Code guidance below was verified against documentation, not by running that client. Windsurf discovery could not be reverified against accessible current vendor documentation during this pass.

## Client Setup

| Client | Current evidence and setup |
| --- | --- |
| Codex | Start at the repository root. Official documentation describes discovering `AGENTS.md` along the path from the project root to the working directory, with override precedence and a configurable size limit. Confirm active instructions during setup; read supporting documents according to the task. Native repository skills use `.agents/skills`, rather than the visible `agents/skills` notes directory. [Instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skill discovery](https://learn.chatgpt.com/docs/build-skills). |
| Claude Code | Current documentation describes native `AGENTS.md` discovery starting with v2.1.277, subject to its instruction settings and session configuration. This repository's existing `CLAUDE.md` contains only `@AGENTS.md`; the import still provides the shared root instructions. A project `CLAUDE.md` can take precedence over native discovery, so check the loaded files with `/context` and explicitly read applicable nested guidance. The import is an existing adapter, not a promise of support for older clients. [Claude Code instructions](https://code.claude.com/docs/en/memory#agentsmd). |
| Windsurf or another client | Do not assume that an older setup recipe still describes the installed client. Open the repository root, explicitly ask it to read `AGENTS.md` and applicable scoped instructions, then verify the instructions it used. Native discovery for Windsurf was not confirmed in this documentation refresh. Consult the installed client's current vendor help before adding any adapter. |

## Verify Adoption

When setting up or upgrading a client, use a small representative task to check adoption. A useful prompt is:

```text
Identify the instruction files active for this repository. Follow root AGENTS.md
and applicable scoped guidance. Read supporting documents only when they apply
to the task, and identify the relevant verification and privacy checks.
```

Use the client's loaded-context view or logs when available to corroborate its response. Check that the resulting work follows the instructions; an agent's own statement is not a complete discovery test. Keep raw session captures and local configuration in ignored folders.

When recording a compatibility result, include the date, client version, interface/session mode, launch directory, relevant instruction settings, files actually loaded, and behavior observed. Recheck on client upgrades and when instruction precedence changes. If an adapter is required for the chosen client, keep it minimal and point it to `AGENTS.md`; do not copy the shared rules or add support for older versions without an explicit support decision.

## Maintaining Instructions

The September 2026 guidance refresh favors a short working contract, task-scoped references, and explicit completion criteria. Preserve concrete project checks and boundaries; retire repeated testing reminders and rigid recipes when they no longer add confidence. OpenAI's [instruction maintenance guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) and Anthropic's [current Opus guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) informed this choice. These are documentation-based recommendations, not comparative client evaluations in this repository.

Keep model-specific effort settings and unattended API-loop mechanics in the client's configuration or harness. They are not prerequisites for adopting this template. Concrete design direction, resource cleanup, privacy gates, and a clear definition of completion remain useful across clients.
