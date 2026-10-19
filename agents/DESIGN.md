# Design Language

This file is the canonical design language for the project once a project has
chosen visual direction. Do not add placeholder brand values, fonts, colors, or
tokens before they are known, approved, or derived from project source material.

## Maintenance Rule

When a user makes a design language request, treat the design language as a
living project artifact. Update this file and any supporting design-system docs
under `agents/design/` so the decision survives beyond the current chat,
implementation, or review.

Design guidance should include both exact values and soft intent. Tokens and
code-facing values explain what to use. Prose explains why the choice exists,
what meaning it carries for users, when to keep the rule, when to break it, and
when a new rule should be defined.

## Typography Contract

Document fonts by semantic role before documenting individual use cases. Prefer
a small set of project-level font roles such as:

- `hero font` - highly branded display typography for the strongest identity
  moments.
- `primary font` - the default font. It should be comfortable to read and is
  used for headers, titles, short strong text, interface elements, and primary
  interface objects.
- `secondary font` - a comfortable supporting font for less important text,
  smaller controls, longer multiline text, and secondary interface objects.
- `mono font` - typography for code, raw data, numbers with even spacing or
  alignment requirements, and file names. Do not use it for ordinary numbers
  inside regular text blocks.

For each role, document:

1. The selected font family or fallback stack, once chosen.
2. The inspiration, intent, and user-facing meaning behind the choice.
3. The default surfaces or text types that use it.
4. The few approved exceptions, including how and why the application differs.
5. The rule for adding another semantic font role instead of creating one-off
   styling.

Keep font definitions centralized in as few implementation surfaces as the
project allows, such as design tokens, CSS variables, theme config, or platform
style constants. Components should reference semantic roles instead of
hard-coding font families.

## Placeholder Text And Loading States

Default to deliberately unreadable placeholders: block/Flow, scribble, or
redacted styles. The first time a user requests lorem ipsum or placeholder text
in a project, give them one opportunity to preserve readable Latin lorem ipsum,
unless they have already specified a preference:

> I'll use unreadable block or scribble placeholders so sample content is clearly
> unfinished. Would you prefer to keep readable Latin lorem ipsum instead?

Honor an explicit choice of readable text; otherwise use the unreadable default.
Record the preference here for the project or its relevant surface, along with
whether the initial choice has been offered. Distinguish an explicit preference
from an applied default. Do not repeatedly ask; reuse the choice unless the user
changes direction. Select the unreadable style to suit the project's design
language without requiring a separate font-selection question.

Block and scribble styles make unfinished content visibly distinct from actual
copy, helping reviewers focus on layout without mistaking sample text for the
content being previewed. They can also represent template cards while data loads,
then be replaced with real data in the normal semantic font role.

See [placeholder patterns](design/placeholders.md) for font examples, loading
behavior, accessibility, and verification guidance. The specific fonts are
examples, not prescribed brand typography.

## Review Standard

A design review should judge whether the design language constrains the product
to a uniform look and feel that communicates meaning to users. Review against:

1. Consistency: new UI follows the documented design language unless an
   intentional exception is documented.
2. Meaning: typography, color, spacing, motion, shape, and component choices
   communicate the intended product tone and user priority.
3. Rationale: important choices explain their inspiration, intent, and reason,
   not only their numeric values.
4. Centralization: repeated visual decisions are represented by semantic tokens,
   roles, or reusable patterns instead of scattered literals.
5. Evolution: new needs either fit an existing rule, justify a documented
   exception, or define a new rule in the design language.
6. Observability: the reviewed UI can be inspected through a running app,
   screenshot, rendered artifact, story, visual test surface, or comparable
   observation path.
