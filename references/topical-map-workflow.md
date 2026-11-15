# Topical map from research to publishable URLs

Apply to new sites, sections and existing inventories. This implements the 30 numbered steps in **Topical Map Steps.xlsx**, including the research and template expansion substeps. Scale the depth to the request. When data is missing deliver a provisional map with a research queue. A complete map records why each page exists and what it helps the audience do.

## 1–10. Define the scope before collecting terms

| Workbook steps | Work | Output |
| --- | --- | --- |
| 1–2 | Define source context (audience, actual offer, role and conversion) and disambiguate the central entity. | One scope statement. Named entity, aliases, class and excluded meanings. |
| 3 | Model ontology (properties and relationships) and taxonomy (parent, child and sibling types). Start from trustworthy sources and verified inventory. | Entity graph and claims ledger. Mark generated relationships as candidates. |
| 4–5 | Express central search intent as an action, entity and decision. Define buyer personas or ICPs by task, qualifying signals, constraints and objections, using sales, support or observed evidence where available. | Intent statement and buyer journeys with verified and assumed attributes distinguished. |
| 6–7 | Define core and outer coverage. Core solves the primary decision and supports the offer. Outer answers adjacent tasks with a credible next step into the core. | In-scope attributes, exclusion rules, and intended links or bridges. |
| 8–9 | Identify sources with strong comparable coverage. Choose one or more benchmarks by actual query and page-type overlap, originality, accuracy and fit. Analyze the catalogue, evidence, layout, internal paths and topic gaps. | Comparable benchmark set with reasons and one gap the site could credibly fill. Do not assume benchmark similarity produces favorable algorithmic classification. |
| 10 | Select relevant derived entities, related entities, attributes and actions from the model. Sort into research now, later or exclude. | Bounded research seeds tied to a real task and the source context. |

## 10.1–10.7. Build the query and evidence pool

1. **10.1 First-party search history.** Extract GSC rows by entity/alias in queries or relevant paths. Capture the query, landed URL, impressions/clicks, date range, locale/device when available and export limitations. Keep GSC impressions distinct from estimated total demand.
2. **10.2 Search surfaces.** Record representative organic results, autocomplete, related queries, People Also Ask, refinements, image and shopping filters, and knowledge features only where observed. Label surfaces so an ad or map result never counts as an organic position.
3. **10.3 Candidate expansion.** Use available models to propose entity–attribute pairs, relationships, variants and query patterns. Explore broader, narrower, part-of, substitute and use-case relationships. Keep crafted candidates separate from their observed demand evidence.
4. **10.4 Knowledge sources.** Use authoritative materials first. Wikipedia/Wikidata/Wiki Graph may reveal categories, references, aliases and graph neighbors. Confirm disambiguation and verify claims against relevant independent sources.
5. **10.5 Corpus wording.** Analyze sitemap path tokens, title/H1, H2–H6, main copy, internal anchors, image filenames and alt text when accessible. Maintain distinct corpora by surface and template. Keep boilerplate for a separate site vocabulary audit. Use observed phrases to improve wording and find differing contexts.
6. **10.6 Benchmark coverage.** Use sitemap, crawl or appropriate tool exports to compare page type, URL, representative query, covered attributes and useful formats. Compare the user task and missing information in addition to keyword overlap.
7. **10.7 Keyword tools.** Import available legitimate exports with provider, market, date and denominator or definitions. Keep rows for conflicting estimates instead of silently merging them. Leave unknown values blank. Deduplicate normalized query keys within comparable source, market and scope, while retaining raw text and provenance.

## 11–15. Generate templates and cluster by task

- **11 and 11.1–11.4.** Separate literal queries from recurring query templates. Examples include `[entity] for [task]`, `[entity] price in [place]`, `[entity A] vs [entity B] for [use case]` and `[product] compatible with [system]`. Expand the most relevant related entities through the same research loop and keep their resulting literals in the query pool. Stop when credible new tasks are scarce or fall outside the scope. Reuse an existing lexical sample when appropriate.
- **12–14.** Assign a demand metric only if you have a source. Organize queries with relevant competing documents, technique, provenance, market and date. For priority queries seek comparable result URLs where missing. Provide both raw evidence and any aggregate. A sum of estimated volumes can double count overlapping searches and must be labeled as a rough query-group sum. Keep ambiguous or unclustered queries in a queue.
- **15.** Cluster by user task, preferred page type, entity interpretation and expected answer. Compare normalized ranking URLs at the same depth when live results are available. Report both intersection and depth or Jaccard (intersection ÷ union) with date and locale. Domain overlap is weaker than URL overlap. Review the strongest counterexample before splitting or merging. Keep grouping provisional when only text similarity is available.
- **Representative and represented queries.** Give each cluster one representative query that best reflects its observed task and page type. Preserve the supported variants under it. Word order and qualifiers may change intent. Use live results and audience evidence to validate important borderline cases.

## 16–19. Turn a raw map into a working page plan

1. **16 Attribute filter.** Consider relevance to the source context and user task first. Then consider prominence to the specific decision. Use observed popularity as a later prioritization signal. A low-demand detail may be indispensable. A popular unrelated meaning stays outside the map.
2. **17 Categorize.** Record attribute, page type, format, funnel stage and required proof. Use the research and content references to assess the practical quality bar. Compare observed gaps with what the site can credibly produce. Third-party keyword difficulty is a directional input.
3. **18 Raw map.** Select core and outer nodes and each node's intended task. Track existing candidates, neighboring nodes and exclusions. Define the contextual boundary and one primary owner for every important task cluster. Section versus separate page depends on intent, scope, proof and user value. Record keep, update, split, merge, redirect, new or defer with the evidence.
4. **19 Processed map.** Specify the title, H1, preferred URL or preserved existing URL, meta description, proof, CTA, editorial owner and publishing status. Add planned image role, file or asset URL and meaningful accessibility text when useful. Connect the brief, draft and internal-link placements. Each publishable node has an acceptance check and post-publish metric.

## Working tables

| Table | Grain | Required checks |
| --- | --- | --- |
| [Query evidence](../templates/query-evidence.csv) | One observation per query and provider/surface/market/window | Reproducible provenance and no fabricated demand. Separate query templates from literal queries. |
| [Raw topical map](../templates/raw-topical-map.csv) | One task cluster | Intent and entity disambiguated. Core/outer membership, merge or split basis and plain-language reason. |
| [Processed topical map](../templates/processed-topical-map.csv) | One target page or explicit defer | URL ownership, facts, visual, CTA, dates, readiness, dependencies and measurable outcome. |
| [Entity fact ledger](../templates/entity-facts.csv) | One claim with conditions | Primary proof, date and status. Record conflicting values instead of treating all as verified. |
| [Brief sections](../templates/brief-sections.csv) | One content or functional slot | Each slot has a user task, answer shape and proof or approved source. |
| [Internal links](../templates/internal-links.csv) | One proposed link placement | Source, destination, placement, anchor idea, user reason and verification. |

Use `cluster_id`, `page_id` and `fact_id` consistently across tables. Use semantically meaningful stable IDs. Deliver applicable tables and a brief implementation sequence. A site strategy needs an URL inventory and actual or proposed routes. A paragraph rewrite generally does not need these tables. For each planned wave check capacity, proof and dependencies. Add pilot pages before scaling new templates. Revisit cluster borders when evidence changes.
