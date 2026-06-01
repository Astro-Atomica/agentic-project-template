# Schedules / Retry Policies Rules

Use this file for schedule- and retry-policy-specific rules about recurrence, backoff, jitter, retry limits, polling, repetition, deadlines, and retry observability.

Reference: [Effect Schedule](https://effect-ts.github.io/effect/effect/Schedule.ts.html).

In software development, schedules describe when work repeats, retries, delays, polls, backs off, or stops. Use this pattern when handling flaky networks, rate limits, queues, recurring jobs, polling loops, health checks, exponential backoff, or periodic observation. Good retry policy is bounded, observable, cancellable, testable, and explicit about which failures are retryable.

In agentic programming, schedules help agents avoid ad hoc loops and magic sleep values. A named retry policy or polling schedule lets an agent explain why it waited, how many attempts were made, what baseline timing was used, and when it stopped. Agents should prefer small deterministic schedule tests over guessing that a timing change is harmless.

## Related Patterns

1. [Interruption / cancellation](interruption-cancellation.md) must be able to stop scheduled or retrying work.
2. [Typed errors / cause trees](typed-errors-cause-trees.md) determine which failures should retry, abort, or escalate.
3. [Streams](streams.md) often use schedules for polling, pacing, batching, and backpressure.
4. [Performance is user experience](../../PRINCIPLES.md) because retry timing and polling cadence affect latency, load, energy use, and user trust.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
