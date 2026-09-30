# Skills And Workflow Notes

This visible directory can hold shared capability notes and references. Ordinary Markdown here is not automatically an installed skill.

Native skills use a `SKILL.md` manifest with a short name, description, task-specific instructions, and optional resources. Put discoverable skills in the chosen client's supported location, and document setup instead of assuming discovery. Current Codex repository discovery uses `.agents/skills`; see [official skill documentation](https://learn.chatgpt.com/docs/build-skills) and the dated [compatibility notes](../rules/agent-compatibility.md).

Keep each skill focused on a recurring task. Load detailed references when needed and retain one authoritative source for shared instructions. A thin adapter may reference material here where the client supports it; verify the loading behavior.

Existing workflows can remain ordinary documents. Add a native skill only when discovery and reuse improve the project. Keep credentials and private machine configuration local; review any required tool-path ignore exceptions before publishing them.
