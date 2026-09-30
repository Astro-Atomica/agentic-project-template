# Task Execution Workflow

Use the user's requested outcome and existing project decisions to guide the work.

1. Run the relevant verification, fix issues caused by the change, and inspect visual or interactive results when applicable. Repeat checks when new evidence warrants it.
2. Update durable project decisions when the task changes them. Use the [privacy gates](../rules/privacy-and-publication.md) if committing or publishing is part of the request.
3. Finish all requested work that can proceed, then summarize the result, verification, and any concrete blocker. Continue independent work while a clarification is pending.

## Subagents And Model Selection

- Use subagents when it makes sense. Honor the user's task-specific routes and preferred profiles, including model, effort, provider, and reviewer choices. Where no route is defined, scope each worker to its task and choose approximately one tier above the estimated minimum needed. Use a higher-tier agent to supervise multiple workers, review their results, and integrate the work. Respect the session's available models and delegation controls.
- Use the [model routing workflow](model-routing.md) to learn gradually from work and volunteered feedback. Reuse established answers, ask only occasional questions that affect the task, and avoid repeated feedback requests or reminders. During active work, quietly refresh the model list and [published pricing cache](../rules/model-pricing-cache.md) and have a high-tier agent review routes and feedback when the 30-day review is due. Published prices may also be refreshed on request.
- The template may prelist model identities from dated vendor catalogs, but leaves profiles, routing decisions, and ratings unset. Let project users save separate profiles for implementation, code review, UX review, and other work. Use occasional comparisons and ordinary task outcomes to record quality, total usage or cost, latency, and rework. Keep judgments brief, dated, and marked stale after 30 days; preserve user preferences while distinguishing them from measured results.
- When asked to benchmark or self-rank models for a task, execute the [small task benchmark](model-routing.md#small-task-benchmark-on-request). Compare actual model-plus-effort profiles, verify their outputs, and report a provisional task-specific ranking with the available time and usage evidence.

## Coordinating Shared Files

- Assign subagents separate file sets where practical. Queue edits to a file already being edited, with the supervisor tracking the current editor, waiting task, and when the wait began. Continue independent work while queued.
- Keep queue waits bounded: default to three minutes unless the project or user sets another limit. Measure from when the task first queued; checking progress does not restart the timer. After that limit, proceed with the needed edit rather than waiting indefinitely.
- Overlapping edits are an exception that can help resolve a blocker, including before the queue limit when useful. Notify the supervisor and other editor of the intended changes without waiting indefinitely for acknowledgment. Prefer separate regions, refresh the file contents before applying patches, and avoid overwriting another agent's changes.
- Have the supervisor reconcile overlapping changes, inspect the combined diff, and run the relevant verification before accepting the integrated result.

For reviews, use [code-review.md](code-review.md). New infrastructure or broader cleanup requires a need within the task's scope.
