<!-- from: meta-ads-analysis/SKILL.md (frontmatter removed) -->

Original description: The complete methodology for reading, diagnosing and acting on Meta Ads data for direct-response eCommerce — tracking, profit math, funnel diagnosis, creative reading, and kill/keep/scale decisions. Profit-first, never vanity metrics.

# Meta Ads Data Analysis

Operating system for reading Meta Ads data.

## The one thing that governs everything

**Meta optimizes for predicted optimization events. You optimize for profit.**
These are different objectives. Every "weird" Meta behavior (funding a zero-purchase ad, starving a good creative, unequal spend) comes from this gap. Your job is to translate Meta's numbers into profit decisions and to overrule Meta when they conflict.

Auction winner = **Total Value = Bid × Estimated Action Rate + Ad Quality**.
Highest bid does not win. Better creative → higher predicted action rate → cheaper delivery.

## Mandatory order of operations

Never skip, never reorder. Answering out of order produces wrong advice.

1. **Tracking** — is the data real?
2. **Profit** — are we above break-even?
3. **Funnel** — where is the leak (ad-side or store-side)?
4. **Creative** — which creative/hook/angle is responsible?
5. **Decision** — kill / keep / scale / test next.

If step 1 fails, stop and fix tracking. Do not judge any ad on broken data.

## Step 1 — Tracking sanity check

Before analyzing anything, confirm:
- Pixel **and** CAPI both firing ViewContent / ATC / IC / Purchase.
- Deduplication working: Meta Purchases must NOT be ~2× Shopify orders.
  Dedup key = `event_name` + `event_id`, 48h window, browser favored within 5 min.
- Event Match Quality on Purchase ≥ 7.
- `value` present, `currency` = **ILS**, correct amount.
- One Pixel, correct dataset, domain verified, no test events in production.
- Purchase fires once (not on refresh, not on upsell pages).

**Stable Meta-vs-Shopify gap = normal attribution. Sudden gap = a bug.**

## Step 2 — Profit math (do this before touching any ad)

```
Contribution margin = price − VAT − COGS − shipping − payment fees − app fees − refunds − discounts
Break-even ROAS = 1 ÷ contribution margin
Break-even CPA  = contribution margin in ₪ per order
Profit per order = (AOV × margin%) − CPA
```
Israel: prices are VAT-inclusive → **VAT = price ÷ 1.18 × 0.18** (18%). Strip it before ROAS.
**If the business owner is an עוסק פטור:** VAT is **not** stripped from the price (copywriting-ads, ../references/offers-pricing-unit-economics.md). Recheck when approaching the annual turnover ceiling.
Meta reports **gross, pre-refund** revenue. Shopify is financial truth.

Margin → break-even ROAS: 60% → 1.67x · 50% → 2.0x · 40% → 2.5x · 30% → 3.33x.

Set **target** CPA/ROAS below/above break-even by the profit goal. Every kill/keep/scale call is measured against these two numbers, never against a benchmark from the internet.

## Step 3 — Funnel diagnosis

Walk top-down and find the **first ratio that collapses** vs. this account's own baseline.

| Ratio | Formula | If low → |
|---|---|---|
| Impression→Click (CTR) | clicks ÷ impr | hook / creative / audience |
| Click→LPV | LPV ÷ outbound clicks | page speed, tracking, accidental clicks (<70–80% = investigate) |
| LPV→ViewContent | VC ÷ LPV | landing page mismatch or VC misfire |
| LPV→ATC | ATC ÷ LPV | product page / offer / price |
| ATC→IC | IC ÷ ATC | cart friction, shipping surprise |
| IC→Purchase | Purch ÷ IC | payment gateway, trust, VAT display, checkout UX |
| LPV→Purchase | Purch ÷ LPV | ≈ site conversion rate |

**Ad-side problem** = leak above LPV. **Store-side problem** = leak below LPV.
Never rewrite creative for a checkout problem, and never fix checkout for a hook problem.

## Step 4 — Creative reading

| Stage | Metric |
|---|---|
| Scroll-stop | Hook Rate = 3s views ÷ impressions (healthy ~20–40%; <20% hook failed) |
| Held attention | Hold Rate = ThruPlay ÷ 3s views (pick ONE definition, keep it consistent) |
| Click intent | Outbound CTR |
| Product interest | LPV, ViewContent, ATC |
| Purchase intent | IC, AddPaymentInfo |
| Conversion | Purchases, CPA, ROAS, contribution profit |

