# Competitor Analysis (Subagent 2, step 4)

Source: `seo/competitor-scrape/*-text.txt` (scraped via `seo-competitor-scrape.yml`,
since this sandbox can't reach external sites directly).

## chungshing-cleaning.com (忠誠清潔服務有限公司)
- Single-page Wix site, English label "Office cleaning" in the title tag but content
  is 100% Chinese, 100% office-cleaning focused (寫字樓包月清潔 - monthly-contract
  office cleaning).
- Positioning: "30 years trustworthy", transparent flat-rate pricing by area,
  no hidden fees, staff insured (MPF + 3rd party liability) - a trust/EEAT angle
  worth matching (we don't currently state insurance/MPF status anywhere).
  Directly validates row 1's "寫字樓包月清潔" (monthly-contract office cleaning)
  supporting-page recommendation in `content-planner.md`.
- Structurally weak: single page, no blog, no FAQ schema, no topical depth at all.
  Confirms this competitor is NOT a structural threat - still good to reference
  for their pricing-transparency messaging.

## globaltophk.com (GTS Professional)
- Much stronger structurally: dedicated service pages per category (not a single
  page) - Office Cleaning, Carpet Cleaning and Maintenance, Pest Management,
  Daily Cleaning, Air System/FCU Cleaning & Sterilization, Formaldehyde Removal,
  Marble Restoration & Maintenance, Vinyl/Wooden Floor Cleaning, plus named
  branded add-ons (Buckeye disinfection spray, SD Labs Anti-Virus coating,
  Scotchgard carpet/upholstery protector).
- Bilingual EN/中 toggle, B2B-facing tone (client list page = social proof).
- **Structural takeaway**: this is the hub-and-spoke dedicated-page-per-service
  model already planned in `content-planner.md` - good validation of that approach.
- **Content gaps to borrow**:
  - Formaldehyde removal (甲醛) - adjacent to our disinfection cluster, not
    currently in our CSV at all. Low-effort addition once High-priority
    clusters are built out.
  - Air system / fan coil unit cleaning - adjacent to our office cleaning
    cluster's "冷氣出風口" mention, not its own page for us yet.
  - Carpet/upholstery protective coating (Scotchgard-style) as a carpet-cluster
    upsell page, pairs with cluster_id 11.
  - Marble/stone restoration - overlaps cluster_id 10 (floor machine cleaning)
    but is positioned as a premium add-on, not just cleaning.

## Verdict on the original two candidates
Both are still reasonable references: chungshing for pricing-transparency
messaging (weak structurally, easy to out-rank), globaltophk for topical
structure to emulate (the stronger site, worth tracking for backlink/authority
comparison once office-cleaning cluster investment starts).
