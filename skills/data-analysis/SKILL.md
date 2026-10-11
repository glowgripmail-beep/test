---
name: data-analysis
description: "Data analysis toolkit. Use when answering data questions (quick metric lookup, what's driving a trend or drop, segment comparisons, formal stakeholder report); writing, optimizing, debugging or translating SQL for Snowflake, BigQuery, Databricks, PostgreSQL, Redshift, MySQL, etc. (CTEs, window functions, cohorts, funnels); profiling a new table or file (nulls, distributions, duplicates); statistics (trends, outliers, anomalies, hypothesis tests, significance, correlations); Python charts with matplotlib, seaborn or plotly (chart choice, accessibility, color, interactive); self-contained HTML dashboards with KPI cards, filters and tables; QA of an analysis before sharing (methodology, accuracy, bias); or creating/improving a company-specific data context skill (\"Create a data context skill\", \"Set up data analysis for our warehouse\", \"Add context about [domain]\"). Covers /analyze, /write-query, /explore-data, /create-viz, /build-dashboard, /validate-data."
---

# Data Analysis

One skill for the full analyst workflow: get the data (SQL), understand it (exploration), analyze it (questions + statistics), show it (charts + dashboards), check it (validation), and teach Claude a company's warehouse (data-context skill builder).

Each original source is kept complete in its own folder as `GUIDE.md` (its original description is the first paragraph). Read only the part(s) the task needs.

Placeholders such as `~~data warehouse` are explained in [CONNECTORS.md](CONNECTORS.md). License: [LICENSE](LICENSE) (Apache 2.0, from the source plugin).

## Routing: task -> file to read