Failure isolation:
- Low hook rate → **hook failed**
- Good hook, steep mid-drop, low CTR → **body/script failed**
- Good CTR + ATC, low purchase → **offer or store failed**
- Good IC, low purchase → **checkout/payment failed**

## Step 5 — Kill / keep / scale

Read by **spend as a multiple of target CPA**, not by days.

| Spend | Look at | Lean |
|---|---|---|
| 0.25× | CPM, hook rate | keep — far too early |
| 0.5× | CTR, CPC, LPV, ATC, IC | live funnel → keep · dead funnel + weak CTR → lean kill |
| 1× | purchases + funnel | 0 purchases + dead funnel → kill · 0 purchases + live funnel → hold, check store |
| 1.5× | CPA trend | 0 + weak funnel → kill · trending to target → keep |
| 2× | CPA vs break-even | 0 purchases → kill (unless tracking broken) |
| 3× | confident read | below break-even → scale · above → kill |

Decision tree:
```
Tracking healthy? ── No → fix tracking, judge nothing
        │ Yes
Enough spend (≥1× target CPA)? ── No → leading indicators only, DO NOT kill
        │ Yes
Any purchases? ── No → Any ATC? ── No → Good LPV/VC?
        │                    │            ├ No  → speed/tracking/traffic quality
        │                    │            └ Yes → product page / offer / price
        │                    └ Yes → Any IC? ── No  → cart friction / shipping
        │                                      └ Yes → payment / trust / VAT / tracking
        └ Yes → CPA vs break-even?
                 ├ above → improving? yes: hold · no: kill
                 └ below → keep; if stable → scale 10–20% or duplicate horizontally
```

## Sample size discipline (non-negotiable)

- Do **not** declare purchase-level winners/losers under **~10–15 conversions** per variant.
- ₪80 spend, 0 purchases → one sale makes CPA ₪80 instantly. Early numbers are noise.
- CPM / CTR / CPC / hook rate stabilize around 2,000–8,000 impressions. ROAS does not.
- Single-day swings (5 sales @ ₪20, then 1 @ ₪90) are **normal**. Decide on trailing 3–7 days.
- Regression to the mean is real: day-1 stars fade, day-1 duds recover.
- Breakdown cells (age/gender/region) with 1–2 purchases are noise — never act on them.

## Why Meta funds a "losing" ad

Exploration vs exploitation · statistical uncertainty · higher predicted action rate from early engagement · cheaper auction pockets · delayed attribution & iOS reporting lag (~72h) · modeled conversions · different audience pockets · incremental/marginal return.
Meta is not broken — it is optimizing to its objective under uncertainty. Impose profit discipline yourself.

Corollary: **5 ads in one ad set ≠ 20% each.** For a fair creative test use **ABO, one concept per ad set, equal budgets, consistent format per ad set**. CBO/ASC = scaling, not testing.

## Small-budget rules (default for a small brand)

- One simple prospecting campaign, **broad / Advantage+ Audience**, Israel geo, Hebrew creative, **Advantage+ Placements**. Few ad sets — fragmentation kills small budgets.
- Learning phase: ~50 events/7 days in the UI, but since **June 2024** the practical threshold for Purchase campaigns is **~10/week**. A profitable ad set can stay "Learning Limited" forever — **do not kill on the label.**
- If under ~10 weekly purchases per ad set, optimize a **proxy event** (ATC or IC) to build signal, then switch back to Purchase.
- Test budget: enough for ~2–3 conversions/day per test ad set; ~8–10k impressions before judging.
- Scale **10–20%** steps, or **horizontally** (duplicate winners) — better on small budgets.
- Stop editing constantly. Significant edits (optimization event, big budget/bid/audience/creative changes) reset learning.

## Attribution facts to state correctly

- Default = **7-day click + 1-day view**. **7-day-view and 28-day-view were removed Jan 12, 2026.**
- Conversions report on **impression/click date** → yesterday's ROAS keeps rising for days.
- Saw-but-didn't-click, bought 3 days later → **Meta gives no credit** (view window is 1 day).
- Clicked, bought 3 days later → **Meta credits the ad** (7-day click).
- Attribution ≠ incrementality. Retargeting ROAS is inflated; only a holdout proves lift.

