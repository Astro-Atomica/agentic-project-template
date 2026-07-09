# CSS Rules

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.

## Goals

CSS should make layout and styling predictable, inspectable, and easy to change without creating a parallel application architecture inside selectors.

1. Prefer readable semantic selectors for durable UI concepts.
2. Prefer small utility classes for generic layout, spacing, typography, and state composition.
3. Use design tokens, CSS custom properties, or project config for values that repeat.
4. Keep selectors shallow enough that changing markup does not require hunting through fragile descendant chains.
5. Keep CSS close to the component, surface, or system it styles according to the project's conventions.

## Native Nesting

Use native CSS nesting to keep related selectors together and make component scope obvious.

Native CSS nesting does not support Sass-style selector concatenation. Write
the complete class name when nesting BEM-like element or modifier selectors.

Write:

```css
.component {
  & .component__header { /* ... */ }
  & .component__actions { /* ... */ }

  & .child-list {
    transition: opacity 140ms ease-out;

    &.child-list--is-updating {
      opacity: 0;
      transition: none;
    }
  }
}
```

Do not append BEM element or modifier suffixes directly to the nesting
selector. Native CSS nesting does not perform string concatenation.

Good CSS is a balancing act between building a modular zero-semantic style/layout framework and using semantics to keep CSS readable and meaningful.

Some CSS can go as far as mixing styling with microformat standards.

```css
button.action {}
```

is more semantic than:

```css
.text-2xl .font-medium {}
```

Mixing utility classes and semantic selectors can still be very useful:

```css
button.action .text-lg {}
```

## Selector Semantics

Selectors should communicate intent without becoming overly coupled to markup.

1. Use semantic class names for stable product or component concepts.
2. Use element selectors only when the element meaning matters, such as `button.action`, `nav.primary`, or `article.summary`.
3. Avoid selectors that depend on incidental DOM depth, such as long chains of nested `div` selectors.
4. Avoid encoding visual values directly into semantic class names unless the class is intentionally a utility.
5. Do not use IDs for styling unless the project has an explicit reason; IDs are too specific and hard to override.

Good:

```css
.component {
  & .component__actions {}
  & button.action {}
}
```

Risky:

```css
#settings div div button {}
.large-highlight-box {}
```

## Tokens And Values

Repeated visual values should come from tokens, CSS custom properties, or project configuration.

1. Avoid magic numbers in CSS.
2. Name repeated colors, spacing, radii, shadows, durations, and z-index layers.
3. Prefer semantic token names when the value has design meaning, such as `--surface-primary` or `--motion-fast`.
4. Prefer scale token names when the value belongs to a system, such as `--space-3` or `--radius-sm`.
5. Keep one source of truth for design values; do not duplicate the same hex color or spacing value across unrelated files.

Good:

```css
.surface {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--surface-primary);
}
```

Risky:

```css
.surface {
  padding: 17px;
  border-radius: 11px;
  background: #f7f5f2;
}
```

## Layout

Layout CSS should make sizing, flow, and constraints explicit.

1. Prefer modern layout primitives: grid, flexbox, container queries, logical properties, and intrinsic sizing.
2. Define stable dimensions for controls, toolbars, grids, canvases, cards, and fixed-format UI elements.
3. Use `min-*`, `max-*`, `aspect-ratio`, and named grid tracks to prevent content from causing accidental layout shifts.
4. Avoid absolute positioning for normal document flow.
5. Use absolute positioning only for overlays, anchored affordances, canvas layers, or deliberate visual effects.
6. Prefer logical properties like `padding-inline`, `margin-block`, and `inset-inline` when direction-aware layout matters.

## Responsiveness

Responsive CSS should adapt structure, not merely shrink everything.

1. Do not scale font size directly with viewport width, unless that is a requirement of the component, module, page, project, widget, app.
2. Use breakpoints or container queries when layout actually changes.
3. Let text wrap naturally unless the UI requires truncation.
4. When truncating text, provide enough context through labels, titles, tooltips, or adjacent metadata.
5. Test narrow and wide layouts when the UI is visual, interactive, or content-heavy.

## State And Interaction

State styles should be explicit, accessible, and easy to reason about.

1. Represent durable component states with named classes or attributes.
2. Prefer ARIA and data attributes for state selectors when they reflect real UI state, such as `[aria-expanded="true"]` or `[data-state="open"]`.
3. Use a state class in the ancestor chain when one state intentionally toggles presentation across descendants.
4. Keep ancestor state selectors scoped to the component or surface that owns the state.
5. Always define visible focus states for interactive elements.
6. Do not remove outlines unless replacing them with an equally visible focus treatment.
7. Respect reduced-motion preferences for transitions, animations, and scroll effects.

Example:

```css
.component {
  &.component--is-busy .component__content {
    opacity: 0.6;
    pointer-events: none;
  }

  & [aria-expanded="true"] {
    color: var(--text-active);
  }

  @media (prefers-reduced-motion: reduce) {
    & .component__content {
      transition: none;
    }
  }
}
```

## Specificity

Specificity should stay low and intentional.

1. Prefer class, attribute, and `:where()` selectors over deeply nested selectors.
2. Treat `!important` as a warning sign. If it is required to achieve a result, there is likely a CSS, HTML, or JavaScript architecture flaw forcing the override.
3. Flag any `!important` usage as technical debt for later code review, even when it is temporarily necessary.
4. Allow `!important` only for deliberate utility overrides, integration boundaries, or emergency patches with a clear explanation.
5. Keep component selectors scoped to the component root.
6. Avoid global resets that silently change third-party, embedded, or generated UI unless that is the explicit goal.
7. Use cascade layers only when the project has a clear layer strategy.

## Components And Utilities

Good CSS often mixes semantic component classes and small utility classes.

1. Use component classes for durable UI concepts.
2. Use utilities for generic, repeatable styling that does not deserve a custom component name.
3. Avoid making every style a utility if the result hides product meaning.
4. Avoid making every style a semantic class if the result duplicates generic layout rules.
5. Prefer local composition over copy-pasting near-identical component CSS.

## Accessibility

CSS can create or destroy accessibility.

1. Preserve readable contrast.
2. Preserve keyboard focus visibility.
3. Do not use color alone to communicate state.
4. Avoid hiding content from assistive technology accidentally with display or visibility rules.
5. Be careful with `pointer-events`, `user-select`, overflow clipping, scroll locking, and fixed layers.

## Review Checklist

1. Selectors are readable, scoped, and not overly specific.
2. Native nesting is used where it improves locality.
3. Repeated values use tokens or custom properties.
4. Layout constraints are explicit and stable.
5. Responsive behavior was considered for narrow and wide containers.
6. Interactive states include hover, active, disabled, focus, and reduced-motion behavior when relevant.
7. CSS changes can be visually verified in the app, direct inspection tooling, screenshot, browser when applicable, or rendered artifact.
