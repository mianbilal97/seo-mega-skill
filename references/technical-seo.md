# Technical SEO and implementation

Use official documentation for current platform behavior. Trace a template observation to evidence and a specific fix. Test the final state at the same layer where the issue occurs.

## Audit sequence

| Layer | Verify and record | Acceptance check |
| --- | --- | --- |
| Response and routes | HTTPS, final status, redirects, soft-404s, served host and paths, application fallbacks, robots.txt and CDN/WAF access. | Intended URLs return the expected final status with a useful response. Equivalent redirects use one hop when practical. |
| Rendering | Compare initial HTML and user-visible rendered page for primary content, links, metadata, hreflang and structured data. Sample mobile and relevant empty or error states. Use Search Console URL Inspection where available. | Important text, links and metadata are accessible on the intended route. Document whether direct crawler evidence was available. |
| Crawl and index | Identify intended indexable templates and exclusions. Inspect meta robots, HTTP X-Robots-Tag, canonical, sitemap and actual index evidence separately. | Key pages can be crawled and are eligible to index. The intended canonical and representative Google-selected canonical agree where confirmed. Excluded URLs use appropriate mechanisms. |
| Discovery and duplication | Crawl internal links and inspect orphan candidates, depth, URLs in XML sitemap, parameter and filter inflation, pagination, internal search and cross-host duplicates. | Intended canonical URLs have crawlable paths and clean sitemap membership. Low-value combinations stay within the site's chosen crawl and index policy. |
| On-page interpretation | Inspect distinct titles, primary visible headings, descriptions, meaningful anchors, body sections, alt text, mobile usability and content continuity across variants. | The page identity and task are clear and consistent across metadata, rendered UI and links. |
| Page experience | Use field data when available. Segment by mobile or desktop and by template. Use lab data to diagnose likely causes. Check heavy scripts, image sizing, keyboard use, layout stability and the conversion flow. | Working interaction and measurable improvement in targeted conditions. Document lab or field context and check current Core Web Vitals thresholds if reporting them. |
| Enhancement and feeds | Validate data types and visible claims, feed availability and eligibility for applicable Search features. Inspect results with current official tools and actual Search Console evidence where possible. | Required properties are sourced and valid. Feed, page and structured data agree. Rich-result display is an independently tracked outcome. |
| Measurement | Check event definition, firing, duplicates, consent behavior and funnel attribution in available environments. | Intended interactions produce verified events without duplicate reporting. Preserve prior event names or document deliberate migrations. |

## Operational decisions

- A robots.txt block controls crawl access and is not a reliable removal mechanism for a known URL. For a crawlable page excluded with noindex, allow the crawler to read the directive. Use authentication for private assets and choose HTTP status or an appropriate removal workflow for retired pages. Verify response headers and search engine behavior before rollout.
- Canonicals are signals. Keep redirects, internal links, sitemap URLs and canonical tags aligned. Avoid chaining canonicals or pointing across divergent content. Check pagination and product variants against actual URL behavior. Leave stable URLs alone unless the change has a clear purpose and a migration plan.
- Include discoverable, preferred indexable URLs in XML sitemaps. Use accurate modification dates and verify declared canonical and directive consistency. Spot-check sitemaps for redirects, duplicates and errors.
- For ecommerce or marketplace facets inventory crawlable paths and parameter combinations. Select indexable subsets by real demand and useful inventory. Decide the treatment of the remainder after testing discovery, existing indexation and user benefit. Avoid blanket blocking if it prevents intended discovery or noindex processing.
- For multilingual or regional sites map genuine regional variants, localize search and commercial details, validate reciprocal hreflang and confirm compatible canonicals. Keep locale switching accessible. Avoid silent location redirects that prevent people or crawlers from reaching alternate locales.
- For migration or large template changes preserve a URL snapshot, analytics baseline and one-to-one redirect map for equivalent replacements. Verify new responses, analytics, content parity, metadata, links, XML sitemaps and monitoring. Roll out by template or canary when practical. Define a rollback trigger for indexability and conversion regressions before release.
- For tools and dynamic destinations preserve functionality, stable inputs and useful default output states. Understand which URLs are public, private, shareable or temporary before setting canonical or crawler directives.
- Verify Googlebot and OAI-SearchBot access where eligible visibility is an objective. Review bot rules across robots.txt and edge controls. Keep the owner's separate GPTBot training choice as an independent decision. A synthetic user-agent request is a diagnostic clue only. A successful generic request does not prove a verified bot can crawl.
- For a live audit report risks and checks individually. A fetch of several public pages cannot verify full-site indexation, access logs, canonical selection or authenticated workflows.
- Use the website authority checklist pattern from the Dubai workbook to record the specific URL or template, test, evidence, date and status. Separate eligible indexation from normal exclusions. Add ownership and maintenance checks such as current platform configuration, backups and dependency health when directly relevant to a rollout. Verify existing capabilities before suggesting an installation or architectural change.
- In a site or template review inspect actual click paths and responsive headings, breadcrumbs and content order. For images choose appropriate formats and sizes, a crawlable path for meaningful assets and accessible alt text. Check visually significant content and compatible canonical signals in the rendered mobile experience.

## Structured data choices

Select only the types relevant to the visible page and verify current Google support and required fields when a search feature matters. For example consider Product and eligible variant formats for products, BreadcrumbList for appropriate hierarchies, Article for relevant editorial pages, VideoObject for an eligible video page, or Organization or LocalBusiness where actual identity and page scope match. For SaaS or web tools check applicable SoftwareApplication guidance and real properties before suggesting it. Ensure consistent identity IDs, URLs and values across templates. Avoid fabricated ratings, fake location attributes and unavailable offers. Useful visible FAQs do not imply FAQ rich-result eligibility. Google AI features have no special schema requirement. Keep schema validation separate from indexing and actual rich-result observation.

## Platform-aware implementation

| Platform | Where to inspect first |
| --- | --- |
| WordPress or similar CMS | SEO plugin and theme output, permalink and archive settings, staging privacy, rendered HTML and sitemap sources. Detect competing generators for robots or metadata. |
| Shopify or comparable store | Theme sections, product/collection routes, variants, app-generated meta, filtering and feeds. Check canonical output on actual routes. |
| Next.js or code-based app | Route metadata, server/client render boundaries, canonical base URL, redirects, locale routing, robots and sitemap generation, headers, fixtures and event code. |
| Webflow or page builders | Per-page CMS templates, dynamic fields, global head or custom code, search settings, redirects, environment URLs and publish controls. |
| Other or unspecified | Inspect the existing route and template authority. Give implementation requirements and checks until the actual platform is known. |

Find the existing source of truth before changing code. Prefer edits at the affected page or correct template boundary. Preserve useful overrides and shared behavior. Before release check representative linked paths and error states. Report exact changed files or CMS fields, passing checks, checks needing external access and verification timing.

Finding columns: ID | severity | affected template/URLs | observed evidence | intended state | user impact | priority | proposed fix | owner | acceptance check | status.
