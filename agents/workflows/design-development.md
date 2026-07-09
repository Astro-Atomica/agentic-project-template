# Design Development Workflow

Use this workflow when helping a user develop or revise `agents/DESIGN.md`.

## Intent

`agents/DESIGN.md` should describe the project's visual identity for coding agents. It should follow the `DESIGN.md` format from `google-labs-code/design.md`: machine-readable YAML front matter for exact design tokens, followed by Markdown prose that explains the rationale and application of those tokens.

Do not seed `agents/DESIGN.md` with default values. Only add tokens, sections, or prose after the user provides direction, source material, screenshots, brand artifacts, or approval.

When the user makes a design language request, update and maintain the project
design language as part of the task. Do not leave design intent only in chat,
component code, screenshots, or one-off implementation notes. Record durable
decisions in `agents/DESIGN.md` and update supporting design-system docs under
`agents/design/` when the rule, review method, example, or reusable pattern
belongs there.

Design language documentation must carry soft meaning as well as exact values.
For important choices, explain the inspiration, intent, user-facing meaning,
when the rule should hold, when it can be broken, and when a new rule should be
defined.

Typography should be documented by semantic font role first: `hero font`,
`primary font`, `secondary font`, and `mono font`. Define the chosen font or
fallback stack in as few implementation surfaces as practical, and describe how
each role is applied differently across scenarios and why.

## Workflow

1. Confirm the design target: product, audience, surfaces, brand constraints, and whether the file is new or a revision.
2. Gather source material before writing: existing app screens, screenshots, brand files, CSS variables, component libraries, style guides, or user-described preferences.
3. Identify known values and unknowns. Ask focused questions for missing decisions instead of inventing defaults.
4. Check whether the request changes the durable design language, a reusable design-system rule, or only the local implementation.
5. Draft YAML tokens only for values that are known, chosen, or derived from approved source material.
6. Draft Markdown rationale in the canonical section order when those sections apply: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
7. In Typography, prefer semantic roles before use cases: `hero font`, `primary font`, `secondary font`, `mono font`, then any approved project-specific roles.
8. Explain rationale for each meaningful design choice, including why it communicates the right meaning to users and when future work should keep, break, or extend the rule.
9. Update supporting docs under `agents/design/` when the decision changes design review criteria, reusable examples, patterns, or system-level guidance.
10. Preserve unknown or future sections by leaving them absent. Do not add placeholder token values.
11. Validate references and contrast when tooling is available. Prefer `npx @google/design.md lint agents/DESIGN.md` when the project can run it.
12. If visual verification is possible, render or inspect a representative screen using the design file and capture observations.
13. Summarize what design decisions were encoded, what remains undecided, what design-system docs changed, and what verification was run.

## Review Checklist

1. Tokens are exact values, not vague prose.
2. Prose explains why and how to apply the tokens.
3. Token references resolve.
4. Colors used together meet the project's accessibility target.
5. Typography uses semantic font roles and keeps implementation definitions centralized.
6. Design rules explain when to follow, break, or extend them.
7. Reusable design review criteria, examples, or system guidance are updated under `agents/design/` when needed.
8. Section order follows the standard when sections are present.
9. The file contains no secrets, private user data, local paths, or unapproved brand assets.
10. The file does not contain invented defaults.