Source of truth: **Revenue/orders → Shopify · which creative to scale → Meta · overall efficiency → blended MER (total revenue ÷ total ad spend).**

## Fatigue (needs the whole cluster, not one metric)

Real fatigue = frequency ↑ **and** CPM ↑ **and** CTR ↓ **and** CVR ↓ **and** CPA ↑ over a 7-day window. Rising frequency alone on broad audiences is not fatigue. Fix order: hook → creative → offer → broaden audience.

## Common diagnostic scenarios

| Symptom | Likely cause | Action |
|---|---|---|
| High CTR, many ATC, few purchases | checkout/offer/trust leak, or ATC misfiring | check ATC→IC→Purchase and dedup; don't call it a winner on ATC |
| Low CTR, expensive CPC, good ROAS | ad pre-qualifies hard | keep/scale; don't kill for low CTR |
| Great hook rate, cheap clicks, 0 purchases | entertaining hook, no buying intent | kill — the classic trap |
| Good clicks, LPV under 70% | page speed or tracking | speed test; don't blame creative |
| Meta ≈ 2× Shopify orders suddenly | dedup broke | Events Manager + recent theme/app/CAPI changes |
| Learning Limited but profitable | budget below threshold | keep; consolidate or use a proxy event |
| Winner dies right after doubling budget | learning reset / volatility | revert or wait ~72h; scale 10–20% next time |
| Retargeting 8x, prospecting 1.8x | retargeting likely non-incremental | holdout test; grow prospecting, keep retargeting lean |
| Everything green but losing money | vanity metrics masking unit economics | manage to contribution margin and MER |

## Custom metrics to build in Ads Manager

Hook Rate · Hold Rate · Outbound CTR · Click→LPV% · LPV→ATC% · ATC→IC% · IC→Purchase% · LPV→Purchase% · Revenue per LPV · Revenue per Click · Cost per ATC · Cost per IC · Profit per Purchase · Contribution Profit · Break-even ROAS · Break-even CPA.

Column presets: **Daily Overview · Creative Testing · Funnel Diagnosis · Scaling · Video Analysis**.

## Daily process

1. Tracking + Shopify revenue sane? 2. Above break-even on 3–7 days? 3. Which ads beat/miss break-even CPA with enough spend? 4. First collapsed funnel ratio on the losers? 5. Hook/CTR on new tests with enough impressions? 6. Decide — few changes, no needless resets.

## Weekly process

Winners/losers by contribution profit → tag hook/angle/avatar/format → which angles repeat → site CVR vs Meta LPV→Purchase → fatigue cluster check → scale candidates → next test batch. Keep the creative log so learning compounds.

## Hard rules

- Never rank creatives by ATC count, CTR, or CPM. Rank by CPA / contribution profit.
- Never kill on one bad day. Never scale on one good day.
- Never trust ROAS on <10 purchases.
- Never blame creative for a checkout problem (or vice versa).
- Never present benchmarks as targets — build baselines from this account's trailing 30 days.
- Never claim to know Meta's internal model. Mark inference as inference.

## Response style

Short, direct, practical. Lead with the verdict (kill / keep / scale / fix X), then the reason, then the number that proves it. No lectures unless he asks for depth. Hebrew unless the user writes in English. Any ad copy produced along the way follows copywriting-ads (../references/hebrew-dr-copy.md and ../references/dr-methodology.md); brand facts, avatars and angles come from [the business's own research and brand documents], and product and offer facts from [the business's current dated product and offer sheet].

## Connected skills

- **Next creative batch:** copywriting-ads (part: ad-vision-writing) for visions (../ad-vision-writing/GUIDE.md), copywriting-ads (../references/hebrew-dr-copy.md) for copy.
- **Competitor ads from a link:** video-production (part: watch) (Claude Code only).
- **Diagnosing why a creative failed:** consumer-psychology-audience-research (part: consumer-psychology) ("How to use in creative testing").
- **Store-side leaks (below LPV):** ecommerce-store-cro (part: store-design-cro) for the page, ecommerce-store-cro (part: shopify-operations) for store data.
