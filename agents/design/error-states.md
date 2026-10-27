# Error Pages, Forms, And Recovery States

Use the site's [design language](../DESIGN.md) for applicable failures, reusing a
shared presentation with situation-specific copy and actions. A custom 404 alone
is insufficient. Select states the actual features/hosting can encounter; record
meaningful exclusions or provider limits. This is not a requirement for a separate
full page or new endpoint for every code.

## Coverage

| Page or state | HTTP response | When applicable and useful recovery |
| --- | --- | --- |
| Page not found | **404 Not Found** | Public websites: link home or to a relevant section; search when available |
| Permanently removed content | **410 Gone** | Deliberately retired content with no replacement: explain removal and offer alternatives; redirect moved content to its actual replacement instead |
| Sign-in required or session expired | **401 Unauthorized** for rejected authentication | Authenticated features: sign in again, preserving a safe return destination and recoverable work |
| Access denied | **403 Forbidden**, or **404 Not Found** when existence must remain private | Restricted content/actions: explain the available next step without disclosing protected information |
| Malformed request | **400 Bad Request** | Invalid request structure: explain what can be corrected |
| Invalid submitted values | **422 Unprocessable Content**, or **400 Bad Request** under the endpoint's validation contract | Identify the fields to correct |
| Expired action link | **410 Gone** for a retired resource; **400 Bad Request** for an invalid action token; **404 Not Found** when unknown or intentionally concealed | Provide a way to obtain a fresh link; choose the response according to resource semantics and disclosure policy |
| Conflicting change | **409 Conflict** | Concurrent edits or state conflicts: let the user review current state and reconcile safely |
| Upload too large | **413 Content Too Large** | Uploads: show the actual permitted limit and let the user select a smaller file |
| Too many requests | **429 Too Many Requests** | Rate-limited interactions: ask the user to wait and respect a supplied retry interval |
| Unexpected server failure | **500 Internal Server Error** | Dynamic services: offer safe retry, navigation, or an existing support route |
| Upstream failure | **502 Bad Gateway** | Proxies receiving an invalid upstream response: explain temporary failure and provide a safe next step |
| Service unavailable or maintenance | **503 Service Unavailable** | Temporary outages: show timing or a status link only when known and maintained |
| Upstream timeout | **504 Gateway Timeout** | Proxies waiting too long for an upstream: explain the timeout and provide a safe next step |
| Client application crash | **No intrinsic HTTP status** | Client applications: show a recoverable error view without claiming the server returned 500 |
| Connection failure or offline state | **No HTTP response received** | Network-dependent interactions: preserve usable content and work; offer retry when connectivity returns |


Use valid HTTP semantics and preserve established API contracts rather than
changing codes to match an example. A page may return 200 while its API request
fails; check the relevant request. Keep API errors in their documented format.
A 401 response needs the appropriate `WWW-Authenticate` header; a browser sign-in
flow may instead redirect to a sign-in page that itself returns 200. Client-side
validation/crashes and offline states do not inherently produce HTTP errors.
References: [status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status),
[HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html).

## Presentation And Recovery

- Explain the problem in plain language and offer a working next action; codes
  are supporting detail. Do not expose secrets, stack traces, or private paths.
- Use a full page when navigation/the app fails and an inline/section error for
  a local failure so other content remains usable. Failed loading is not empty data.
- Preserve recoverable input without retaining secrets unnecessarily. Prevent
  duplicate submissions while pending. If a mutation's outcome is uncertain,
  establish the outcome or use verified duplicate prevention before retrying.
- Support keyboard use, visible focus, readable contrast, small screens, and the
  site's themes. Associate/announce dynamic errors and manage focus appropriately.
- Where supported, provide a minimal themed host/proxy outage document that can
  render without the failed application/API and its unavailable assets.

## Validate Forms And Explain Errors Clearly

Data/input forms must validate values and report friendly errors and states.
Explain required fields, formats, and limits; validate relevant types, ranges,
lengths, and cross-field rules. Give timely feedback without marking untouched
fields invalid before users can complete them. Validate again at the trusted
processing boundary; browser checks alone do not protect server operations.

Say what needs correction and how, for example "Enter an email address like
name@example.com". Put field errors beside inputs, associate them for assistive
technology, use more than color, and clear/update resolved errors. Use a summary
or form-level message when useful. Distinguish invalid input from server/network
failures and show submitting, confirmed success, and failure states. Apply the
recovery rules above so failed submission does not discard work or repeat an
operation with an unknown outcome.

## Thank-You Pages For Submissions And Purchases

Provide themed thank-you/confirmation pages after successful form submissions
and purchases, with accessible details and a useful onward action.

- **Forms:** acknowledge receipt and explain next steps. State reference numbers
  or response timeframes only when supplied/supported by the actual service.
- **Purchases:** show verified order/payment state, relevant summary/reference,
  and delivery, access, download, or tracking steps. Mention receipts/emails only
  when that workflow exists.

Base success on the responsible service's verified result, not merely a redirect
or URL parameter. Represent pending, failed, canceled, and unknown outcomes
truthfully. Refresh/back/revisit must not repeat the operation. Direct visits
without context must not fabricate success or expose another user's details.
Keep private confirmation data out of public metadata and sitemaps.

## Verification

Expose applicable states through the [test sitemap](test-sitemap.md), labeling
simulated previews separately from actual HTTP responses. Use isolated data and
services for forms/purchases; no real transactions just to exercise a preview.

Check unknown nested URLs by direct navigation and refresh, actual server/proxy
status/headers, outage rendering with dependencies unavailable, and working
recovery actions. Exercise valid/invalid/corrected form input, input preservation,
accessible feedback, success/failure/pending outcomes, and safe confirmation
revisits. Inspect representative desktop/mobile states. Record local versus
host/deployed evidence; fixture rendering alone does not prove error handling.
