# Design Development Workflow

Use this when a request establishes or changes the project's visual language. Keep actual design decisions in [DESIGN.md](../DESIGN.md) and supporting examples in [design/](../design).

1. Inspect the user's direction, existing screens, brand material, and implementation tokens. Clarify only decisions that block useful progress.
2. Record concrete choices and their intent in DESIGN.md: values, semantic roles, usage, and justified exceptions. Keep unknown choices absent. A local styling change needs a global rule only when it establishes a reusable decision.
3. Follow the [current DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) used by the scaffold: optional YAML front matter for exact tokens and Markdown rationale. Keep present sections in order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. Omit undecided sections and token groups; update `omitted` when adding approved values. Preserve existing project decisions and any intentional extensions.
4. Inspect representative screens or rendered states against the documented language and accessibility requirements. Use existing stories, fixtures, or direct views when available.
5. Update durable decisions and summarize what changed, what was verified, and what remains undecided.

Apply decisions through shared tokens or the framework's conventions. The upstream format is currently alpha; check changes to the specification when adopting a new validator version.

Validate this file with the project's configured DESIGN.md linter. For an on-demand check, the dot-free CLI alias works across platforms:

```text
npx --yes --package="@google/design.md" designmd lint agents/DESIGN.md
```

Use `npx.cmd` in Windows PowerShell when needed. This command needs Node.js/npm and may download the validator; it does not require adding a dependency to the scaffold. The alpha format and published CLI 0.4.0 were checked on 2026-09-29.
