# Research and topical maps

## Build an evidence set

1. Start with business and product reality. Record the source context: who serves whom, what they offer, why the site can cover the subject, its geography and how it converts. Pick the central entity or service and central search intent. A mixed site can have different scope statements for major sections.
2. Build a query pool from customer language, GSC, site search, support and sales questions, product or service inventory, SERPs and suggestions. Record a source and date for each. Include intent, audience, stage, qualifiers, entities, region and language. Distinguish observed demand from supplied or brainstormed ideas. Record unavailable volume or difficulty as unknown.
3. Search a focused set of representative queries when tools permit. Record date, locale, device if known and limitations. Sample genuinely comparable organic pages, usually 3–8 per important cluster when available, and record exclusions. Keep business competitors, SERP competitors and AI-cited sources as separate sets that may overlap. Note dominant formats, commercial features, official sources, user objections, useful scope and conversion paths. Keep ads, maps, AI answers and organic links distinct. If only snippets are available, limit claims to them.
4. Capture URLs, the query that surfaced them, page type, visible H1 and representative sections, evidence and limitations, update signals and key internal links when accessible. Find repeatable passage patterns and unmet needs. Highlight weak availability, missing test methodology, hidden costs or missing edge cases where observed. Compare the attributes that matter to customers. Summarize competitor evidence in original language.
5. Remove duplicate canonical pages and separate templates, site boilerplate, comments, footer, navigation and ads from relevant text. Distinguish facts from competitors' assertions. For scaled research use a stratified sample by intent, template and geography with coverage noted. Do not treat the sample as the entire SERP.

Suggested observation columns: query | locale | observed date | surface | organic position if known | URL | page type | topics and coverage | proof | gap | caveat.

## Build the entity and vocabulary map

- List the main entities, aliases, entity types, attributes, relations and evidence. Use entity–attribute–value for factual properties and subject–predicate–object for relationships. Include conditions, units and dates where they change meaning. Resolve ambiguity with identifying attributes or authoritative registry IDs when helpful.
- Classify candidate coverage as **essential** to answer, **supporting** to clarify a decision, **adjacent** for optional linking, or **out of scope**. Convert important relationships into questions, sections, examples, glossary entries or separate pages when search intent and user value support one.
- Use authoritative product data, standards, documentation and first-party materials to verify entity claims. Use Wikipedia/Wikidata and [Wiki Graph](https://github.com/blinpete/wiki-graph) for exploration. Start from an unambiguous entity, inspect adjacent nodes and filter each by business or task relevance. The graph's edges indicate an editorial or API relationship. Verify each important relationship independently before use. A nearby node alone does not justify a page, term or schema relationship.
- For **scaffolding**, the main job might be selecting a system for a project. Candidate entities might include frame scaffold, tower scaffold, platforms and guardrails. Validate product compatibility from manufacturer data and safety or loading claims against current local authorities before drafting. A local rental page covers available systems, site constraints and quote logistics. A design explainer may cover different questions.

Suggested entity columns: entity | type | aliases or ID | relation or attribute | value and conditions | source | priority | URL or section.

## Run lexical research when a useful corpus exists

| Signal | How to calculate or collect | Use |
| --- | --- | --- |
| N-grams | Count contiguous 2–4-token spans from cleaned same-intent main content. Report occurrence count and distinct-document count. | Identify established phrases, product labels, modifiers and common task descriptions. |
| Skip-grams | Compare ordered token pairs with one or two intervening tokens within a sentence. Document the window and corpus. | Surface contextual pairings worth reading in the source passage. |
| NLP keywords | Use an available model or transparent extraction to identify noun phrases, categories, aliases and attributes. Review actual context. | Check comprehensibility and missing concepts. Use a heuristic label unless a specific model and score exist. |
| Auto-suggest | Record actual autosuggest, question features, first-party queries or other available sources with locale/date. Keep generated candidates labeled as hypotheses. | Expand the query pool and build an intent check. Suggestions do not reveal exact search volume. |
| Distinct vocabulary | Compare approved first-party vocabulary and useful terms underrepresented across the comparable corpus. | Surface real differentiation and niche terms worth validating. Rarity alone proves little. |

Measure document support as distinct matching source pages divided by distinct eligible pages. Preserve excerpts privately for review and keep claims tied to their original source. Use counts to investigate, never as insertion quotas. Inspect repeated unnatural phrases, cross-intent contamination and branding artifacts. For larger clean-text samples use [lexical-audit.py](../scripts/lexical-audit.py). It reports transparent counts and supports a minimum document frequency. It does not perform entity extraction, NLP scoring, rank tracking or live keyword lookups.

## Turn research into the URL map

1. Define the core cluster close to the audience's primary job and the site's legitimate offer. Define supporting clusters that deepen understanding or help adjacent decisions. Reject unrelated topics raised only by keyword volume or graph proximity.
2. Group variants with a shared goal, format and likely answer. Compare live ranking URL overlap when possible. Report the overlap as intersection and denominator or Jaccard ratio and record sampling depth. Format and locale matter. Treat overlap as a directional check. Split when the task, proof, inventory, audience or CTA differs materially. If live data is unavailable label the grouping provisional.
3. Inventory existing URLs and query groups. Distinguish legitimate multi-URL appearances from actual competition. Look for the same intent paired with swapping preferred URLs, divided internal signals or landing pages that miss their goal. Reuse a suitable URL. Use redirects for genuine replacements with an equivalent destination. Preserve useful individual pages that serve distinct tasks.
4. Assign one preferred owner URL, page type, task, entity focus, relevant attributes, H1 angle, evidence needs, answer format, CTA and priority for each cluster. Include known query variants and buyer prompts. Match titles to the search task using natural phrasing. Preserve an established URL unless a documented issue or consolidation warrants migration.
5. Map links between hub, detail, supporting and conversion pages where the destination advances the reader's next task. Record source, destination, location and reason. Place contextual bridges at the relevant passage and use natural anchors. Ensure important indexable pages have inbound paths. Test hyperlinks, canonical target and destination indexability where intended.

Topical map columns: cluster ID | core or supporting | entity and task | representative queries and prompts | locale | page type | current URL | preferred URL | keep/update/split/merge/new/defer | proof gap | parent or links | CTA | priority and basis.

Internal link columns: source URL | destination URL | placement | anchor idea | user reason | existing/proposed | validation result.
