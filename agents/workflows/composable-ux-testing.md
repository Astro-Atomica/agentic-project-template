# Composable UX Testing Workflow

Use this workflow for UX features that transform state, data, layout, navigation, or visible interaction.

## Principle

Every UX step should be testable in isolation.

Model complex flows as a sequence:

```text
A -> B -> C -> D
```

To test `B -> C`, start from a known `B` fixture or state, apply one operation, and assert the resulting `C` state or view. Do not make every test walk through `A -> B -> C -> D`.

## Workflow

1. Name the user-visible flow and split it into small state transitions.
2. Define a stable input for each step: fixture, serialized state, mock service response, route state, or setup function.
3. Extract the transformation behind each step into a testable unit when possible.
4. Assert one step at a time: input state, operation, output state.
5. Add at least one thin integration test that proves the steps connect.
6. For visual UX, pair the isolated state with an easy-to-render test surface or story.
7. Keep fixtures small, readable, and deterministic.

## Design Goal

The best UX tests make the target state cheap to reach. If a state requires five manual clicks before it can be inspected, that is five chances for the agent to take the wrong path or skip visual validation. Prefer direct fixtures, state loaders, stories, debug routes, or flat test pages that show the state immediately.

## Checklist

1. Each meaningful UX step has a known input and expected output.
2. Transformations are deterministic.
3. Fixtures can be loaded without manual navigation.
4. Visual states can be rendered directly for inspection.
5. End-to-end tests exist only where they add confidence beyond step tests.
