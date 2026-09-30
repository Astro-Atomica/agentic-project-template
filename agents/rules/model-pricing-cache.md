# Published Model Pricing Cache

Keep dated public token prices here to support [model routing](model-routing.md). During active project work, refresh relevant models from official provider pricing pages when the monthly review is due, or when the user requests it. Reuse fresh cached prices during ordinary routing; avoid repeated lookups, questions, or reminders.

## Cached Prices

Rates are **USD per million tokens**, for direct-provider APIs with standard global processing. OpenAI base rates apply to input ≤272K; longer requests use the adjustments below. Current model IDs are in the [routing catalog](model-routing.md#model-catalog); previous model IDs are documented in the linked specs below.

Context values use **API / DESK / CLI** order. `?` means unverified; `*` marks cached client metadata rather than an active-session limit. Combine DESK and CLI into one value only after verifying they agree; keep three values when they differ or either remains unknown.

### Current Generation

| Model | API effort settings | Context (API / DESK / CLI) | Input | Cache read / write | Output |
| --- | --- | --- | --- | --- | --- |
| GPT-6.1 Sol | low, medium, high, xhigh, max | 1.05M / 272K* / ? | $2.00 | $0.10 / $2.50 | $10.00 |
| GPT-6 Astra | low, medium, high, xhigh, max | 1.05M / 272K* / ? | $10.00 | $1.00 / $12.50 | $50.00 |
| GPT-6 Sol | none, low, medium, high, xhigh, max | 1.05M / 272K* / ? | $2.00 | $0.20 / $2.50 | $10.00 |
| GPT-6 Luna | none, low, medium, high, xhigh, max | 1.05M / 272K* / ? | $0.10 | $0.01 / $0.125 | $0.50 |
| Claude Fable 5.1 | low, medium, high, xhigh, max | 1M / ? / ? | $10.00 | $0.25 / $12.50 (5m), $20.00 (1h) | $50.00 |
| Claude Opus 5.5 | low, medium, high, xhigh, max | 1M / ? / ? | $4.00 | $0.20 / $5.00 (5m), $8.00 (1h) | $20.00 |
| Claude Sonnet 5.5 | low, medium, high, xhigh, max | 1M / ? / ? | $2.00 | $0.20 / $2.50 (5m), $4.00 (1h) | $10.00 |
| Claude Haiku 4.5 | No named effort tiers; thinking budget | 200K / ? / ? | $1.00 | $0.10 / $1.25 (5m), $2.00 (1h) | $5.00 |

### Last Generation

Retain selected preceding releases for cost comparisons and existing project routes. These are their currently published prices, rather than historical launch prices. Haiku 4.5 remains in the current table as the latest Haiku release.

| Model | API effort settings | Context (API / DESK / CLI) | Input | Cache read / write | Output |
| --- | --- | --- | --- | --- | --- |
| GPT-5.6 Sol | none, low, medium, high, xhigh, max | 1.05M / 272K* / ? | $4.00 | $0.40 / $5.00 | $20.00 |
| GPT-5.6 Terra | none, low, medium, high, xhigh, max | 1.05M / 272K* / ? | $2.00 | $0.20 / $2.50 | $12.00 |
| GPT-5.6 Luna | none, low, medium, high, xhigh, max | 1.05M / 272K* / ? | $0.20 | $0.02 / $0.25 | $1.20 |
| Claude Fable 5 | low, medium, high, xhigh, max | 1M / ? / ? | $10.00 | $1.00 / $12.50 (5m), $20.00 (1h) | $50.00 |
| Claude Opus 5 | low, medium, high, xhigh, max | 1M / ? / ? | $5.00 | $0.50 / $6.25 (5m), $10.00 (1h) | $25.00 |
| Claude Sonnet 5 | low, medium, high, xhigh, max | 1M / ? / ? | $2.00 | $0.20 / $2.50 (5m), $4.00 (1h) | $10.00 |

**Last checked: 2026-09-29 (America/Los_Angeles).** Treat these facts as stale after 30 days.

Sources: [OpenAI pricing][openai-pricing]; model specs for [Sol 6.1][sol-6-1], [Astra][astra], [Sol 6][sol-6], and [Luna][luna]; Anthropic [pricing][anthropic-pricing], [model specs][anthropic-models], and [effort controls][anthropic-effort].

Previous-generation specs: GPT-5.6 [Sol][sol-5-6], [Terra][terra-5-6], and [Luna][luna-5-6]; Claude [Fable 5][fable-5], [Opus 5][opus-5], and [Sonnet 5][sonnet-5].

Client context evidence: the starred DESK values were observed in local Codex model metadata during this template review on 2026-09-29. They are provisional observations, not universal desktop limits. CLI limits and Claude desktop limits remain unverified. Record the exact client, version, configuration, source, and check date below the tables when verifying or replacing a value; keep account-specific details private. Codex supports configurable [context and compaction limits][codex-context-config].

Effort settings describe published API controls, not project rankings or recommended routes. Agent clients may expose a different set, including client-specific levels such as `ultra`; record the actual controls in agent profiles. API context windows include input and output; client working budgets and compaction thresholds can be smaller and should be labeled separately. The 272K pricing boundary is not a model's total context capacity. Haiku uses an extended-thinking token budget rather than named effort tiers.

## Published Pricing Conditions

- For the listed OpenAI models, input >272K doubles input and cache rates and multiplies output rates by 1.5 for the full request. Fast rates are 2x Standard; Batch and Flex are 50% lower. Astra Ultrafast is 6x Standard. Regional processing and FedRAMP endpoints add 10%. Apply the context adjustment before processing modifiers. See [OpenAI pricing][openai-pricing] for availability and details.
- GPT-5.6 Sol's listed promotional prices are published as available at least through 2026-11-21. Recheck this condition during a refresh rather than assuming the promotion continues.
- Anthropic cache writes have separate 5-minute and 1-hour rates as shown. Its 4.6-and-later models have no long-context premium within their supported window. Batch token rates are 50% lower; US-only inference on supported models adds 10%. Opus 5.5 Fast uses $8 input and $40 output; Opus 5 Fast uses $10 input and $50 output per million tokens before cache and geography modifiers. See [Anthropic pricing][anthropic-pricing] for combinations and availability.
- Tool charges, taxes, private discounts, and subscription-credit rates are outside these base API rows. Match estimates to the actual interface and published billing mode.

## Refresh And Use

Record conditions that affect the rate, including service mode, batch discounts, context-length thresholds, regional pricing, and cache duration. Use `not published` or `not applicable` for missing categories rather than assuming a zero rate. Keep tool fees or other charges distinct from token rates when they affect an estimate.

Update the check date only after successfully verifying the published rates, context limits, and effort controls. If only some rows are refreshed, record their check dates below the table. If a refresh fails, retain the last verified values and their original dates, and label estimates that rely on stale data; do not invent prices or silently treat them as current.

When a model is superseded, move its row to the last-generation table and retain its source links. Refresh both generations when relevant to project routes; a retained price does not establish continued model availability.

Use matching cached rates with reported task usage for labeled cost estimates, including supervision, review, and retries. Published API prices do not establish subscription-credit charges or prove that a model uses fewer tokens. Price changes inform routing tradeoffs while explicit user preferences remain in force.

Keep this shared cache limited to public pricing facts and source links. Private billing records, negotiated rates, account details, and raw task evidence belong in ignored local files. This cache is maintained during work or on request; it does not schedule a background job.

[openai-pricing]: https://developers.openai.com/api/docs/pricing
[anthropic-pricing]: https://platform.claude.com/docs/en/about-claude/pricing
[sol-6-1]: https://developers.openai.com/api/docs/models/gpt-6.1-sol
[astra]: https://developers.openai.com/api/docs/models/gpt-6-astra
[sol-6]: https://developers.openai.com/api/docs/models/gpt-6-sol
[luna]: https://developers.openai.com/api/docs/models/gpt-6-luna
[anthropic-models]: https://platform.claude.com/docs/en/models/overview
[anthropic-effort]: https://platform.claude.com/docs/en/build-with-claude/effort
[sol-5-6]: https://developers.openai.com/api/docs/models/gpt-5.6-sol
[terra-5-6]: https://developers.openai.com/api/docs/models/gpt-5.6-terra
[luna-5-6]: https://developers.openai.com/api/docs/models/gpt-5.6-luna
[fable-5]: https://platform.claude.com/docs/en/models/fable-5/overview
[opus-5]: https://platform.claude.com/docs/en/models/opus-5/overview
[sonnet-5]: https://platform.claude.com/docs/en/models/sonnet-5/overview
[codex-context-config]: https://learn.chatgpt.com/docs/config-file/config-reference
