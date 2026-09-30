# Model Routing Workflow

Use this to learn project users' routing preferences gradually during normal work. Preserve useful feedback about subagents, supervisors, and reviewers without turning routing into a setup interview or trying to fill every cell.

## Start From What Is Known

Read the [model catalog, profiles, and routes](../rules/model-routing.md), relevant [personas](../personas/README.md), and existing user preferences. Check which models, effort settings, tools, and delegation controls the current client actually exposes. Reuse recorded answers; do not interview the user again before routine work.

When assigning work, follow the [shared-file coordination rules](task-execution.md#coordinating-shared-files): separate file sets by default, queue overlapping edits, and keep waits bounded.

Default to quiet learning: use existing preferences, task outcomes, and feedback the user volunteers. A new project, task category, or stale entry does not automatically require a routing conversation. Leave nonblocking unknowns unresolved and keep working.

Ask an occasional short question only when the answer materially affects the current work and cannot reasonably be inferred. Usually ask one question, then learn more over time. Do not repeatedly ask for ratings, revisit unanswered optional questions, solicit feedback after every task, or remind the user about routine routing maintenance.

Rarely, when relevant to feedback the user is already discussing, mention that their impressions of a model on a task can help keep the subagent routing map tidy. Keep that suggestion brief; do not make it a recurring prompt or sign-off.

## Optional Question Reference

This is a reference for choosing a useful question, not a questionnaire to present to the user. Most tasks need none of these questions.

| Topic | Useful question | What to preserve |
| --- | --- | --- |
| Work categories | Would you like this kind of work to have its own route? | The user's task categories and scope; avoid a fixed universal taxonomy. |
| Preferences and reserved work | Is there a model or provider you prefer for this task? | Explicit choices, provider constraints, and uncertain hypotheses. A preference does not need benchmark proof. |
| Model and effort | Which model and effort would you prefer here? | Exact selectable model, effort, tools, and a short profile name. Leave an unknown effort unresolved. |
| Review and supervision | Do you have a preferred reviewer for this work? | Separate worker, supervisor, and reviewer choices; roles can use different models or providers. |
| Tradeoffs and escalation | Which matters most for this task: quality, time, or cost? | An acceptable result, practical limits, escalation triggers, and permitted alternatives. |
| Uncertainty and evidence | Would a small comparison help resolve this routing choice? | Candidate profiles, representative task, success criteria, available usage data, and who judges the result. Comparison is optional. |

A user can answer several topics in one sentence. Preserve the distinctions they supply rather than translating everything into a single low/medium/high model tier. Effort labels are not equivalent across providers.

## Learn, Record, And Apply

1. Record clear user preferences and volunteered feedback in [model routing](../rules/model-routing.md), including task, model, and effort when known. Add small observations as work provides evidence; a successful run does not establish a new user preference. Keep unknown fields unresolved. Separate required choices, preferences, hypotheses, and observed results; do not silently turn tentative examples into project defaults. Mention updates briefly when useful rather than requesting routine confirmation.
2. Verify that the chosen client can express the configuration. If it cannot, use a recorded alternative where applicable or ask one focused question when the choice blocks the work. Continue independent work.
3. Apply specific user routes before generic tier heuristics. Use a configured alternative or report the limitation when a requested profile is unavailable. Keep explicit preferences until the user changes them; a stale date does not cancel them.
4. If a comparison is useful, use the evidence guidance in the routing document. When the user requests a task benchmark, execute the small benchmark below and return a provisional ranking backed by actual results.
5. During active project work, refresh available models and the [published pricing cache](../rules/model-pricing-cache.md), and have a high-tier agent review existing routes and recent feedback when the 30-day review is due. Also refresh relevant published prices on request. Do this quietly using available evidence and official pricing sources. A due review is not a reason to send a reminder or ask the user to rerate models. Update evidence and pricing dates only after an actual check.

## Small Task Benchmark On Request

When asked to benchmark or self-rank models for a task, run a bounded comparison using the available delegation or model-execution tools. Use the requested profiles and limits. If these are unspecified, start with two available model-plus-effort profiles, one representative task, and one attempt each; state the scope and practical time or usage limits before running. Ask only for missing choices that materially affect execution.

1. Define the task, starting inputs, acceptance checks, and ranking priorities before candidates run. Use the user's quality, cost, and speed priorities; otherwise put acceptable correctness first and report cost/time separately. Keep the exercise small enough to inform one routing decision.
2. Verify the selectable model IDs, effort settings, tools, and access. Execute each candidate through an actual supported subagent, client, or provider interface. Record the configuration used. If a candidate cannot be run, mark it unavailable; one model imagining another's response is not a comparison.
3. Give each candidate the same task, instructions, fixtures, starting revision, and limits in isolated scratch copies or contexts. File-editing benchmarks require separate scratch copies or worktrees; context isolation alone does not isolate shared files. Keep other candidates' answers hidden until their attempts are complete. Record material tool differences rather than attributing them to model quality.
4. Request the candidate's result, verification evidence, and brief self-assessment against the rubric. Capture observed duration, retries, and reported usage where available. Self-assessment helps explain the attempt; it does not establish its score or rank.
5. Have the supervising agent run the acceptance checks and review each result against the same rubric. Use a separate reviewer profile when useful and available; conceal candidate identity during review when practical. For visual work, inspect the rendered result. For review tasks, check confirmed findings, missed issues, and false positives. Mark any unavoidable self-review or observation gap.
6. Return a provisional task-specific ranking with this report shape. Rank only profiles that meet the acceptance bar as viable choices; report failures, ties, missing measurements, and low confidence explicitly. A single attempt is a smoke benchmark, not a durable capability rating.

| Rank or status | Actual model and effort | Outcome and evidence | Time and rework | Usage or cost |
| --- | --- | --- | --- | --- |

Include supervisor/reviewer overhead and retries in total usage and cost. Follow the [evidence guidance](../rules/model-routing.md#gather-evidence-occasionally) for missing metrics and cost estimates. Repeat only close or inconsistent comparisons when it would affect the decision and fits the requested limits.

Keep the prompt, rubric, configurations, outputs, checks, and report in ignored `_code_review/model-routing/` notes. Record any safe routing evidence as task-specific and dated; keep the user's preferred route separate. Benchmark results do not automatically replace explicit user preferences. Apply the 30-day freshness convention when reusing the ranking.

The template's profile, route, and benchmark-result tables remain empty. Use this conversation and benchmark workflow within the session's available tools and delegation controls.
