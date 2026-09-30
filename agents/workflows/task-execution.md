# Task Execution Workflow

Use the user's requested outcome and existing project decisions to guide the work.

1. Run the relevant verification, fix issues caused by the change, and inspect visual or interactive results when applicable. Repeat checks when new evidence warrants it.
2. Update durable project decisions when the task changes them. Use the [privacy gates](../rules/privacy-and-publication.md) if committing or publishing is part of the request.
3. Finish all requested work that can proceed, then summarize the result, verification, and any concrete blocker. Continue independent work while a clarification is pending.

## Subagents And Model Selection

- Use subagents when it makes sense. Scope each worker's model to its task and choose approximately one tier above the estimated minimum needed. Use a higher-tier agent to supervise multiple workers, review their results, and integrate the work. Respect the session's available models and delegation controls.
- At least every 30 days, refresh the project's available model list and have a high-tier agent review the rough task assignments in [model routing](../rules/model-routing.md).
- Leave the routing tables empty in the template. Let project users build and revise task-fit estimates over time from their own judgments and project experience. Keep estimates brief, dated, and marked stale after 30 days rather than treating them as lasting capability claims.

For reviews, use [code-review.md](code-review.md). New infrastructure or broader cleanup requires a need within the task's scope.
