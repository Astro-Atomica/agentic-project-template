# Project Model Routing

The template prelists contemporary model identities, while leaving routing decisions and ratings unset. Project users can develop task-specific judgments over time from their own experience. Suitability depends on the task, effort setting, tools, context, and constraints; a single global tier does not capture it.

Use the [model routing workflow](../workflows/model-routing.md) to learn gradually from normal work and volunteered feedback, reuse existing answers, and ask only occasional questions that matter to the task. The catalog and tables below support this without requiring a routing interview.

## Model Catalog

**Catalog edition: 2026-10-01. Vendor sources checked: 2026-09-29 (America/Los_Angeles).**

This starting list covers selected general-purpose and agent models from the official [OpenAI][openai-models] and [Anthropic][anthropic-models] catalogs. It is not exhaustive. A vendor listing does not establish access through the project's account, client, region, or delegation tools. Project access dates are intentionally blank; add them only after checking the actual interface. Add other providers or local models when relevant.

| Provider | Model | Vendor model ID | Source | Project access checked |
| --- | --- | --- | --- | --- |
| OpenAI | GPT-6.1 Sol | `gpt-6.1-sol` | [OpenAI][openai-models] | |
| OpenAI | GPT-6 Astra | `gpt-6-astra` | [OpenAI][openai-models] | |
| OpenAI | GPT-6 Sol | `gpt-6-sol` | [OpenAI][openai-models] | |
| OpenAI | GPT-6 Luna | `gpt-6-luna` | [OpenAI][openai-models] | |
| Anthropic | Claude Fable 5.1 | `claude-fable-5-1` | [Anthropic][anthropic-models] | |
| Anthropic | Claude Opus 5.5 | `claude-opus-5-5` | [Anthropic][anthropic-models] | |
| Anthropic | Claude Sonnet 5.5 | `claude-sonnet-5-5` | [Anthropic][anthropic-models] | |
| Anthropic | Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | [Anthropic][anthropic-models] | |

Vendor IDs above use the documented OpenAI/Codex or direct vendor API spelling. Managed services and agent clients may use different aliases. Record the exact selectable ID and supported effort controls when establishing a route.

## Project Routing Decisions

Leave the following tables unpopulated in the template. Users can save several profiles for the same model, then route specific work to them. Small edits and script execution, development and debugging, and rethinking architecture can each have a different effort setting. Code review, UX review, and 3D work can have their own preferred workers and reviewers.

### Agent Profiles

Give each profile a short name users can refer to in conversation. Record the exact model ID, actual client controls, relevant tools, and role or [persona](../personas/README.md). A persona defines responsibilities; a profile defines the model configuration used to carry them out.

| Profile | Provider and model ID | Client and tools | Effort or thinking mode | Role or focus | Basis and evidence | Reviewed | Stale after |
| --- | --- | --- | --- | --- | --- | --- | --- |

Effort labels are model- and client-specific; the same label does not establish equivalent reasoning across providers. Leave an undecided setting marked unresolved until chosen, rather than treating it as maximum effort. Check supported controls before using a profile.

### Task Routes And Preferences

| Task, domain, and scope | Worker profile | Supervisor or reviewer profile | Provider or model preference | Constraints and escalation | Basis and evidence | Reviewed | Stale after |
| --- | --- | --- | --- | --- | --- | --- | --- |

Users may prefer a provider, reserve a particular task for a model, or choose a different reviewer from the implementer. State whether a choice is required, preferred, or experimental. Honor explicit user requirements and use specific task preferences before generic tier heuristics. If a requested configuration is unavailable, report the limitation and use a recorded alternative when applicable; do not silently substitute another provider or effort setting.

Keep each route brief but specific. Useful constraints include tool or modality access, context size, cost or latency budgets, required accuracy, and the consequences of failure. Record when to escalate, such as failed verification, repeated unproductive attempts, or a task exceeding its original scope.

Distinguish user judgment, vendor claims, and observed project results in the evidence field. A user's preference is enough to establish a route without claiming a benchmark win. Preserve uncertain task-fit ideas as hypotheses to compare later, and leave unknown preferences unset.

When users define task-specific tiers, choose a worker approximately one tier above the estimated minimum needed unless an explicit route says otherwise. Prefer a higher-tier supervisor coordinating multiple workers. Use the best available arrangement within the session's model and delegation controls when that hierarchy is unavailable. The catalog itself assigns no tiers or worker/supervisor roles.

## Gather Evidence Occasionally

Use ordinary project outcomes first. During a monthly review, compare only unresolved or costly routes when useful; refreshing the catalog does not require rerunning every task.

When asked, execute the [small task benchmark](../workflows/model-routing.md#small-task-benchmark-on-request) to compare actual candidate profiles and produce an evidence-backed provisional ranking. Candidate self-assessments are inputs to verification, not substitutes for it.

1. Define an acceptable result for a representative task: tests and review for code, inspected rendered results for UX or 3D work, and confirmed findings for reviews. Compare profiles from the same starting revision, prompt, fixtures, and tool access. Keep candidate runs isolated and repeat close or inconsistent results before drawing a firm conclusion.
2. Record the model/version, client, effort, outcome, elapsed time, retries, and correction or review effort. Capture reported input, cache, output, and reasoning usage when available; mark missing data unknown. Include workers, supervisors, reviewers, and retries. Avoid counting reasoning twice when it is already part of billed output.
3. Compare total cost per acceptable completed task, using actual charges or credits when available, or a labeled estimate using the [published pricing cache](model-pricing-cache.md) and matching service mode. Per-token price, token consumption, and subscription credits are different measurements; response length and account-wide quota changes do not establish task usage.
4. Keep raw evidence in ignored `_code_review/model-routing/` notes. Record a brief safe conclusion in the route, including failures and uncertainty. Keep user preferences separate from measured results; one task's outcome is not an overall model ranking.

OpenAI describes GPT-6.1 Sol as offering near-Astra performance at lower cost and recommends comparing them on the same task. That [vendor claim][sol-model] does not establish project-specific task fit or lower token consumption. [Comparison guidance][model-selection] supports using the same inputs and quality bar.

## Maintenance

Check project access before routing. Treat catalog checks and routing judgments as **STALE** once they are 30 days old, even if their status has not been edited. The latest vendor checks become stale on **2026-10-29**; this date does not validate project access or any routing decision.

During active project work, refresh the catalog and review established profiles and routes when the 30-day review is due, using a high-tier agent to review task assignments, observations, and volunteered feedback. Keep routine maintenance quiet; do not repeatedly ask for ratings or send reminders. Update dates only after an actual review. Recheck aliases, availability, supported controls, and retirement notices when changing clients, accounts, or sessions. A stale user preference remains recorded as user intent; its age does not authorize silently replacing it or presenting old evidence as current.

Monthly or on request, check relevant models' published token prices and update the [pricing cache](model-pricing-cache.md). Use fresh cached rates for routine cost comparisons, with source dates and applicable pricing conditions. Refreshing public pricing does not require another routing interview.

Keep private account and deployment details local. This is a maintenance convention, not an automatically scheduled job.

[openai-models]: https://learn.chatgpt.com/docs/models
[anthropic-models]: https://platform.claude.com/docs/en/models/overview
[sol-model]: https://developers.openai.com/api/docs/models/gpt-6.1-sol
[model-selection]: https://developers.openai.com/api/docs/guides/model-selection
