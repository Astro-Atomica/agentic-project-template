# Design Guidance

## Design Language Maintenance

Design language requests must update the project design language, not just the
current screen or component. Keep durable visual identity, rationale, and
design-system guidance in:

- `agents/DESIGN.md` for the canonical project design language.
- `agents/design/` for supporting design-system notes, examples, review
  methods, and reusable artifacts.

The design language is not only a numeric specification. It should preserve the
inspiration, intent, and reasoning behind design decisions so future agents and
humans can understand when to keep a rule, when to break it, and when to define
a new rule.

## Semantic Typography

Document fonts around semantic roles before documenting individual surfaces.
Use this core vocabulary unless the project has a clear reason to add another
role:

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

Each semantic font role should explain:

1. What font or fallback stack implements the role.
2. What product voice or user meaning the role carries.
3. Where the role is normally applied.
4. How exceptions differ and why they are justified.
5. Where the role is defined in implementation so font choices stay centralized.

Components should consume semantic font roles through tokens, CSS variables,
theme configuration, or platform style constants instead of hard-coding font
families throughout the app.

## Living Design Examples

Ground reusable design elements in stateless examples that are simple to render, inspect, and compare.

1. Keep reusable UX patterns visible in a flat test surface, story page, design route, or rendered artifact.
2. Make each example reachable directly without long navigation, authentication, or fragile setup.
3. Prefer stateless examples that accept explicit props, tokens, fixtures, or serialized state.
4. Keep validators simple enough for agents to run often: screenshot, DOM inspection, contrast check, snapshot, or visual diff.
5. Treat complex setup as a design-testing smell. If a UX element requires five steps to see, that is five chances to take the wrong path or skip visual inspection.
6. Use living examples as the source for reusable modules, not one-off screenshots hidden in discussion.

The goal is fast visual convergence. Flat bulk UX test surfaces are easier to inspect, easier to screenshot, and harder to forget.

## Design Review

A design review should evaluate whether the current UI expresses the documented
design language, not merely whether it looks polished in isolation.

Check:

1. The design follows documented typography, color, spacing, motion, shape, and
   component rules.
2. Any exception is intentional, explained, and added back to the design
   language or design-system docs when it should be reusable.
3. Visual choices communicate product meaning and user priority.
4. Repeated values are centralized through semantic tokens, roles, or reusable
   patterns.
5. The review uses an observation path such as a running app, screenshot,
   rendered artifact, story, visual test page, or visual diff.
