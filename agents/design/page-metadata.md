# Page Metadata And Share Images

Use one metadata source per distinct page, including public content records and
localized versions. Query aliases and transient UI states are not automatically
separate pages. Canonicalize duplicate URLs and derive matching tags from the same
page data rather than copying homepage defaults.

## Titles, Descriptions, And Semantic Markup

| Surface | Requirement |
| --- | --- |
| Browser/search | One meaningful unique `<title>` and `<meta name="description">` per distinct page |
| Open Graph (including Facebook/Meta) | Page-specific `og:title`, `og:description`, `og:image`, `og:url`, and appropriate `og:type`; site name/locale as relevant |
| Other targeted social platforms | Their supported card fields, such as `twitter:card`, title, description, image, and image alt text; verify current platform requirements |
| Semantic HTML | Correct document language, meaningful main heading, logical hierarchy, and appropriate landmarks/content elements |
| Structured data | Relevant Schema.org types describing real page content/entities; prefer JSON-LD where appropriate for Google |

Keep visible content and metadata consistent in meaning. Do not invent ratings,
prices, authors, dates, or business details to fill a schema. Choose types for the
actual page, such as an article, product, application, or breadcrumb trail. Open
Graph, semantic HTML, and structured data serve different purposes; none replaces
the others. Search engines can rewrite titles/snippets or decline rich results.

References: [titles](https://developers.google.com/search/docs/appearance/title-link),
[descriptions](https://developers.google.com/search/docs/appearance/snippet),
[structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data),
and [Open Graph](https://ogp.me/).

## Unique Page Images

Give each distinct public shareable page its own representative image. Reuse a
branded layout with page-specific artwork, content, or title treatment; a single
generic logo card everywhere is insufficient. A social image need not be a hero.

Set stable absolute HTTPS image URLs, accurate type/dimensions, and descriptive
`og:image:alt`/applicable card fields. Export a consumer-supported format, typically
PNG or JPEG, even if the editable source is SVG. Check target-platform crop, size,
and file limits, and inspect legibility at actual thumbnail sizes.

## Delivery And Scope

For public shareable routes, deliver metadata in initial HTML through the existing
build/server approach; do not depend on social crawlers executing JavaScript.
Client navigation must also replace stale titles/tags. If the current architecture
cannot provide this, identify the gap and resolve the approach within project
scope; this rule alone does not authorize a framework migration.

Private pages still need safe, meaningful titles/descriptions. Use page-purpose
text rather than leaking private records into metadata. Public share cards are
not required for private, test, transient, or error surfaces. Record deliberate
exclusions once; do not publish private images merely to achieve uniqueness.

## Keep robots.txt Current

Serve maintained `/robots.txt` at each deployed website origin. Keep one policy
source/generator per environment. Review affected rules when routes, domains,
public/private boundaries, environments, or crawler policy change, and at release.
No file edit is needed when current rules still express the intended policy.

Keep `Sitemap:` URLs current and absolute. Remove obsolete exclusions, preserve
intended access to public pages/rendering assets, and prevent staging-wide blocks
from leaking into indexable production sites. Preserve deliberate crawler choices.
`robots.txt` controls crawling, not authentication or guaranteed exclusion from
search; keep secrets out. Put `noindex` in page metadata or `X-Robots-Tag`, not
robots.txt, and allow crawling when a crawler needs to read that directive.

Check the built/served file returns 200 and UTF-8 plain text, not app-shell HTML.
Evaluate representative allowed/disallowed paths, user-agent matching, and rule
precedence with a parser appropriate to the targeted crawlers. Verify current
sitemap URLs and host/CDN contents after authorized deployment. A file update
does not prove crawlers refreshed their cached copy.

References: [creation](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt),
[interpretation](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec),
[crawl/index controls](https://developers.google.com/search/docs/crawling-indexing/robots/intro).

## Generate And Maintain The Public Sitemap

Sites with public indexable pages need current XML sitemaps, normally at
`/sitemap.xml`, or an index. Prefer generation from authoritative routes/content:

- **Build:** generate and deploy with the corresponding pages.
- **Runtime/CMS:** refresh on content publication, changes, moves, and removal;
  define bounded cache freshness independent of code releases.
- **Manual:** acceptable for small stable sites if page changes update the sitemap
  in the same change and release checks detect missing/stale entries.

Include intended indexable canonical absolute production URLs. Exclude drafts,
private/test/error pages, redirects, removed/noindex pages, and duplicate variants.
Keep canonical metadata, robots rules, and sitemap entries aligned. Use `lastmod`
for known significant page changes, never merely build time; omit unknown dates.
Split files within current protocol limits and keep robots.txt references current.
Fully private apps can document that no public sitemap applies.

Check XML validity, unique encoded URLs, coverage/exclusions against the source
inventory, and actual deployed freshness. Do not replace a good sitemap with an
empty/partial one when its source fails; surface and fail the update. Check index
and child files return 200/XML and representative URLs resolve as expected. Run
checks in the content-update path as well as releases when content changes
independently. A sitemap assists discovery but does not guarantee indexing.
Reference: [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).

## Verification

Use the [test sitemap](test-sitemap.md) for page-type inspection, plus the actual
route/content inventory to catch duplicate/missing metadata across records.
Inspect original HTML, client-navigation updates, URLs, asset responses, and card
rendering. Validate relevant structured data and target-platform previews where
available and authorized. Local previews do not prove live crawler rendering;
record caching/platform limits and unverified checks. Keep private/unpublished
content out of external validators without authorization.
