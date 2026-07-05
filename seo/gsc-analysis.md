# GSC Opportunity Analysis (Subagent 3)

Source: `seo/gsc-raw-data/*.csv` (Apr-Jul 2026 export). Opportunity score =
impressions ÷ position (higher = more impressions being wasted at a
reachable-but-unrealized position). Uses actual **page-level** position from
`Pages.csv` where a page exists, not the single best-ranking query variant,
since that's what most of a cluster's impression volume is actually
experiencing.

## Quick win already applied
**香港深層廚房清潔** ranks position 6.6 (page 1) with 52 impressions and
**zero clicks** - not a ranking problem, a title/meta problem. The exact
phrase wasn't in the page's `<title>`, meta description, or H1. Fixed in
`blog-post-kitchen-cleaning.html` (this commit) - free win, no new content
needed, should show up in GSC within 1-2 weeks.

## Cluster opportunity ranking (page-level position)

| Cluster | Impressions | Page position | Opportunity score | Priority in CSV |
|---|---|---|---|---|
| Bathroom | 1900+ | 10.44 | **~182** | High |
| Kitchen | 600+ | 13.52 | **~44** | High |
| Carpet (11) | 850+ | ~45 (blended across 3 pages) | **~19** | Medium |
| Office | 2500+ | 71.29 | **~35** | High |
| Mold (4) | 490+ | n/a (no page) | n/a - zero competition | High |

## Stress-test: is office cleaning worth near-term content investment?

**Largely agree with the working conclusion, with one refinement.** At the
page level (71.29), office cleaning's raw opportunity score (~35) is
competitive with kitchen's - but that's misleading: it's driven entirely by
volume (2500 impressions), not efficiency. The generic head terms specific to
office cleaning - 辦公室清潔 (pos 86), 辦公室清潔公司 (pos 77), 辦公室清潔服務
(pos 82), 包月清潔 (pos 89-90) - are all stuck on page 7-9 and look like a
genuine domain-authority/backlink ceiling, not a content gap.

**But** one query in the same cluster, 辦公室 深層 清潔 (specific long-tail
phrasing), already sits at position 35.77 - roughly page 4, moving. That's
real evidence that specific, narrow phrasing can gain ground even in this
cluster while the broad head terms can't. **Recommendation: don't drop office
cleaning, but stop trying to rank the broad pillar term with content alone.
Target the narrow supporting pages already in `content-planner.md` (monthly
contract, disinfection, price guide) and treat the broad "辦公室清潔公司"
head term as a backlinks/GBP problem on a longer timeline**, exactly as
already planned.

## New finding not in the current CSV: 除臭 (odor removal)

除臭服務 (93 impr, pos 31.4) and 除臭公司 (81 impr, pos 30) aren't tracked as
their own cluster, but together represent 174 impressions at a genuinely
reachable position (page 3) - better efficiency than most office-cleaning
queries. This is closely adjacent to both the mold pillar and the existing
`_drafts/2026-07-16-carpet-odor-removal-tips.md` draft. **Recommend**: either
add as `cluster_id 16` (除臭服務 / General Odor Removal) linking the mold
pillar and the carpet-odor draft together, or fold explicitly into the mold
pillar's internal linking rather than leaving it untracked. Not urgent, but
too good an opportunity score to leave completely off the plan.

## Carpet cluster may be underrated at "Medium" priority

At ~19, carpet's opportunity score beats every Medium-priority cluster and
approaches office's. It already has 2 dedicated pages (lower structural
lift than starting a new pillar) and the second-highest raw impressions
(850+) in the whole dataset. Worth considering bumping to High alongside
bathroom/kitchen/mold, or at minimum front-loading its planned supporting
pages (carpet disinfection, stain removal) earlier in the 12-month calendar
than currently scheduled.

## Zero-click, high-impression queries worth a title/meta pass (same fix as kitchen)
- 浴室清潔 - pos 22.84, 127 impr, 0 clicks - close to page 2, a title/meta
  refresh on the bathroom pillar could realistically convert some of this
  without new content.
- 深層清潔公司 (generic "deep cleaning company") - pos 44.36, 234 impr, 0
  clicks - doesn't map cleanly to any single existing page; worth checking
  which page currently ranks for it (likely `services.html` or the
  homepage) and reinforcing that page's title/meta for this exact phrase.

## Geography and device (secondary, informational)
- Hong Kong dominates by volume (7,030 impressions) but international
  traffic (US 563, Taiwan 253, Canada/Australia ~80 each) ranks noticeably
  *better* (position 7-11) than the HK-targeted pages (position 52 avg) -
  almost certainly the site's non-cleaning novelty pages (carpet/clock
  learning games) picking up irrelevant global traffic. Not actionable for
  the cleaning business, just explains why blended average position looks
  worse than the cleaning content's real position.
- Mobile outperforms desktop on every metric that matters (47 vs 15 clicks,
  1.45% vs 0.29% CTR) despite fewer impressions. Confirms HK local-service
  searches skew mobile - worth keeping in mind for page speed/UX priorities
  on any new pages, though no specific technical issue was found in this
  data alone.
