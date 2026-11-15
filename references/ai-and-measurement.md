# AI search, distribution and measurement

## Eight-step workflow

1. **Earn discoverability.** Fix crawl, render and index eligibility for important public pages. Improve their organic relevance and usefulness. Search retrieval is a meaningful pathway. Eligibility and organic rank are baseline observations rather than forecasts of citations. Verify each platform's current access guidance.
2. **Map the prompts behind decisions.** Use real queries, sales calls, support and research to cover discovery, use-case fit, price, comparisons, alternatives, limitations, buying, implementation and troubleshooting. A manageable baseline is about 25 useful prompts for a broad project. Start smaller for a narrow task. Include branded and unbranded prompts and distinguish their roles. Assign each a current or proposed URL and one useful evidence asset.
3. **Make useful answers easy to find.** Put the factual answer or action early. For question-led sections provide a self-contained answer with the qualifying condition and source. Put supporting detail after the answer. Use plain language, labeled tables, meaningful headings and visible source links where useful. Support graphical facts with text or an accessible table.
4. **Publish defensible evidence.** Prefer real first-party results, accessible product methodology, original data, screenshots, tested examples, verified prices or well-substantiated viewpoints. For original studies specify collection window, inclusion criteria, sample size, method, limitations and update trigger. Ensure a passage can be quoted without losing a material qualification.
5. **Earn relevant independent coverage.** Find the publishers, reviewers, professional associations, podcasts, forums, YouTube channels, newsletters and communities relevant to observed prompts. Use a consistent truthful company name and product description. Pitch an authentic asset or answer a question in context. Record contact, suitability, status and disclosures as applicable. Keep outreach drafts separate from sending. Avoid planted reviews, mass posting and fabricated endorsements.
6. **Refresh substance.** Use evidence on stakes, demand, decay, changes and owner capacity. A quarterly review of roughly 20 priority URLs is a planning option on a larger site. Correct real details such as test numbers, product behavior, prices, images and sources. On a small or fast-changing site choose a different cadence. Monitor the updated cohort and avoid claiming a date change improved visibility.
7. **Make crawl and interpretation reliable.** Check renders, links, bots, Search Console evidence and suitable structured data. Give actual bylines, reviewer profiles and methodology where useful. Mark up visible eligible facts. Use the site owner's bot policy and official controls. Google AI features do not require special schema or an additional AI text file.
8. **Measure sources and outcomes.** Establish a fixed prompt panel and search baseline. Track source URLs, mentions and citations separately. Record absent responses and access gaps. Compare recurring evidence and prioritize tests that also solve a user task.

## Prompt panel method

- Choose surfaces deliberately. Examples include ChatGPT Search, Gemini with available grounding, Google AI Mode and Google AI Overviews where observed. A feature may not trigger. Access can vary by account, surface and country. Label inaccessible or unrun surfaces.
- Fix prompt text and ID, locale, language, surface, search or grounding settings and personalization conditions where practical. Record observed date/time, run ID, available model indicator and whether the feature triggered. Re-run in comparable sessions as resources permit. Use one data row per prompt × surface × run and a separate table for source URLs if there are many.
- Capture related evidence. Use actual linked URLs and store captures if practical. Record target domain cited, brand mentioned, product recommended and citation context as separate observations. Normalize tracking parameters for aggregation and retain raw links. For no response or no citations state the correct status, for example `not run`, `error`, `feature absent`, or `response observed with no source`.
- Define denominators. Citation rate can mean eligible observed responses citing the target domain divided by eligible observed responses, with eligibility stated. Report response count, feature trigger rate and unknowns separately. Track comparable core prompts across periods. Distinguish domain occurrence from URL and mention occurrence. Multiple runs may vary. Avoid reducing observations to a single unexplained visibility score.
- Use current Search Console reports. Inspect dedicated generative visibility reports when available. Read the documented dimensions and metric definitions before comparing them with ordinary Web performance. Augment with analytics and tagged referral traffic where observable. Keep direct AI citations separate from search impressions, sessions and assisted conversions.
- For meaningful missing prompts classify the gap: crawl or index issue, wrong landing page, missing facts, weak evidence, brand coverage gap, irrelevant surface, or unexplainable variance. Pick one action that addresses evidenced weaknesses. Update page or distribution evidence and retest.

Prompt map columns: prompt_id | verbatim prompt | language | target locale | intent | branded/unbranded | preferred URL | evidence asset | priority | origin.

Run log columns: prompt_id | run_id | timestamp and timezone | surface | model or unknown | grounding and personalization settings | locale | feature status | target cited | brand mentioned | recommendation context | evidence capture | notes.

Citation log columns: run_id | prompt_id | raw source URL | normalized URL | domain | citation context | source type | source relevance | actionable relationship or content gap.

## Organic and conversion measurement

| Goal | Baseline and cohort | Signal |
| --- | --- | --- |
| Eligibility | Submitted and intended canonical URLs by template | Valid discovery/index state, canonical matches, significant crawl errors. |
| Qualified discovery | GSC clicks/impressions by page, query group, brand, market and device as available | Qualified search demand captured. Use the same segmentation and comparable dates. |
| Search presentation | CTR by relevant query and page cohort | Change in engagement among impressions. Account for positions and SERP feature mix. |
| Content or product utility | Analytics and real primary action by landing page or template | Demo, qualified lead, checkout, tool completion, signup or other stated goal. |
| AI visibility | Fixed prompt panel across comparable runs plus platform reports | Mentions, citations, triggering, recurring sources and qualified referrals as distinct measures. |

Record release date, baseline window, follow-up window and confounders such as seasonality, tracking changes, promotions, SERP changes and simultaneous releases. Use comparable 28-day periods or another window justified by demand, and use year-over-year checks where useful. Check deploy verification early and effect over an appropriate crawl and demand window. For similar untreated pages use comparison cohorts where practical. Report observations and plausible explanations separately. When a metric changes give its denominator and date range.

For topical map releases log the target template, cluster and first observed discovery/indexing where available. Compare still-eligible page cohorts and fixed query groups before attributing changed averages to page quality. Monitor branded and nonbranded visibility independently if the roadmap includes a brand or independent coverage initiative.

## Priority and cadence

1. Treat widespread accidental index exclusions, broken purchase or lead journeys and critical misinformation as blockers where observed. Fix or isolate them first.
2. For the remaining issues rate impact (1–5), confidence (1–5) and effort (1–5). Use impact × confidence ÷ effort as a sorting aid. A 1 indicates minor impact, speculative confidence, or minimal effort on its respective dimension. A 5 indicates site or revenue-scale impact, direct reproducible evidence, or major effort. Order by documented dependencies before applying the score. An uncertain high-impact issue gets a verification action.
3. Give each item a target, owner role, fix, reason, acceptance test and follow-up metric. For a full site propose staged work across days 1–30, 31–60 and 61–90 with baseline and review points. For a single page give a small action sequence matched to crawl frequency and expected traffic. Prompt checks can start monthly. Adjust the interval to volatility and available sample sizes.
4. Use historical claims only as hypotheses to test. Mark external study numbers with date, surface, method and denominator. Record the actual outcomes before reporting lift. Track wins and setbacks in the same format.
