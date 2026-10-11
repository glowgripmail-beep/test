---
name: ecommerce-store-cro
description: "Use for designing, building, auditing or operating an e-commerce store (Shopify, Israel, Hebrew/RTL, mobile-first): product page, home page, cart, checkout, offer and bundles, trust, mobile, speed, Israeli regulation (accessibility, distance-sale cancellation, subscriptions, privacy, spam law), measurement and A/B testing, research-based with sources. Also for running a Shopify store through the Shopify MCP tools (orders, products, collections, inventory, discounts, customers, ShopifyQL analytics, GraphQL) and for reading and replying to WhatsApp customer messages (order status, complaints, returns, price objections, counterfeit worries, abandoned-cart outreach) in Israeli friend-not-brand tone. Hebrew triggers: עיצוב חנות, דף מוצר, דף בית, עגלה, צ'קאאוט, המרה, הצעה, מארזים, אמון, מובייל, מהירות, רגולציה, נגישות, שופיפיי, הזמנות, מלאי, הנחה, וואטסאפ, שירות לקוחות, איפה ההזמנה שלי, עגלה נטושה."
---

# E-commerce Store, CRO and Store Operations

One skill for everything that happens on and around the store itself: how the store should look and convert (research-based CRO knowledge for an Israeli Shopify store), how to operate it day to day through the Shopify MCP tools, and how to answer customers on WhatsApp.

Merged from three source skills. Each source lives in its own folder as `GUIDE.md`, kept close to verbatim:

| Part | Folder | What it is |
|---|---|---|
| store-design-cro | `store-design-cro/GUIDE.md` | Hebrew research knowledge base (sections 1-14) with evidence labels ([עובדה], [מקובל], [השערה], [לא אומת], [שנוי במחלוקת], [לבדוק]) and sources: site structure, product page, color and type, layout, consumer psychology on the store, trust, mobile, speed, checkout, AOV, Israeli accessibility and regulation, measurement, store observations, pre-launch checks. |
| shopify-operations | `shopify-operations/GUIDE.md` | Operating manual for the Shopify MCP tools: tool map, read-before-write and confirm-before-mutate rules, GraphQL discipline, ShopifyQL patterns, routine jobs, escalation outside the MCP, a default Israeli DTC app stack. |
| whatsapp-customer-service | `whatsapp-customer-service/GUIDE.md` | Playbook for WhatsApp customer conversations: ground rules, reply style, scenario playbook, what never to send, draft mode without a connection. |

Note: the store-design-cro text refers to the shopper as "היא / הלקוחה" (female). Adapt the gender to the actual store's audience. Niche examples were replaced with [bracketed placeholders]; fill them from the actual store.

## Which part to read when

