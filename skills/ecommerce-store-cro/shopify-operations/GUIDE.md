Original description: Operating manual for managing a Shopify store through the connected Shopify MCP tools — orders, products, inventory, discounts, and analytics.

# Shopify Operations

Manage the store through the connected Shopify MCP tools. Everything the MCP exposes is in scope; theme *code* edits are not in the MCP — for those, give exact click-path instructions in the Shopify admin instead.

## Store context (fill in per store)

Ask only for what's missing: store domain · Hebrew RTL · currency ILS · brand color · theme · page builder · payment provider · reviews app · email/popups · abandoned cart · the product and the offer.

## Store rules

- Subscription products need the cancellation terms stated in plain Hebrew on the page itself, not only in the policy.

## Tool map — pick the right tool per job

| Job | Tools |
|---|---|
| Orders | list-orders → get-order (details, fulfillment, line items) |
| Products | search_products, get-product, create-product, update-product, bulk-update-product-status |
| Collections | search_collections, get-collection, create-collection, update-collection, add-to-collection |
| Inventory | get-inventory-levels, set-inventory |
| Discounts | create-discount |
| Customers | list-customers |
| Analytics | run-analytics-query (ShopifyQL) |
| Store info | get-shop-info |
| Anything not covered above | graphql_schema → graphql_query / graphql_mutation |

## Operating rules

1. **Read before write.** Always fetch current state (get-product / get-order / get-inventory-levels) before any update.
2. **Confirm before mutating.** Any change to the live store — price, product status, inventory, discounts, collections — show the user exactly what will change (before → after) and get a yes first. Read-only queries need no confirmation.
3. **GraphQL discipline.** For anything beyond the dedicated tools: explore with graphql_schema, draft the operation, run validate_graphql_codeblocks, only then execute. Use search_docs_chunks when API behavior is unclear.
4. **Copy standard.** Any product description, page copy, or discount messaging follows the copywriting-ads skill (highest professional standard, Hebrew, per avatar).

## ShopifyQL — ready patterns

```
FROM sales SHOW total_sales, orders, average_order_value BY day SINCE -30d
FROM sales SHOW total_sales BY product_title SINCE -30d ORDER BY total_sales DESC
FROM sessions SHOW sessions, conversion_rate BY day SINCE -14d
FROM sales SHOW total_sales BY referring_channel SINCE -30d
```
Adjust ranges/dimensions per question; prefer one focused query over dumping everything.

## Routine jobs (do these efficiently)

- **Daily check:** yesterday's sales + orders + AOV (one ShopifyQL query) → flag anomalies vs. trailing 7 days.
- **Order status question (from customer):** get-order by number → answer with concrete fulfillment status and days.
- **New offer/discount:** confirm % and constraints → create-discount → report the code back.
- **Product page update:** get-product → draft new copy per copywriting-ads → show diff → update-product after approval.
- **Stock check before scaling ads:** get-inventory-levels; warn if runway < expected ad-driven demand. On [products with an expiry date] watch the expiry date too, not just the count.
- **Subscription check:** how many active subscribers, churn after month 1 and after month [N] (month [N] is where the product proves itself, so churn before it is the real leak).

## Escalation (outside MCP)

Theme/Liquid code, page-builder sections, payment-gateway settings, reviews moderation, Klaviyo flows, abandoned-cart automations — give exact admin/app click-paths and, if code is needed, write it ready to paste.

## Connected skills

- **Design, layout and CRO decisions:** store-design-cro (same skill: `../store-design-cro/GUIDE.md`). Theme edits always go to the newest unpublished theme version, never the live theme.
- **Funnel numbers from ads:** copywriting-ads (part: meta-ads-analysis, Step 3).
- **Customer messages about orders:** whatsapp-customer-service (same skill: `../whatsapp-customer-service/GUIDE.md`).
