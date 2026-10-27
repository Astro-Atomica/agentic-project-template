# Post-Prototype Test Sitemap

Immediately after the initial web app/page prototype, provide a browser-accessible
**Test sitemap** (for example `/test-sitemap`). Link it from development/preview
navigation and include its URL in the prototype handoff. Maintain it as page types
and states change, including for single-page apps.

## Coverage

- Link to a representative instance of every page type, including ordinary pages,
  alternate layouts, authentication, forms, confirmations, policy/contact pages,
  and all applicable error/recovery states.
- Include inspectable loading, empty, validation, success, and failure states
  where they materially change the experience. Use deterministic fixtures or
  preview routes for states that cannot reliably be reached through navigation.
- Reuse actual page/component implementations. Existing stories or fixtures can
  be link targets; a separate duplicate implementation is insufficient.
- Label each entry with its page/state, working inspection link, required test
  role/fixture, and expected HTTP code or client-only/no-response status. Clearly
  distinguish simulated error previews (often served with 200) from real errors.
- Keep planned but unimplemented types visible as pending, without fake links.
  Every implemented type and applicable state needs a working inspection path
  before handoff; disclose unresolved coverage gaps.
- Include access to metadata/share-card and favicon/app-icon inspection. Reuse
  existing tools or simple fixtures for these checks; a custom diagnostic dashboard
  is not required. See [metadata](page-metadata.md) and [icons](site-icons.md).

One representative record per type is enough for this navigation page. It need
not enumerate every database record or every combination of state and viewport.

## Access And Verification

Keep the test sitemap and fixtures in development/staging by default. Protect
production-retained test surfaces with access controls; search exclusions alone
are insufficient. Use synthetic data and supported test roles without bypassing
real authorization. Inspection links must not send real messages, make purchases,
change real records, or disrupt a service.

This human review page is separate from the [public XML sitemap](page-metadata.md#generate-and-maintain-the-public-sitemap).
Exclude test previews from that public inventory.

Compare the page with the route/type inventory, follow every inspection link,
and verify direct navigation/refresh and the intended state. Then apply the
[web readiness checks](../workflows/web-readiness.md) for affected behavior:
responsive task usefulness, loading, forms/recovery, consent, metadata/icons, and
contact destinations. Static fixtures do not establish real request handling,
loading performance, event delivery, or production behavior. Use focused tests
at the responsible layer and report unverified coverage explicitly.
