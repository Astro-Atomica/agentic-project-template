# Design Development Workflow

Use this workflow when helping a user develop or revise `agents/DESIGN.md`.

## Intent

`agents/DESIGN.md` should describe the project's visual identity for coding agents. It should follow the `DESIGN.md` format from `google-labs-code/design.md`: machine-readable YAML front matter for exact design tokens, followed by Markdown prose that explains the rationale and application of those tokens.

Do not seed `agents/DESIGN.md` with default values. Only add tokens, sections, or prose after the user provides direction, source material, screenshots, brand artifacts, or approval.

## Workflow

1. Confirm the design target: product, audience, surfaces, brand constraints, and whether the file is new or a revision.
2. Gather source material before writing: existing app screens, screenshots, brand files, CSS variables, component libraries, style guides, or user-described preferences.
3. Identify known values and unknowns. Ask focused questions for missing decisions instead of inventing defaults.
4. Draft YAML tokens only for values that are known, chosen, or derived from approved source material.
5. Draft Markdown rationale in the canonical section order when those sections apply: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
6. Preserve unknown or future sections by leaving them absent. Do not add placeholder token values.
7. Validate references and contrast when tooling is available. Prefer `npx @google/design.md lint agents/DESIGN.md` when the project can run it.
8. If visual verification is possible, render or inspect a representative screen using the design file and capture observations.
9. Summarize what design decisions were encoded, what remains undecided, and what verification was run.

## Review Checklist

1. Tokens are exact values, not vague prose.
2. Prose explains why and how to apply the tokens.
3. Token references resolve.
4. Colors used together meet the project's accessibility target.
5. Section order follows the standard when sections are present.
6. The file contains no secrets, private user data, local paths, or unapproved brand assets.
7. The file does not contain invented defaults.
