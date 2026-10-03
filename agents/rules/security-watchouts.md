# Security watchouts

Updated October 3, 2026 · Build 1

Use this guidance when creating or reviewing networked features, handling untrusted
input, packaging public assets, or changing deployment. Apply relevant checks to
the actual stack; record non-applicable areas instead of adding unnecessary
infrastructure. This complements [publication privacy checks](privacy-and-publication.md),
which do not establish application security or server configuration.

## Transport and executable content

- Verify every supported HTTP hostname redirects to its intended HTTPS host before
  serving pages, scripts or APIs. Use fixed/allowlisted destination hosts; do not
  reflect an untrusted Host or forwarded header into redirects.
- Verify HSTS on HTTPS responses, including error paths where practical. Decide
  max-age, subdomain scope and preload deliberately; do not opt unrelated hosts
  into a long-lived policy. Redirects alone do not authenticate a first HTTP visit.
- Browser scripts can be replaced on an unauthenticated HTTP connection even when
  the application has no XSS bug. Test actual script URLs as well as the homepage.
- Inventory executable dependencies, dynamic imports and workers. Pin dependencies
  and inspect package advisories. Self-hosting and a clean dependency scan do not
  prove a script safe. Add and test CSP against real provider/worker/embed needs;
  report-only rollout can reveal compatibility problems. CSP is defense in depth,
  not a substitute for escaping or HTTPS.

## Inputs, injection and destinations

- Trace URL/query/body/header/storage/provider data to DOM, SQL, filesystem,
  template, process and redirect sinks. Prefer textContent/text nodes for text,
  parameterized SQL for values and fixed allowlists for identifiers or commands.
- Avoid input-fed eval, Function, shell command construction, dynamic includes,
  unsafe deserialization and arbitrary object merges. Check prototype-related keys
  if merging untrusted objects. TypeScript types are not runtime validation.
- Validate types before regex/string operations. Require whole-value matches;
  test final newline, CRLF, NUL, Unicode, arrays, objects, null and booleans. Some
  regex end anchors accept a trailing newline. Check semantic allowlists/ranges
  after syntax checks. Wrong types should return controlled client errors.
- Bound the bytes actually read, not only Content-Length. Reject excess input
  before JSON parsing or expensive work. Cover chunked/missing-length bodies,
  decompression limits, nesting, collection size, CPU time and provider responses.
- Construct navigation and upstream URLs from fixed origins and encoded values.
  Test protocol-relative URLs, userinfo, encoded separators, backslashes, duplicate
  parameters and traversal. Validate redirects and network destinations after
  parsing; do not allow user-selected internal hosts or filesystem paths.

## Adversarial APIs and stored data

- Assume scripts can spoof browser signals, user agents, country claims and consent
  assertions. Origin/CORS are browser boundaries, not authentication of scripts.
  A valid signed token establishes only the facts it signs, not humanity.
- Define uniqueness, replay and classification policies server-side. A mutable
  category must not let one identity count in several supposedly exclusive tables.
  Enforce invariants transactionally, including concurrent requests, retry paths,
  migrations and enrichment. Test both category orderings and total consistency.
- Bound token issuance as well as token use. Per-token limits can be bypassed by
  minting more tokens. Choose budgets with shared networks and legitimate bursts
  in mind; application limits do not replace host-level flood controls.
- Store rejection metrics separately from successful activity. Never retain raw
  payloads, identifiers or secrets merely to make an error report easier.
- Treat persisted records as untrusted on read. One accepted malformed field can
  break every later dashboard load. A renderer should tolerate invalid legacy
  values without crashing or silently deleting counts. A validation fix does not
  clean existing data: plan a backed-up, idempotent, aggregate-preserving repair
  when evidence shows cleanup is needed.

## Deployment and file exposure

- Inspect the exact artifact manifest, archive members and built output. A public
  source directory copied recursively can carry an accidental secret into a build.
  Use explicit publication allowlists and content scans; .gitignore does not stop
  a deployment command from uploading ignored files.
- Browser HTML/JS/CSS/JSON/images are downloadable by design. Never embed secrets
  in client bundles, configuration or source maps. PHP and other server scripts
  must execute rather than be served as source; verify server behavior separately.
- Keep private databases, keys, deployment tools, archives, backups and notes
  outside the document root with minimum permissions. Deny sensitive filenames
  as defense in depth, including journals and temporary upload/backup suffixes.
- Avoid publicly readable temporary copies of server source during atomic uploads.
  Stage outside webroot on the same filesystem when possible, then rename into
  place. Validate archive paths, file types, symlinks, destination containment and
  exact manifest membership before extraction/replacement.
- Disable directory listings, but remember known filenames can still be requested.
  noindex and robots.txt are not access controls. A 404 for an absent secret file
  does not prove a deny rule works on an existing file. Use harmless canaries only
  within authorized scope and remove them afterward.
- Distinguish selected release files from all files already on a host. A manifest
  audit does not find forgotten old releases, unrelated sites or account backups.

## Repeatable verification

For applicable rows, add regression cases to the project's ordinary test command
and CI. Fail clearly when a required runtime is missing; do not silently skip the
only server-side security tests. Keep bounded fuzzing deterministic and local with
isolated storage and mocked upstreams. Never create fake production visits, flood
live endpoints, or transmit private payloads to third parties to test a parser.

| Surface | Minimum cases and assertions |
| --- | --- |
| HTTP/TLS | Every supported host and representative asset; redirect target, HTTPS HSTS, error response headers |
| Request parser | Boundary size and one byte over, chunked body, malformed JSON, scalar/array/object types, duplicate parameters, newline/control characters |
| Injection | Script/SQL/shell-like values, prototype keys, encoded traversal; no execution, unsafe destination, private-file read or error-detail leak |
| Authentication | Missing/tampered/replayed token, binding mismatch, forged forwarded headers, issuance and use budgets |
| Data integrity | Same identity replay, both category orders, concurrent writes, enrichment, consistent totals and rejection isolation |
| Rendering | Malformed persisted/provider records, invalid locale/country/time values; usable page and safe text output |
| Publication | Exact file manifest, secret scan, no private/source-map/backup artifacts unless intentionally public, outside-root state, temporary-file handling |

Use isolated integration tests for behavior, not source-string assertions alone.
Inspect the real browser when a DOM execution or rendering claim depends on it.
Record source revision, corpus/seed, request count, observations, process cleanup
and limits in ignored _code_review/ notes; never print discovered secrets.

Maintain a concise project security audit with: finding/priority, affected path,
trigger, impact, evidence, mitigation, regression test, local status, deployed
status and remaining uncertainty. Alert the user promptly to credible risks.
Mark findings fixed only at the layer actually verified. Separate hardening gaps
from demonstrated exploits; neither successful tests nor agent review certify a
whole account secure. These instructions do not expand deployment authority.

References: [HSTS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security),
[CSP](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP).
