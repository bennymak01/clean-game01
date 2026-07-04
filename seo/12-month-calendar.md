# 12-Month Blog Publishing Calendar (2026-07 → 2027-06)

Cadence: 2 posts/month (24 posts/year), front-loaded by CSV priority + GSC
opportunity score (impressions × 1/position). Uses the existing `_drafts/` →
`auto-publish.yml` → `blog/YYYY-MM-DD-slug/` pipeline already in this repo.

**Bug found & fixed**: `auto-publish.yml` only publishes drafts whose filename
starts with the *current* date, inside a hardcoded `2026-06-13`–`2026-07-23`
window. Three already-written drafts were orphaned by this:
- `_drafts/2026-04-10-office-carpet-cleaning-guide.md` (dated in the past)
- `_drafts/2026-04-10-carpet-odor-removal-tips.md` (dated in the past)
- `_drafts/office-cleaning-price-2026.md` (no date prefix at all)

Fix applied: re-dated all three into this calendar's near-term slots, and
removed the hardcoded end-date cap so the workflow keeps running for the
full 12 months instead of stopping 2026-07-23. See diff in
`.github/workflows/auto-publish.yml`.

| # | Publish date | Cluster | Slug / working title | Status |
|---|---|---|---|---|
| 1 | 2026-07-09 | Office (pillar support) | 辦公室地氈清洗指南 (`office-carpet-cleaning-guide`) | existing draft, re-dated |
| 2 | 2026-07-16 | Office (pillar support) | 地氈有異味？5個除臭方法 (`carpet-odor-removal-tips`) | existing draft, re-dated |
| 3 | 2026-07-23 | Mold (new pillar) | 除霉服務完整指南：香港除霉公司點揀？ | new |
| 4 | 2026-07-30 | Office (pillar support) | 辦公室清潔價錢全攻略 2026 (`office-cleaning-price-2026`) | existing draft, re-dated |
| 5 | 2026-08-06 | Bathroom (pillar support) | 廁所清潔完整指南 | new |
| 6 | 2026-08-13 | Mold (pillar support) | 浴室磁磚縫除霉 | new |
| 7 | 2026-08-20 | Kitchen (pillar support) | 抽油煙機拆洗服務指南 | new |
| 8 | 2026-08-27 | Office (pillar support) | 辦公室消毒服務 | new |
| 9 | 2026-09-03 | Mold (pillar support) | 牆身天花除霉 | new |
| 10 | 2026-09-10 | Bathroom (pillar support) | 浴室消毒服務 | new |
| 11 | 2026-09-17 | Trust/EEAT (series) | 清潔公司如何處理客訴？ | new |
| 12 | 2026-09-24 | Office (pillar support) | 寫字樓包月清潔 | new |
| 13 | 2026-10-01 | Kitchen (pillar support) | 廚房水槽清潔 | new |
| 14 | 2026-10-08 | Mold (pillar support) | 冷氣機發霉清洗 | new |
| 15 | 2026-10-15 | Bathroom (pillar support) | 浴室去水渠清潔 | new |
| 16 | 2026-10-22 | Office (pillar support) | 辦公室清潔公司比較指南 | new |
| 17 | 2026-11-05 | Kitchen (pillar support) | 雪櫃清潔消毒 | new |
| 18 | 2026-11-19 | Mold (pillar support) | 除霉公司邊間好？收費比較 | new |
| 19 | 2026-12-03 | Home regular cleaning (medium) | 家居定期大掃除完整指南 | new |
| 20 | 2026-12-17 | Bathroom (pillar support) | 浴室深層清潔收費指南 | new |
| 21 | 2027-01-14 | Disinfection (medium) | 家居消毒服務指南 | new |
| 22 | 2027-02-11 | Pest control (medium) | 滅蟲服務完整指南 | new |
| 23 | 2027-03-11 | Kitchen (pillar support) | 廚房深層清潔收費指南 | new |
| 24 | 2027-04-08 | Low-priority topics (batch) | 玻璃窗/吸水服務/隔油池 topical-authority page | new |

Trust/EEAT series (`accountability`, `communication`, `relocation`, `punctuality`,
`professional-cleaning-qualities`) continues interspersed roughly monthly to
keep author-authority signals fresh — slot #11 above is the next one; more can
be added as capacity allows without displacing the cluster-priority posts.

Office cleaning (highest impressions, worst position) gets steady content
investment above but — per Subagent 3's mandate — should NOT be assumed to
close on content alone; see `seo/gsc-analysis.md` (produced in the Subagent 3
pass) before committing paid/backlink budget to it.
