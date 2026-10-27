# Analytics Planning, Installation, And Verification

For websites and apps, raise an analytics checkpoint once the initial prototype
has a meaningful user flow and revisit unresolved setup before launch. Remind
the developer to install/configure the selected analytics tool, instrument useful
events, and verify delivery. An SDK dependency or script tag alone does not
establish working analytics.

## Ask What Matters

Inspect existing analytics, product goals, and recorded tracking decisions first.
Reuse established priorities without repeating the question. When priorities are
missing, present a brief plan tailored to the product, then ask:

> Are there particular actions, outcomes, or user journeys you want to track?
> I'd start with visits, the main task or conversion funnel, and failures. Useful
> additions could include time to first value, feature adoption, returning usage,
> or where people get stuck. Which would help you make decisions?

Suggest a few relevant options from the list below, not every possible metric.
Ask about the provider/project only if it is unresolved; reuse existing choices.
Record the plan and user preferences in project docs. If the answer is pending,
continue independent work and keep the proposed scope visible. Respect a recorded
decision to defer or omit analytics; retain deferred setup in the existing backlog
or `_private/feature-requests.md` and do not repeatedly ask unchanged questions.

## Quick Instrumentation Plan

1. **Define the outcome:** identify the main user task or business goal and the
   questions analytics should answer. For each proposed event, record its name,
   exact trigger, allowed properties, environment, and decision it supports.
2. **Install and configure:** use the chosen provider and project, configure the
   appropriate client/server integration and existing consent/opt-out behavior,
   and separate development/staging traffic from production reporting. Keep
   secret credentials server-side and out of source control.
3. **Instrument the core flow:** track page/screen views and meaningful entry,
   start, completion, and failure points. For sales, this might be offer viewed,
   CTA clicked, checkout started, and purchase confirmed. For an app, it might be
   task started, useful result produced, and saved/exported. For forms, capture
   meaningful form start, validation failure categories, and confirmed submission.
4. **Configure a small report in the chosen tool:** show traffic, core task/conversion
   completion, and failure rates; a custom dashboard is not required. Define each
   denominator, counting window, and identity scope;
   sessions, browser identifiers, accounts, and people are not interchangeable.
5. **Verify end to end:** exercise the flow in an isolated test environment and
   inspect received events in the provider. Confirm names/properties, timestamps,
   duplicate prevention, consent behavior, and report calculations. Record what
   is installed, instrumented, locally tested, and verified in the target environment.

## Interesting Options To Suggest

| Product question | Possible instrumentation |
| --- | --- |
| How quickly do people get value? | Time from meaningful start to first useful result, plus completion rate |
| Where does the main journey stall? | Funnel steps, validation/error categories, and step-to-step completion; infer drop-off over a defined window |
| Which features earn repeat use? | Feature adoption and repeat use by an explicitly defined cohort/identity model |
| Does the mobile experience work? | Completion and failure by coarse viewport/device categories and performance bands |
| What are people struggling to find? | Search usage, zero-result counts, filter use, and subsequent successful navigation |
| Which calls to action help? | Actual CTA impressions and clicks by placement, including sticky versus in-content, followed by confirmed outcomes |
| Does content lead somewhere useful? | Key section visibility, downloads, or relevant outbound actions tied to the page's purpose |

Choose events that answer a question. A button click is not a completed task,
and a thank-you-page view is not sufficient proof of a purchase. Record confirmed
outcomes from the authoritative operation and deduplicate retries/revisits.
Do not claim measured abandonment from a missing completion without defining the
window and accounting for incomplete sessions or blocked telemetry.

## Data Boundaries And Maintenance

Allowlist properties. Exclude raw form values, free-text searches, credentials,
private document content, sensitive URLs/query strings, and unnecessary personal
data. Prefer route templates, action identifiers, error categories, and coarse
dimensions. Do not automatically enable session replay, screenshots, or broad
autocapture as part of a basic install; scope those separately if requested.
Follow the [privacy/cookie guidance](../design/policy-pages.md) and update notices
to match the actual implementation. Do not let analytics block the primary UI or
break a task when the provider is unavailable.

Verify initial and client-side navigation without double-counting, repeat clicks,
failed operations, and rejection/withdrawal of tracking where applicable. Keep
test data out of production metrics and never create real purchases or messages
merely to test events. Before an authorized launch, flag missing instrumentation
or unverified delivery; absent data is not zero usage. Update event definitions
and reports when flows change, and retire events that no longer support decisions.