| Task | Read |
|---|---|
| **Quick lookup** — a single number, a simple filter, a factual question ("How many users signed up last week?") | [analyze/GUIDE.md](analyze/GUIDE.md) (complexity level "Quick answer") |
| **Full analysis** — what's driving a trend or drop, segment comparisons over time | [analyze/GUIDE.md](analyze/GUIDE.md), plus [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) for the methods |
| **Formal report** for stakeholders (methodology, caveats, recommendations) | [analyze/GUIDE.md](analyze/GUIDE.md), then [validate-data/GUIDE.md](validate-data/GUIDE.md) (incl. its Analysis Documentation Template) |
| **Write a SQL query** from a natural-language need (workflow: requirements, dialect, schema discovery, best practices, presentation) | [write-query/GUIDE.md](write-query/GUIDE.md) |
| **Dialect syntax** — date/string/JSON/array functions and performance tips | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) "Dialect-Specific Reference" |
| ...PostgreSQL (Aurora, RDS, Supabase, Neon) | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) § PostgreSQL; compact cheat-sheet in [data-context-extractor/references/sql-dialects.md](data-context-extractor/references/sql-dialects.md) § PostgreSQL / Redshift |
| ...Snowflake | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) § Snowflake; [sql-dialects.md](data-context-extractor/references/sql-dialects.md) § Snowflake (safe division `DIV0`, `SELECT * EXCLUDE`) |
| ...BigQuery | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) § BigQuery; [sql-dialects.md](data-context-extractor/references/sql-dialects.md) § BigQuery (`SAFE_DIVIDE`, `SELECT * EXCEPT`) |
| ...Redshift | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) § Redshift; [sql-dialects.md](data-context-extractor/references/sql-dialects.md) § PostgreSQL / Redshift |
| ...Databricks / Spark SQL | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) § Databricks SQL (Delta Lake); [sql-dialects.md](data-context-extractor/references/sql-dialects.md) § Databricks / Spark SQL |
| ...MySQL | Only in [data-context-extractor/references/sql-dialects.md](data-context-extractor/references/sql-dialects.md) § MySQL |
| ...SQL Server, DuckDB, SQLite | Listed as supported dialects in [write-query/GUIDE.md](write-query/GUIDE.md) step 2, but no source has a dialect reference for them |
| ...cross-dialect basics (current date, concat, coalesce...) | [sql-dialects.md](data-context-extractor/references/sql-dialects.md) "Common Patterns Across Dialects" |
| **SQL patterns** — window functions, CTEs, cohort retention, funnel, deduplication | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) "Common SQL Patterns" |
| **Debug a failing query** | [sql-queries/GUIDE.md](sql-queries/GUIDE.md) "Error Handling and Debugging" |
| **Explore / profile a new table or file** (shape, nulls, cardinality, quality, relationships) | [explore-data/GUIDE.md](explore-data/GUIDE.md) |
| Schema discovery queries / documenting a table for the team / lineage | [explore-data/GUIDE.md](explore-data/GUIDE.md) "Schema Understanding and Documentation" |
| **Statistics** — central tendency, spread, percentiles, distributions | [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) "Descriptive Statistics Methodology" |
| Trends, growth rates, seasonality, simple forecasting | [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) "Trend Analysis and Forecasting" |
| Outliers / anomaly detection (z-score, IQR, percentile, time series) | [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) "Outlier and Anomaly Detection" |
| A/B tests, significance, which test to use, sample size | [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) "Hypothesis Testing Basics" |
| When to be cautious about claims (causation, multiple comparisons, Simpson's paradox...) | [statistical-analysis/GUIDE.md](statistical-analysis/GUIDE.md) last section, and [validate-data/GUIDE.md](validate-data/GUIDE.md) "Common Data Analysis Pitfalls" |
| **Make a chart now** from query results / a DataFrame (step-by-step command workflow) | [create-viz/GUIDE.md](create-viz/GUIDE.md) |
| **Chart choice, design principles, accessibility, code patterns** (line, bar, histogram, heatmap, small multiples, plotly, number formatting) | [data-visualization/GUIDE.md](data-visualization/GUIDE.md) |
| **Dashboard** — self-contained interactive HTML with KPI cards, Chart.js charts, filters, sortable table | [build-dashboard/GUIDE.md](build-dashboard/GUIDE.md) |
| **Validate / QA an analysis** before sharing (checklist, pitfalls, sanity checks, confidence rating) | [validate-data/GUIDE.md](validate-data/GUIDE.md) |
| **Build a company data-context skill** (bootstrap: discover schemas, interview analysts, generate skill) | [data-context-extractor/GUIDE.md](data-context-extractor/GUIDE.md) "Bootstrap Mode" + [references/skill-template.md](data-context-extractor/references/skill-template.md), [references/sql-dialects.md](data-context-extractor/references/sql-dialects.md), [references/domain-template.md](data-context-extractor/references/domain-template.md), [references/example-output.md](data-context-extractor/references/example-output.md) |
| **Improve an existing data-context skill** (add a domain, metrics, tables, terminology) | [data-context-extractor/GUIDE.md](data-context-extractor/GUIDE.md) "Iteration Mode" + [references/domain-template.md](data-context-extractor/references/domain-template.md) |
| Package the generated data-context skill as a zip | `python data-context-extractor/scripts/package_data_skill.py <path/to/skill-folder> [output-directory]` ([script](data-context-extractor/scripts/package_data_skill.py)) |

Typical end-to-end chain: `explore-data` -> `write-query` (+ `sql-queries`) -> `analyze` (+ `statistical-analysis`) -> `create-viz` / `data-visualization` or `build-dashboard` -> `validate-data`.

For chart design in other media (HTML/React artifacts, SVG, d3, Recharts, stat tiles), the separate system skill `dataviz` also applies; it is not part of this skill.

## Former slash commands

Six sources were slash commands (they had an `argument-hint`). This merged skill has no commands of its own; when a user types one of these, follow the matching GUIDE:

| Command (as the user may type it) | Argument hint | Follow |
|---|---|---|
| `/analyze <natural language question>` | `<question>` | [analyze/GUIDE.md](analyze/GUIDE.md) |
| `/write-query <description of what data you need>` | `<description of what data you need>` | [write-query/GUIDE.md](write-query/GUIDE.md) |
| `/explore-data <table_name or file>` | `<table or file>` | [explore-data/GUIDE.md](explore-data/GUIDE.md) |
| `/create-viz <data source> [chart type] [additional instructions]` | `<data source> [chart type]` | [create-viz/GUIDE.md](create-viz/GUIDE.md) |
| `/build-dashboard <description of dashboard> [data source]` | `<description> [data source]` | [build-dashboard/GUIDE.md](build-dashboard/GUIDE.md) |
| `/validate-data <analysis to review>` | `<analysis to review>` | [validate-data/GUIDE.md](validate-data/GUIDE.md) |

Three sources were background knowledge only (`user-invocable: false`): `sql-queries`, `data-visualization`, `statistical-analysis`. `data-context-extractor` was a model-invoked skill with two modes (Bootstrap / Iteration).

## Overlaps between sources

- **create-viz vs data-visualization**: both cover chart-type selection tables, matplotlib/seaborn/plotly code, and design rules (color, typography, layout, accuracy). `create-viz` is the step-by-step command workflow (get data -> pick chart -> generate -> save PNG -> present code and variations); `data-visualization` is the deeper reference (more chart types with alternatives, "When NOT to use" list, more code patterns, accessibility checklist).
- **write-query vs sql-queries vs data-context-extractor/references/sql-dialects.md**: `write-query` is the workflow and general best practices; `sql-queries` is the per-dialect function reference + patterns + debugging; `sql-dialects.md` is a compact per-dialect cheat-sheet meant to be pasted into a generated company skill (and the only source with MySQL notes).
- **analyze step 4 vs validate-data**: `analyze` has a 5-item quick validation (row count, nulls, magnitude, trend continuity, aggregation); `validate-data` is the full QA checklist, pitfall catalog and confidence rating.
- **validate-data vs statistical-analysis**: both describe survivorship bias, Simpson's paradox, correlation vs causation, small samples and multiple testing/cherry-picking.
- **explore-data vs data-context-extractor**: both give a table-documentation template (explore-data "Schema Documentation Template"; data-context-extractor "Reference File Standards" and `references/domain-template.md`) and schema-discovery SQL (explore-data: PostgreSQL `information_schema`; data-context-extractor: BigQuery/Snowflake).
- **build-dashboard vs create-viz/data-visualization**: dashboards use Chart.js (JavaScript) in one HTML file; the other two use Python. The dashboard CSS accent colors (`#4C72B0`, `#DD8452`, `#55A868`, `#C44E52`, `#8172B3`, `#937860`) are the same as data-visualization's `PALETTE_CATEGORICAL`.
- **Number formatting** appears three times: create-viz code comments, data-visualization `format_number()` (Python), build-dashboard `formatValue()` (JavaScript).

## Conflicts between sources (not resolved — each side labeled)

1. **Dual-axis charts**
   - create-viz: "Two-variable comparison over time" -> "Dual-axis line or grouped bar" (recommended).
   - data-visualization: "Dual-axis charts: Use cautiously. They can mislead by implying correlation. Clearly label both axes if used."
2. **Default color palette**
   - create-viz: `sns.set_palette("husl")`, while also saying "Use a consistent, colorblind-friendly palette".
   - data-visualization: explicit colorblind-friendly `PALETTE_CATEGORICAL = ['#4C72B0', ...]` and `sns.color_palette("colorblind")`; "Avoid red/green only".
3. **Doughnut / donut charts**
   - build-dashboard: "Doughnut chart: Composition (when <6 categories)" as a standard dashboard pattern.
   - data-visualization: "Donut charts: Slightly better than pie charts but same fundamental issues. Use for single KPI display at most."
4. **Pie / part-to-whole**
   - create-viz: "Stacked bar or area chart (avoid pie charts unless <6 categories)".
   - data-visualization: pie charts "Avoid unless <6 categories and exact proportions matter less than rough comparison ... Use bar charts instead"; part-to-whole -> stacked bar, alternatives treemap / waffle (area chart listed for trend/composition over time instead).
5. **Line-chart baseline**
   - build-dashboard `createLineChart`: `y: { beginAtZero: true }` always.
   - data-visualization: "Line charts can have non-zero baselines: When the range of variation is meaningful" (create-viz and data-visualization both require zero only for bar charts).
6. **Showing the chart**: create-viz code ends with `plt.savefig(...)` then `plt.show()`; data-visualization patterns only `plt.savefig(...)` (plotly examples use `fig.show()`).
7. **Large-number formatting**: data-visualization `format_number()` has a billions tier (`$1.2B`); build-dashboard `formatValue()` stops at millions (`M`).
8. **Redshift date difference**
   - sql-queries § Redshift: `DATEDIFF(day, start_date, end_date)`.
   - data-context-extractor `sql-dialects.md` § PostgreSQL/Redshift (combined): `DATE_PART('day', end_date - start_date)`.
9. **Which dialects are covered**
   - write-query asks among 10 dialects (PostgreSQL, Snowflake, BigQuery, Redshift, Databricks SQL, MySQL, SQL Server, DuckDB, SQLite, Other).
   - sql-queries documents 5 (PostgreSQL, Snowflake, BigQuery, Redshift, Databricks); its description says "all major data warehouse dialects".
   - data-context-extractor Bootstrap "Common options" lists 4 (BigQuery, Snowflake, PostgreSQL/Redshift, Databricks); its `sql-dialects.md` has 5 (adds MySQL).
10. **`EXISTS` vs `IN` wording**: write-query "Prefer `EXISTS` over `IN` for subqueries with large result sets"; sql-queries (PostgreSQL) "Use `EXISTS` over `IN` for correlated subqueries".
11. **Null-rate thresholds (inside explore-data)**: step 4 flags ">5% nulls (warn), >20% nulls (alert)"; the Completeness Score uses >99% complete = green, 95-99% yellow, 80-95% orange, <80% red.
12. **Good dimension cardinality (inside explore-data)**: "Best dimension columns ... 3-50 values" vs Segmentation Discovery "categorical columns with 3-20 distinct values".
13. **Anomaly thresholds**: statistical-analysis z-score outliers at |z| > 3 and IQR 1.5x; time-series anomalies "typically 2-3 standard deviations of the residuals". validate-data red flag: any metric changing ">50% period-over-period without an obvious cause".
14. **Package format (inside data-context-extractor)**: GUIDE Phase 4 says "Package as a zip file"; the script docstring says "distributable .skill file (zip format)" but writes `<skill_name>.zip`. The script's placeholder check only looks at `SKILL.md` for `[PLACEHOLDER]` / `[COMPANY]`, not at reference files.
15. **Table-documentation fields**: explore-data template includes Grain, Row Count, Owner, Example Values; data-context-extractor templates include Location, Partitioned By, Update Frequency with lag, Nested/Struct Fields, Sample Queries, Related Dashboards.

## Files

```
data-analysis/
  SKILL.md                      # this router
  CONNECTORS.md                 # ~~category placeholders (from the source plugin)
  LICENSE                       # Apache 2.0 (from the source plugin)
  analyze/GUIDE.md
  build-dashboard/GUIDE.md
  create-viz/GUIDE.md
  data-context-extractor/GUIDE.md
  data-context-extractor/references/{domain-template,example-output,skill-template,sql-dialects}.md
  data-context-extractor/scripts/package_data_skill.py
  data-visualization/GUIDE.md
  explore-data/GUIDE.md
  sql-queries/GUIDE.md
  statistical-analysis/GUIDE.md
  validate-data/GUIDE.md
  write-query/GUIDE.md
```
