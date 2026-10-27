# Favicons And Web App Icons

Maintain a coherent icon family derived from the site's approved identity.
Favicons identify the site; app icons identify a bookmarked or installed app;
[share images](page-metadata.md) identify individual pages. Provide assets and
declarations for each applicable surface rather than treating one file as proof
that all three work.

## Favicon Design

Every website must have a favicon set declared with `<link rel="icon">`, using
accurate `type` and `sizes` values. If no suitable favicon exists, work with the
user to develop one from the logo. If the logo itself is missing, establish the
identity with the user before finalizing it.

Test the mark at actual 16, 32, and 48 pixel sizes. Simplify fine details, adjust
spacing/strokes, or develop a symbol variant when shrinking the full logo loses
recognition. Treat this as graphic design work, not merely file conversion. Use
appropriate graphic design tooling or specialist support when needed, and review
meaningful adaptations with the user. Preserve editable source artwork and
record approved variants in the project's design docs.

Prefer SVG for suitable vector artwork and scalable rendering where supported.
SVG supports full color as well as monochrome. Use PNG for raster/full-color
artwork or required platform exports. Include raster sizes required by the
selected browser/platform targets; use ICO only when those targets call for it.
Do not add old-platform compatibility assets without an agreed support need.
An SVG can scale cleanly and still be illegible at tiny sizes, so visual checks
remain required.

GIF may be considered for an optional animated favicon only after verifying
both format and animation behavior on the supported browsers/surfaces. Do not
assume GIF acceptance means the animation plays. Keep a complete static icon
set; essential identity or state must not depend on animation. Review motion
for distraction and accessibility before adopting it.

References: [icon declarations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#icon),
[favicon formats](https://developer.mozilla.org/en-US/docs/Glossary/Favicon),
[image formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types).
For public search, also satisfy the current
[Google favicon requirements](https://developers.google.com/search/docs/appearance/favicon-in-search).

## Web App, Bookmark, And Home-Screen Icons

Web apps must declare appropriate icons for their supported bookmark,
home-screen, and installation surfaces. Ordinary browser bookmarks use site
icons; home-screen and installed-app surfaces may use different declarations.

- For manifest-based home-screen/install targets, link a web app manifest with
  `<link rel="manifest">` and configure the real app identity and supported launch
  behavior. Provide icon sources with accurate type, size, and purpose metadata.
  Ordinary bookmark support alone does not require installing a PWA or adding a
  service worker. Optional manifest fields need not be set without a reason.
- Provide suitable PNG app exports, commonly 192 and 512 pixels for Chromium
  installation targets, plus maskable artwork when supported/needed. Design for
  the mask's safe area instead of simply labeling an ordinary icon `maskable`.
- Include `<link rel="apple-touch-icon">` where appropriate for supported Apple
  bookmark/home-screen surfaces; a 180-pixel PNG is a common export. Check current
  platform selection behavior with both manifest and touch icons present.
- Record chosen target platforms and sizes. Do not assume favicon declarations
  alone satisfy app icon requirements, or that icons alone establish complete
  PWA/installability support. Add platform-specific tags only for a defined need.

References: [manifest icons](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/icons),
[app icon design](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons),
[installability](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable),
and [WebKit icon selection](https://webkit.org/blog/14787/webkit-features-in-safari-17-2/).

## Verification

Add an icon inspection view to the [test sitemap](test-sitemap.md), with actual-size
favicon samples, light/dark backgrounds, and app icon crop/mask previews. Inspect
the real browser tab and bookmark, check declarations and asset responses, and
test home-screen/install appearance on supported platforms when available.
Preview images alone do not prove OS/browser selection. Record any unavailable
device checks instead of claiming cross-platform completion.
