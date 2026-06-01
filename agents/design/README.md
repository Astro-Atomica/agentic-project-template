# Design Guidance

## Living Design Examples

Ground reusable design elements in stateless examples that are simple to render, inspect, and compare.

1. Keep reusable UX patterns visible in a flat test surface, story page, design route, or rendered artifact.
2. Make each example reachable directly without long navigation, authentication, or fragile setup.
3. Prefer stateless examples that accept explicit props, tokens, fixtures, or serialized state.
4. Keep validators simple enough for agents to run often: screenshot, DOM inspection, contrast check, snapshot, or visual diff.
5. Treat complex setup as a design-testing smell. If a UX element requires five steps to see, that is five chances to take the wrong path or skip visual inspection.
6. Use living examples as the source for reusable modules, not one-off screenshots hidden in discussion.

The goal is fast visual convergence. Flat bulk UX test surfaces are easier to inspect, easier to screenshot, and harder to forget.
