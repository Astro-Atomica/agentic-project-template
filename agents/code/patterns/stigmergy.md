# Stigmergy Rules

Use this file for stigmergy-specific rules about indirect coordination through shared traces, artifacts, environment state, queues, logs, markers, or other observable work surfaces.

Reference: [Stigmergy](https://en.wikipedia.org/wiki/Stigmergy).

In software development, stigmergy describes coordination where later work is guided by durable traces left by earlier work instead of direct conversation alone. Examples include failing tests that point to the next fix, issue labels that expose project state, migrations that encode schema history, review notes that preserve unresolved risks, logs that reveal runtime behavior, queues that expose pending work, and generated artifacts that make progress visible. Use stigmergic traces when they make collaboration easier to resume, audit, test, or hand off; keep those traces structured, current, and intentionally placed so they guide action instead of becoming stale noise.

In agentic programming, stigmergy is one of the main ways agents stay useful across long tasks, context compaction, restarts, and new threads. Agents should leave small, durable, observable traces in the right project surfaces: tests that describe expected behavior, `_private/` notes that preserve user intent, `_code_review/` notes that preserve deferred risks, process logs that show which local services were started, and design or validation artifacts that make UX decisions inspectable. Good traces let the next agent or human continue from evidence instead of reconstructing hidden reasoning from chat history.

## Related Patterns

1. [Event streams](event-streams.md) make stigmergic traces temporal: the system records ordered events so later consumers can react, replay, audit, or resume from observable history.
2. [Functional reactive programming](functional-reactive-programming.md) makes stigmergic traces reactive: shared state and derived signals guide later behavior through deterministic data flow.
3. [State machines](state-machines.md) make stigmergic traces explicit: visible states, transitions, and guards tell the next actor what can happen next.
4. [Object-oriented design](object-oriented.md) and [mixins](mixins.md) can package stigmergic behavior behind stable interfaces, so traces are written, read, and cleaned up through reusable boundaries instead of scattered ad hoc code.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
