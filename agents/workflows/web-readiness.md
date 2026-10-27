# Web Readiness Checklist

Use for websites and web apps, regardless of framework or selected profile.
This is the routing checklist; linked documents own the detailed requirements.
For a focused edit, read and verify affected areas only. Review the full list
after the initial prototype and before release; do not implement the whole list
as a side effect of an unrelated task.

Apply requirements to the product's actual features, supported platforms, and
publication scope. Keep explicit user choices. Record meaningful exclusions,
deferred work, and hosting limitations once in existing project notes; do not
create a new report for every checklist item. Do not introduce authentication,
commerce, installability, a new framework, or a service solely to fill a row.

## Checklist And Canonical Guidance

Numbers preserve the original review list; grouped rows share one requirement.

| Item | Area | Read when implementing or reviewing |
| --- | --- | --- |
| 1 | Themed error/recovery pages with explicit HTTP codes | [Error states](../design/error-states.md) |
| 1a | Required test sitemap immediately after the initial prototype | [Test sitemap](../design/test-sitemap.md) |
| 2 | Primary value above the fold | [Design rule](../DESIGN.md#put-the-pages-primary-value-above-the-fold) |
| 3-4 | Unique page titles/descriptions, social and semantic metadata | [Metadata](../design/page-metadata.md#titles-descriptions-and-semantic-markup) |
| 5 | Unique representative images for public shareable pages | [Share images](../design/page-metadata.md#unique-page-images) |
| 5a | Web app bookmark/home-screen/install icons for supported surfaces | [App icons](../design/site-icons.md#web-app-bookmark-and-home-screen-icons) |
| 6 | Recognizable favicon set; develop from the logo with the user if missing | [Favicon design](../design/site-icons.md#favicon-design) |
| 7 | Maintained robots.txt | [Crawler policy](../design/page-metadata.md#keep-robotstxt-current) |
| 8 | Generated or maintained public sitemap | [Public sitemap](../design/page-metadata.md#generate-and-maintain-the-public-sitemap) |
| 9 | Ask whether image alt text is added now, queued, or skipped | [Choice below](#image-alt-text-choice) |
| 10 | Popular mobile sizes first, then RNG-selected sizes and usefulness ratings | [Responsive review](../design/responsive-design.md) |
| 11 | Sticky sales CTA where useful; task-appropriate actions for other apps | [Scrolling actions](../DESIGN.md#keep-important-actions-accessible-while-scrolling) |
| 12 | Fast useful content, progressive loading, stable layout; measured optimization | [Loading rule](../DESIGN.md#load-quickly-show-progress-keep-layouts-stable) |
| 13 | Input validation and friendly error messages/states | [Forms](../design/error-states.md#validate-forms-and-explain-errors-clearly) |
| 14 | Themed confirmation pages for form submissions and purchases | [Thank-you pages](../design/error-states.md#thank-you-pages-for-submissions-and-purchases) |
| 15-16 | Accurate privacy/cookie notices and applicable consent controls | [Policy pages](../design/policy-pages.md) |
| 17 | Analytics reminder, quick plan, user priorities, installation and verification | [Analytics](analytics.md) |
| 18 | Valid public contacts; fictional details only when explicitly requested | [Contact details](../design/policy-pages.md#publish-valid-contact-details) |

## Image Alt-Text Choice

When first adding/reviewing images, reuse a recorded choice or ask:

> Should I review every image and add appropriate alt text now, queue that work
> for later, or skip the alt-text pass?

- **Add now:** inspect each image in context, implement appropriate alternatives,
  and verify them in the rendered/accessibility result.
- **Queue:** record affected pages/images in the existing backlog, or
  `_private/feature-requests.md` if none exists; retain pending status.
- **Skip:** record the decision and scope without silently queuing the work.

Record the answer once and reuse it. An unanswered question stays unresolved
while independent work continues. Preserve existing valid alt text/control labels
and distinguish queued/skipped work from verified accessibility. This choice
does not change social-image metadata requirements.

When performing the pass, review every image without adding prose indiscriminately: informative
images need context, functional images need their purpose conveyed, and decorative
or redundant images generally use `alt=""`. Complex diagrams may need an adjacent
explanation/data equivalent. Do not use empty alt text to hide unfinished work.
See the [W3C decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/).

## Verification Scope

Use the test sitemap as a review entrypoint, not proof of production behavior.
Combine targeted browser observation with checks at the responsible layer:
HTTP responses, built metadata, provider events, storage, or authoritative state.
Reuse existing fixtures and test commands. Check all page types, then sample
variants according to risk; avoid an exhaustive cross-product of every record,
state, viewport, and device. Retain discovered failures as regression cases.

Keep tests isolated and non-destructive. Existing authorization governs external
validation, real submissions, and deployment. Report local checks, live checks,
and unresolved gaps separately; this checklist does not grant publication authority.
