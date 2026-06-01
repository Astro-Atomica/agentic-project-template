# Event Stream Rules

Use this file for event-stream-specific rules about ordering, backpressure, replay, subscriptions, and observability.

Reference: [Stream processing](https://en.wikipedia.org/wiki/Event_stream_processing).

In software development, event streams model work as ordered records over time. They are useful when the order, replayability, durability, or auditability of events matters: user actions, domain events, telemetry, queue messages, workflow transitions, logs, and integration feeds. Good event-stream code makes ordering, delivery guarantees, idempotency, retention, schema evolution, and backpressure explicit instead of hiding them in incidental callbacks or scattered side effects.

In agentic programming, event streams give agents an observable history to inspect instead of asking them to infer behavior from a final state. A small event log, test trace, workflow journal, or queue snapshot can show what happened, what failed, what retried, and what should happen next. This is especially useful across context compaction and handoff because the stream becomes evidence the next agent can replay, summarize, or validate.

## Related Patterns

1. [Stigmergy](stigmergy.md) treats event streams as durable traces that coordinate future work through the shared environment.
2. [Functional reactive programming](functional-reactive-programming.md) often consumes streams and derives state from them through deterministic data flow.
3. [State machines](state-machines.md) use events as transition triggers and make valid next states explicit.
4. [Object-oriented design](object-oriented.md) can wrap producers, consumers, subscriptions, and event stores behind stable interfaces.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
