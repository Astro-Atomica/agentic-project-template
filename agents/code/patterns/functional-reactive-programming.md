# Functional Reactive Programming (FRP) Rules

Use this file for FRP-specific rules about signals, streams, derived state, effects, and deterministic data flow.

Reference: [Functional reactive programming](https://en.wikipedia.org/wiki/Functional_reactive_programming).

In software development, functional reactive programming models changing values as signals, streams, and derived computations. Use it when state needs to update predictably from inputs over time, especially in interfaces, simulations, dashboards, editors, and asynchronous systems. Good FRP keeps pure derivations separate from effects, makes dependency direction clear, avoids hidden mutation, and gives every subscription or effect a visible lifecycle.

In agentic programming, FRP helps agents reason about cause and effect. When a UI, workflow, or data pipeline is expressed as inputs, derived state, and effects, an agent can test a small input change and observe the expected output without spelunking through unrelated imperative code. This keeps edit-review loops tight because the agent can validate one reactive path at a time.

## Related Patterns

1. [Event streams](event-streams.md) provide time-ordered inputs that FRP systems can transform into derived state.
2. [State machines](state-machines.md) can bound reactive behavior by making valid states and transitions explicit.
3. [Stigmergy](stigmergy.md) appears when reactive traces, logs, snapshots, or validation surfaces guide future work.
4. [Object-oriented design](object-oriented.md) and [mixins](mixins.md) can package reactive sources, derived models, and effect lifecycles behind reusable boundaries.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
