# Error Handling / Result Types Rules

Use this file for error-handling- and result-type-specific rules about recoverable failures, exceptional failures, typed outcomes, propagation, logging, retries, and user-facing error boundaries.

References: [Exception handling](https://en.wikipedia.org/wiki/Exception_handling), [Result type](https://en.wikipedia.org/wiki/Result_type).

In software development, error handling defines how a system represents, propagates, recovers from, and explains failure. Use exceptions for truly exceptional or boundary-crossing failures when they fit the host language, and use result types or explicit return values when failure is expected, recoverable, or part of normal control flow. Good error handling preserves useful context, avoids swallowing failures, separates user-facing messages from diagnostic detail, keeps secrets out of logs, and makes retry, fallback, abort, and cleanup behavior explicit.

In agentic programming, clear error handling gives agents observable failure paths to test instead of vague crashes or silent no-ops. Typed results, named error cases, structured logs, and focused failing tests help an agent distinguish bad input, missing configuration, unavailable tools, network failure, permission failure, and programming bugs. When agents add error handling, they should also add or update tests for the failure path so the behavior can be verified without relying on hope.

## Related Patterns

1. [Validation boundaries](validation-boundary.md) prevent invalid external data from becoming unclear internal failures.
2. [State machines](state-machines.md) can model recoverable failure states, retry transitions, and terminal error states.
3. [Event streams](event-streams.md) can record failure events for audit, replay, retry, and diagnosis.
4. [Stigmergy](stigmergy.md) benefits when failures leave durable, structured traces that guide the next human or agent action.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
