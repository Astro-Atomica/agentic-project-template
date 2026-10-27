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

## Put the Page's Primary Value Above the Fold

The initial visible viewport must communicate or deliver the page's primary
value before the user scrolls. Choose that value according to the page's purpose
and the user's task; document it for each page type.

| Page purpose | Value to prioritize in the initial viewport |
| --- | --- |
| Sales or conversion | A clear offer/benefit and a meaningful primary call to action (CTA) |
| Web app or tool | The primary task, useful controls, current work, or an actionable result |
| Dashboard or status | The most useful summary, current status, or information needing attention |
| Documentation, reference, or content | Clear topic/context and useful information or a direct way to find the answer |
| Search or browse | Search/filter controls and useful results or categories |

A CTA is appropriate when it serves that purpose; it is not a universal
requirement for every site or app. Avoid letting decorative heroes, oversized
branding, or introductory copy push the actual value out of the initial view.

The fold depends on viewport size and browser UI. Verify representative desktop
and mobile initial views, accounting for persistent navigation and overlays.
Preserve readable text, accessible controls, and natural scrolling rather than
shrinking or crowding the interface to fit everything above an arbitrary line.
Use the post-prototype test sitemap to inspect this across page types.

## Responsive Design Across Screen Sizes

Keep the site or app useful across a wide range of viewport sizes as devices and
usage patterns change. Prioritize currently popular mobile sizes for the intended
audience, then randomly sample other sizes within the supported range and rate
how well users can complete the page's primary task. Include tablet and desktop
layouts where supported. Choose layout breakpoints where content needs to adapt,
rather than relying only on a fixed list of device models.

Follow the [responsive review guidance](design/responsive-design.md) for target
selection, reproducible sampling, usefulness ratings, and regression checks.

## Keep Important Actions Accessible While Scrolling

**Sales sites and sales pages:** On long mobile sales pages, consider a sticky
primary CTA such as "Buy now", "Book an appointment", or "Start free trial".
Keep it available as visitors scroll through the offer so they can act without
searching for the original button. Use a clear label and preserve any context
needed to understand the action. Add persistence where it helps the purchase or
conversion flow; a sticky button is not mandatory on every sales page.

**Other sites and apps:** Keep important actions or controls conveniently
accessible when doing so helps the user's current task. Choose the behavior and
placement to suit the experience; persistent controls are optional, and some
pages need none. Avoid imposing a sales-style CTA or bottom bar on every app.

In either case, persistent UI must not obscure content, focused fields, other
controls, or the final portion of the page. Account for small viewports, safe
areas, zoom, and the on-screen keyboard. Verify the actual scrolling and
interaction behavior as part of the responsive review.

## Load Quickly, Show Progress, Keep Layouts Stable

- Aim to deliver useful above-the-fold content within **one second on
  representative devices and networks**.
- Render progressively, prioritize primary interactions, and defer nonessential
  assets and below-the-fold work.
- Show honest loading feedback and reserve space for incoming content to prevent
  layout shifts.
- Measure before optimizing. Once the experience is consistently fast and
  responsive, pursue further gains only when the user benefit justifies the
  complexity and maintenance cost.

Define the useful-content milestone and representative test conditions for the
project. Check initial loads and subsequent navigation, recording device/network
conditions and cold versus warm caches. Inspect responsiveness and layout
stability while assets load; a quick skeleton alone does not satisfy the
useful-content goal. Prioritize measured bottlenecks over speculative tuning.

## Web Readiness

Use the [web readiness checklist](workflows/web-readiness.md) for page metadata,
icons, alt-text timing, error/recovery states, forms, confirmations, policy pages,
contact details, analytics, and the required post-prototype test sitemap.
Supporting documents define those requirements; keep project-specific visual
choices here and avoid copying the checklist into this file.

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