| Task | Read |
|---|---|
| Plan or build the store structure (home, collection, product page, cart drawer, post-purchase offer, thank-you page) | `store-design-cro/GUIDE.md` section 1 |
| Build or audit a product page (first screen, gallery, price and offer, add-to-cart button, reviews, section order) | `store-design-cro/GUIDE.md` section 2 |
| Colors, contrast, typography, Hebrew fonts, RTL and bidi | `store-design-cro/GUIDE.md` section 3 |
| Layout, spacing, scanning patterns, accordions vs tabs, touch zones | `store-design-cro/GUIDE.md` section 4 |
| Persuasion on the store (social proof, honest scarcity, anchoring, price display, bundles and defaults, risk reversal, objections) | `store-design-cro/GUIDE.md` section 5 (deeper theory: consumer-psychology-audience-research) |
| Trust for Israeli shoppers | `store-design-cro/GUIDE.md` section 6 |
| Mobile-first, in-app browsers, forms | `store-design-cro/GUIDE.md` section 7 |
| Speed, Core Web Vitals, images, video, fonts, app scripts | `store-design-cro/GUIDE.md` section 8 |
| Checkout, fields, cost transparency, Israeli payment providers, subscriptions on Shopify, abandoned carts | `store-design-cro/GUIDE.md` section 9 |
| Raising AOV (quantity tiers, subscription, free-shipping threshold, cross-sell, post-purchase offer, gifts) | `store-design-cro/GUIDE.md` section 10 |
| Israeli accessibility law, consumer protection (distance sales, cancellation), ongoing transactions, privacy (Amendment 13), spam law, reviews and sale pricing | `store-design-cro/GUIDE.md` section 11 |
| Funnel metrics, GA4 events, Clarity, A/B test sample sizes, testing tools | `store-design-cro/GUIDE.md` section 12 |
| What observed stores do, what not to copy from big brands | `store-design-cro/GUIDE.md` section 13 |
| Pre-launch checklist (payments provider, regulatory consultant, lawyer) | `store-design-cro/GUIDE.md` section 14 |
| Any action in the Shopify admin via MCP (orders, products, inventory, discounts, collections, customers, analytics, GraphQL) | `shopify-operations/GUIDE.md` |
| Daily sales check, order status lookup, new discount, product page update, stock check before scaling ads, subscription churn check | `shopify-operations/GUIDE.md` "Routine jobs" |
| Theme/Liquid code, page builder, payment gateway, Klaviyo flows (outside the MCP) | `shopify-operations/GUIDE.md` "Escalation" |
| Reply to a customer on WhatsApp (order status, product question, price objection, return/cancellation, counterfeit worry, abandoned cart) | `whatsapp-customer-service/GUIDE.md` |

Related skills: copy for pages and messages: copywriting-ads; funnel leaks from ads: copywriting-ads (part: meta-ads-analysis); psychology, research and Israeli audience: consumer-psychology-audience-research; visual design direction: ui-web-design and image-generation-branding; funnel diagrams: documents-files-diagrams (part: archify).

## Conflicts between sources

Not resolved here. Each side is labeled by source.

1. **Abandoned-cart sequence.** store-design-cro (section 9, Klaviyo email benchmark): reminder after 2 to 4 hours, offer after 24, last one after 48. whatsapp-customer-service: one personal message, one follow-up max after 24h, then stop. (Different channels, but the cadence differs.)
2. **WhatsApp abandoned-cart outreach.** whatsapp-customer-service prescribes it as a routine scenario. store-design-cro: WhatsApp cart recovery is [לא אומת] (only vendor blogs) and whether the spam law applies to WhatsApp and abandoned-cart reminders is [לבדוק] (section 11, section 14 lawyer list). shopify-operations recommends Flashy (WhatsApp and SMS) for abandoned carts.
3. **Payments provider.** shopify-operations recommends PayPlus as the default gateway (installments, Bit). store-design-cro: with PayPlus, Apple Pay, Google Pay and Bit go through a redirect and need an extra app; Shopify subscriptions require Shopify Payments, PayPal Express, Authorize.net, Adyen or Stripe, so subscription support must be verified with the gateway before building an offer around a subscription.
4. **Theme.** shopify-operations recommends Shrine ("RTL works"). store-design-cro: the Horizon family supports Hebrew; any other theme must be verified, and checkout Hebrew translation is [לא אומת].
5. **Cancellation right.** whatsapp-customer-service: "the 14-day cancellation right is law — honor it without friction". store-design-cro section 11: 14 days from receiving the product or the disclosure document, whichever is later; cancellation fee 5% or 100 ₪, whichever is lower; refund within 14 days; 4 months for people 65+, people with disabilities and new immigrants when the deal included a conversation with the business ([לבדוק], may include WhatsApp sales chats).
6. **Precedence claim.** store-design-cro states that for anything store- or design-related it overrides consumer-psychology and israeli-audience (now in consumer-psychology-audience-research) because it has sources, and that design skills only give visual direction while it wins on conversion, trust, RTL, mobile and accessibility.
