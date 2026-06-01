# Typed Errors / Cause Trees Rules

Use this file for typed-error- and cause-tree-specific rules about expected failures, defects, interruption causes, parallel failures, sequential failures, and preserving failure provenance.

Reference: [Effect Cause](https://effect-ts.github.io/effect/effect/Cause.ts.html).

In software development, typed errors make expected failure cases explicit, while cause trees preserve the full story of how work failed. Use this pattern when failures can come from validation, IO, permissions, network calls, subprocesses, retries, parallel branches, defects, or cancellation. Good cause modeling keeps user-facing messages separate from diagnostic detail, preserves original causes, and avoids flattening distinct failures into vague strings.

In agentic programming, typed errors and cause trees help agents distinguish bad input, unavailable tools, permission problems, flaky services, defects, and user cancellations. A structured failure value gives the next agent evidence to inspect instead of a chat fragment or stack trace guess. When agents add a new failure path, they should add tests or examples that show the typed error and the preserved cause.

## Related Patterns

1. [Error handling / result types](error-handling-result-types.md) define how typed failures are returned, propagated, logged, and recovered.
2. [Interruption / cancellation](interruption-cancellation.md) should preserve cancellation as a distinct cause, not disguise it as ordinary failure.
3. [Fibers / structured concurrency](fibers-structured-concurrency.md) need cause trees when parallel child work can fail in several ways.
4. [Tracing / spans](tracing-spans.md) connect causes to timing, parent work, and diagnostic context.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
