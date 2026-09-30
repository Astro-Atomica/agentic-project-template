# Agents

Shared operating context for coding agents and humans working with them.

## Contents

- [PRINCIPLES.md](PRINCIPLES.md) - shared coding principles for project work
- [DESIGN.md](DESIGN.md) - project visual identity for coding agents
- [code](code) - language, platform, environment, and pattern guidance with small customization stubs
- [commit-templates](commit-templates) - reusable commit message templates and commit metadata patterns
- [design](design) - supporting design guidance and artifacts
- [rules](rules) - durable repo conventions and safety rules
- [model routing](rules/model-routing.md) - empty tables for project users to record models and task-fit estimates over time
- [privacy-policy.json](privacy-policy.json) - project publication allowlists and sensitive-pattern policy
- [workflows](workflows) - repeatable task procedures
- [skills](skills) - reusable capability notes and native skill setup guidance
- [personas](personas) - optional specialist roles
- [tools](tools) - reusable repo-local tools, scripts, and command wrappers for agents

## Convention

Keep this folder visible. Hidden dotfolders are reserved for tools that require them or local ignored state.

Read the documents relevant to the task. This index is not a startup checklist; root `AGENTS.md` provides the shared working contract and task-specific routes.

Publication safety is operationalized by [rules/privacy-and-publication.md](rules/privacy-and-publication.md) and [tools/privacy_preflight.py](tools/privacy_preflight.py).

See [Agent Compatibility](rules/agent-compatibility.md) for dated client setup notes and the difference between documented discovery and runtime verification.
