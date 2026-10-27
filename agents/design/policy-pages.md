# Privacy, Cookies, And Contact Pages

Provide themed, readable privacy-policy and cookie-notice pages. Link them from
persistent footer/app navigation, including before sign-in, and relevant collection
or consent surfaces. Use the [contact rules below](#publish-valid-contact-details)
for operator/support details. These visitor pages are separate from the repo's
`agents/privacy-policy.json`, which only configures publication scanning.

## Match The Actual Product

Inspect forms, accounts, payments, analytics, embeds, hosting logs, cookies,
browser storage, and third-party integrations. Use confirmed business facts and
applicable jurisdictions/audiences; ask for missing facts rather than inventing
them. Unresolved text stays a draft, not a publication-ready policy.

- **Privacy policy:** operator/contact, data collected, purposes, recipients,
  retention or retention criteria, and applicable rights/request procedures,
  legal bases, and international transfers.
- **Cookie notice:** actual cookies and similar technologies, purposes, providers,
  durations, and controls. Include third-party behavior. If none are used, say so
  accurately rather than inventing an inventory.
- **Other policies:** assess terms of use/service and relevant commerce policies
  (shipping, returns/refunds, cancellation, subscriptions). Use the actual product,
  jurisdictions, and confirmed business policies; do not add every possible page.

Update notices, effective dates, and any required communications when substantive
behavior or policy changes. Review affected content during release preparation.

## Cookie Notice And Consent Controls

A notice explains behavior; consent/preferences controls implement choices where
required. Determine the need from actual technologies, purposes, and jurisdictions,
not a blanket assumption that every site needs the same banner.

Where consent is required, gate the relevant storage/tracking before consent and
after rejection/withdrawal. Make acceptance/rejection straightforward and allow
preferences to be revisited. Do not relabel tracking as essential to bypass choice.
Use current official guidance for the applicable jurisdiction, for example the
[UK ICO's privacy/cookie guidance](https://ico.org.uk/for-organisations/advice-for-small-organisations/privacy-notices-and-cookies/cookies-and-privacy-notices-in-detail/);
it does not establish requirements everywhere.

## Verification And Maintenance

Inspect notice links, mobile readability, keyboard access, and availability after
consent rejection. Test network/storage behavior before and after choices, on
reload, and when integrations activate. A functioning button alone does not prove
tracking respects preferences. Include pages and applicable preference states in
the [test sitemap](test-sitemap.md).

Confirm text matches implementation and approved facts; record remaining factual,
integration, or jurisdiction-review gaps. Pages and banners alone do not establish
legal compliance. Report what was actually checked.

## Publish Valid Contact Details

Provide a usable contact route confirmed for the intended operator. Do not invent
or publish lorem ipsum/template/fake phone numbers, email/postal addresses, social
handles, or support destinations unless the user explicitly requests them for
that published surface. Prototype placeholder approval does not authorize release.

Confirm intended public use through the user or an authoritative source with
established ownership; record the evidence. Plausible formatting, a working
domain, or HTTP success alone does not prove ownership. Judge intent by provenance:
a 555 number may be intentional fiction, while an invented 1-800 number may be
an accidental placeholder or someone else's contact. Neither prefix proves validity.

Ask for missing/uncertain public contacts and flag them before publication; never
silently substitute personal details. Check displayed text against actual `tel:`,
`mailto:`, form, and external-link destinations across footers, contact/policy
pages, confirmations, and public metadata. Review the built publication artifact
for leftover placeholders, preserving explicitly requested fictional examples.
Recheck when operator/support arrangements change.

Use read-only checks and existing confirmation evidence first. Calls, emails, or
real form submissions need explicit authorization. Distinguish ownership checks,
configuration checks, and actual delivery tests; do not claim unperformed tests.
