# Placeholder Patterns

Follow the default and one-time readable-text opt-out in
[DESIGN.md](../DESIGN.md#placeholder-text-and-loading-states). Prefer deliberately
unreadable shapes for placeholder content so reviewers can assess layout and
content density without mistaking it for final copy. Use readable Latin lorem
ipsum when the user explicitly chooses it. Actual copy under review remains
readable.

## Presentation Options

| Style | Examples | Useful for |
| --- | --- | --- |
| Block | Flow Block, Flow Rounded, Flow Circular, or Redacted | Abstract text rows and layout previews |
| Scribble | Redacted Script in Light, Regular, or Bold | Handwritten-looking abstract copy and informal wireframes |
| Readable (explicit opt-out) | Latin lorem ipsum in the normal text font | Text flow, wrapping, and readable prototype content when requested |

[Google Fonts' Flow and Redacted overview](https://fonts.googleblog.com/2022/01/flow-and-redacted-check-out-these-new.html)
documents these families and links to their font pages. The
[Flow source](https://github.com/HYPD/flow-typeface) and
[Redacted source](https://github.com/christiannaths/redacted-font) include SIL Open
Font License terms. Check the license shipped with the selected font and retain
required notices when distributing assets. These are examples, not dependencies
the template installs or requires.

## Loading Cards

Block or scribble fonts can render the shape of a template card before its data
arrives. Use synthetic placeholder content with representative line lengths and
reserve roughly the final card dimensions. On success, replace it with real data
and restore the appropriate semantic font role. Show an explicit empty or error
state when appropriate instead of leaving the card looking perpetually busy.

Keep the initial shell lightweight. A placeholder font is a presentation technique,
not a guarantee of faster loading; do not delay rendering to download it. CSS
shapes are another option when the font is unavailable or would add unnecessary
loading cost. Keep placeholder styling centralized and scoped so it cannot leak
into real content.

Hide decorative placeholders from assistive technology, mark the containing
region busy while loading, and provide a concise accessible loading status.
Clear the busy state when loading ends. If motion is used, respect reduced-motion
preferences. A redacted-looking font only changes appearance: use synthetic text,
never rely on it to conceal sensitive data still present in the document.

## Verification When Implemented

Inspect the selected preview style and, for loading cards, the loading, populated,
empty, and error states. Check narrow layouts, delayed or unavailable fonts,
layout movement on replacement, and the accessible loading announcement. Confirm
that real data is readable and no placeholder styling remains after loading.
