# Content Planner — High-Priority Topical Clusters

Source material: `seo/scraped-content/*.txt` (existing clean.com.hk pages) is to be
REWRITTEN, not copied, into the supporting pages below. Each supporting page links
back to its pillar page and the pillar links out to all supporting pages
(hub-and-spoke internal linking).

Existing drafts already cover 2 of these slots — flagged inline so we don't
duplicate effort.

## Pillar 1: Office Cleaning (辦公室清潔) — cluster_id 1
Pillar page: `office-deep-cleaning.html` (exists, 2500+ impr, pos 70-90)

Supporting pages:
1. **辦公室清潔公司 / office cleaning company guide** — buyer's-guide comparison page,
   targets "辦公室清潔公司" (317 impr), "辦公室清潔服務" (210 impr)
2. **寫字樓包月清潔 / monthly-contract office cleaning** — targets "寫字樓包月清潔" (46),
   "包月清潔" (32) — commercial/recurring-revenue intent, high conversion value
3. **辦公室消毒服務 / office disinfection service page** — dedicated service page
   (currently only covered inside the pillar + the general 霧化消毒 blog),
   targets "辦公室消毒" (309 impr)
4. **辦公室地氈清洗指南** — ALREADY DRAFTED: `_drafts/2026-04-10-office-carpet-cleaning-guide.md`
   (currently orphaned — dated in the past, see auto-publish note below)
5. **地氈除臭 5 個方法** — ALREADY DRAFTED: `_drafts/2026-04-10-carpet-odor-removal-tips.md`
   (same orphaned-date issue)
6. **辦公室清潔價錢 2026** — ALREADY DRAFTED: `_drafts/office-cleaning-price-2026.md`
   (no date prefix at all — never auto-publishes under the current mechanism)

Net new to write: #1, #2, #3 (3 posts). #4-6 just need re-dating + republishing.

## Pillar 2: Bathroom Cleaning (浴室清潔) — cluster_id 2
Pillar page: `blog-post-bathroom-cleaning.html` (exists, only page with real clicks:
pos 10.4, 1681 impr, 23 clicks — the proof of concept)

Supporting pages:
1. **廁所清潔 / toilet-cleaning specific page** — cluster_id 5 in CSV, already shows
   good positions on tiny content (pos 4-11.75); dedicated page, not just a blog mention
2. **浴室磁磚縫除霉 / bathroom tile-grout mold removal** — bridges to the mold pillar
   below; matches the pillar's own "五大重點清潔區域" section 3
3. **淋浴間去水渠清潔 / bathroom drain unclogging** — pillar's FAQ Q4 already gestures
   at this as a related professional service; make it its own page
4. **浴室消毒服務 (dedicated service page)** — currently only exists as a blog
   post value-add inside the general disinfection blog; "浴室消毒" already ranks
   pos 6 on tiny content
5. **浴室深層清潔收費指南** — price-guide page (commercial intent, mirrors the
   office pricing page pattern which is a good format to reuse)

## Pillar 3: Kitchen Cleaning (廚房清潔) — cluster_id 3
Pillar page: `blog-post-kitchen-cleaning.html` (exists, second-best performer,
pos 6.6 on "香港 深層廚房清潔", no dedicated service page yet)

Supporting pages:
1. **抽油煙機拆洗服務 / range hood deep-clean** — the pillar calls this out as its
   own biggest pain point ("最容易被忽視的油污重災區"); strong standalone demand
2. **廚房水槽清潔 / kitchen sink deep cleaning** — direct GSC query match (6 impr,
   but pillar already surfaces sink as "細菌密度最高的廚房部位")
3. **雪櫃清潔消毒 / fridge cleaning & disinfection**
4. **廚房深層清潔收費指南** — price-guide page (same reusable format)
5. **食肆/餐廳隔油池清洗 / restaurant grease-trap cleaning** — B2B upsell bridging
   to cluster_id 15 (清洗隔油池), pairs kitchen cluster with a low-priority topic

## Pillar 4: Mold / Mildew Removal (除霉) — cluster_id 4 — NEW PILLAR
No existing page on either site. Build as a full pillar; pairs naturally with the
bathroom cluster (mold = bathroom's #1 pain point per the existing blog's own data).

Pillar page (new): **除霉服務完整指南 / Mold Removal Hong Kong — the complete guide**
targets "除霉公司" (153), "除霉服務價錢" (152), "除霉服務" (152)

Supporting pages:
1. **浴室除霉 / bathroom mold removal** — direct link from the bathroom pillar
2. **牆身天花除霉 / wall & ceiling mold removal** — common HK humidity complaint,
   distinct room context from bathroom
3. **冷氣機發霉清洗 / air-con mold & musty smell removal** — HK-specific seasonal
   pain point, high search-intent commercial angle
4. **除霉公司邊間好 / how to choose a mold-removal company + price benchmarks**
   — commercial-intent comparison page, targets "除霉公司推薦" (10), "除霉公司" (153)

## Cross-cutting notes
- Every new page above should include 2 FAQ entries (per Subagent 2 spec) and
  internal links: supporting page → pillar → other supporting pages in the same
  cluster, plus a cross-link between the Mold pillar and the Bathroom pillar.
- Reuse downloaded photos from `assets/service-photos/{slug}/` where the topic
  has an original-site photo (office, renovation, home-regular-cleaning, fogging,
  pest-control, floor, carpet-machine, steam) — see CSV `photo_download_status`.
  Bathroom, kitchen, mold, and toilet have no original-site photo and need new/stock
  images (flagged `needs_own_photo_*` in the CSV).
