# Content Calendar — Status & Aug–Dec 2026 Plan

## What actually happened to the original plan

The original 24-post, 12-month calendar (2026-07 → 2027-06, drip-fed via
`_drafts/` → `auto-publish.yml`) assumed a slow cadence of 2 posts/month.
Instead, 16 of those cluster-topic slots were fast-tracked and directly
published as static `blog-post-*.html` pages, cross-linked and merged
straight to `main`, months ahead of their original scheduled dates:

- **Office cluster**: pillar + 辦公室清潔公司 (buyer's guide) + 寫字樓包月清潔 — done
- **Bathroom cluster**: pillar + 廁所清潔 + 浴室消毒 + 淋浴間去水渠清潔 + 浴室深層清潔收費指南 — done
- **Kitchen cluster**: pillar + 抽油煙機拆洗 + 廚房水槽清潔 + 雪櫃清潔消毒 + 廚房深層清潔收費指南 + 餐廳隔油池清洗 — done
- **Mold cluster**: pillar + 浴室磁磚縫除霉 + 牆身天花除霉 + 冷氣機發霉清洗 + 除霉公司邊間好 — done

Every one of those pages has a real, human-verified Replicate-generated
hero image and is cross-linked from its pillar and `blog.html`.

**Still genuinely open** (checked against `seo/clean-com-hk-topical-cluster-plan.csv`,
not just the old calendar's guesswork):

| Cluster | Topic | Status | GSC impressions | Priority |
|---|---|---|---|---|
| 1 (office) | 辦公室消毒服務 (dedicated disinfection page) | never written | 309 (query `辦公室消毒`) | High — biggest remaining single gap |
| 7 | 家居定期大掃除 (home regular cleaning, new pillar) | `missing_entirely` | 185+ | Medium |
| 9 | 滅蟲服務 (dedicated pest-control service page — separate from the existing `blog-post-hsr-mosquito-alert.html` news piece) | `missing_entirely` as a *service* page | 41 | Medium |
| 12 | 高溫蒸氣消毒 | `missing_entirely` | 0 | Low |
| 13 | 清潔招牌及玻璃門窗 | `missing_entirely` | 0 | Low |
| 14 | 吸水服務 | `missing_entirely` | 0 | Low |

Everything else in the CSV (carpet, floor, renovation, general disinfection)
already has a dedicated or blog-level page and isn't a priority gap.

Per Subagent 3's original mandate: office cleaning still has the single
largest impression pool in the whole CSV but sits at position 35-70 —
content alone will not fix that; see `seo/gsc-analysis.md` before
committing paid/backlink budget there instead of more posts.

## Aug–Dec 2026 plan

Cadence: 2 posts/month, 10 posts total. Prioritized by real GSC opportunity
first, then a genuine Hong Kong seasonal angle (Lunar New Year 大掃除 demand
spikes every Dec–Jan ahead of CNY, which falls 2027-02-17), then the
remaining zero-impression low-priority gaps batched cheaply at the end.

| # | Target week | Topic | Rationale |
|---|---|---|---|
| 1 | 2026-08-03 | 辦公室消毒服務完整指南 (`office-disinfection-service`) | Closes the office cluster's last real gap — 309 impr query, currently unserved |
| 2 | 2026-08-17 | 家居定期大掃除完整指南 (`home-regular-cleaning`, new pillar) | Biggest remaining pillar-level gap, 185+ impr, one of the original 11 site categories |
| 3 | 2026-09-07 | 滅蟲服務完整指南 (`pest-control-service`) | Dedicated commercial-intent service page; existing mosquito post is news/awareness, not conversion-focused |
| 4 | 2026-09-21 | Trust/EEAT series #4 — 清潔公司如何處理客訴？(`handling-customer-complaints`) | Keeps author-authority signal fresh per the original series cadence (last one used was `punctual-cleaning-kowloon`) |
| 5 | 2026-10-05 | 清潔招牌及玻璃門窗清潔指南 (`shopfront-glass-signage-cleaning`) | B2B/shopfront angle, zero on-site competition |
| 6 | 2026-10-19 | 吸水服務指南：水浸後點處理？(`water-extraction-service`) | Still inside HK's typhoon/heavy-rain season (May–Nov) — timely for flood/water-damage searches |
| 7 | 2026-11-02 | 年廿八大掃除完整指南：農曆新年前點清潔？(`lunar-new-year-deep-cleaning`) | Seasonal: CNY 2027 is Feb 17; publishing in early Nov gives ~3 months to rank before the search spike that typically starts mid-Dec |
| 8 | 2026-11-16 | 高溫蒸氣消毒完整指南 (`steam-disinfection-service`) | Clears the last zero-impression low-priority gap; pairs naturally with the CNY post above (post-large-gathering hygiene angle) |
| 9 | 2026-12-07 | 農曆新年大掃除收費指南：邊間清潔公司好？(`lunar-new-year-cleaning-price-guide`) | Commercial-intent companion to #7, timed right before the actual pre-CNY booking rush |
| 10 | 2026-12-21 | Trust/EEAT series #5 — 2026年香港清潔行業回顧 (`2026-cleaning-industry-year-review`) | Year-end authority piece; also a natural place to internally link the whole year's new cluster content together |

Format for all 10: same structure used throughout this session — feature
snippet, TOC, table + checklist + quote-block, a first-person "我" personal
anecdote in the body, 2 FAQ with matching `FAQPage` schema, editor byline
box in the footer, and a Replicate-generated hero image (Chinese title text
typed directly into the prompt, never as `\u` escapes — verify the tool's
echoed decode before triggering, and inspect the downloaded image for
watermark hallucinations before merging).

## Open question for the next checkpoint

Posts #1–3 and #5–8 are new dedicated service pages — should these ship the
same way as the last 16 (write + merge directly to `main`, generate hero
image immediately) or go back through the `_drafts/` → `auto-publish.yml`
schedule so they land on their target weeks instead of all at once? The
Trust/EEAT entries (#4, #10) fit the existing drafts pipeline more naturally
since they're not tied to cluster cross-linking the way service pages are.
