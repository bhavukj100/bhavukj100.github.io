# Bhavuk Jain | Data Engineering Portfolio

Website: https://bhavukj100.github.io/

A responsive portfolio with three projects in one interactive gallery. Visitors
can explore a small result set, understand the modeling choices, and open the
source code without leaving the page crowded with every case study at once.
Each project card has an original purple SVG illustration tied to its purpose. The
homepage listing shortcuts open the matching record in the Airbnb explorer.
On phones, only the selected card expands to show its visual.

## Projects

- **[Airbnb analytics](https://github.com/bhavukj100/airbnb-analytics-dbt-snowflake):**
  Snowflake and dbt transformations. The browser includes 12 listing summaries
  exported with a read-only query against `AIRBNB.GOLD.FACT`. Capacity and rate
  filters, sorting, chart/table views, and listing details operate locally on
  that embedded extract. It is static, not a live warehouse connection. The
  project walkthrough uses the verified lineage image from the project repo.
  Credit: [Ansh Lamba's project tutorial](https://www.youtube.com/watch?v=3SZSDKEZqoA&t=819s).
- **[Retail, reconciled](https://github.com/bhavukj100/aws-retail-sales-pipeline):**
  a small synthetic revenue example matching the repository's inputs and expected
  outputs. Day 1 shows $150 captured, $20 refunded, and $130 net; Day 2 shows an
  unpaid order with $0 revenue. The Spark pipeline runs locally. AWS infrastructure
  and an optional Airflow DAG are included in that project as code, without a
  claimed cloud deployment.
- **RouteScope:** an interactive synthetic flight-share example with three routes
  and a coverage slider. It includes the carrier that crosses the target. The
  Python and SQLite implementation remains in `carrier-priority-demo.zip`.

## Airbnb preview data

Only listing ID, capacity, bedrooms, bathrooms, and nightly rate are embedded.
No host names, booking identifiers, credentials, or personal contact data are
exported. Rates retain the source values; the project does not identify their
currency. Averages and counts in the explorer describe the 12-row preview.

The export query groups repeated final-table rows into listing summaries. It
was executed in a separate read-only evidence worksheet; project model SQL,
dbt configuration, and Snowflake objects were not changed.

```sql
SELECT LISTING_ID, ACCOMMODATES, BEDROOMS, BATHROOMS, PRICE_PER_NIGHT,
       COUNT(*) AS FACT_ROWS
FROM AIRBNB.GOLD.FACT
GROUP BY LISTING_ID, ACCOMMODATES, BEDROOMS, BATHROOMS, PRICE_PER_NIGHT
ORDER BY LISTING_ID, PRICE_PER_NIGHT
LIMIT 12;
```

`FACT_ROWS` is used for verification only and is not included in the public
preview or presented as a booking count. The interactive data is embedded in
`index.html` in the `airbnb-data` JSON element.

## Hosting and maintenance

`index.html` contains the website, styles, demos, and optional consent-based
analytics. Plus Jakarta Sans is embedded as a subsetted variable WOFF font in the
HTML, so no external font request is needed. Its SIL Open Font License is included
in the HTML source. System fonts remain as fallbacks.
`.nojekyll` enables static serving. GitHub Pages publishes `master` from the
repository root. `.github/workflows/daily-checks.yml` validates website anchors,
the RouteScope archive, and coverage scenarios. It updates `ACTIVITY.md` with
actual maintenance results.

Visitor analytics remain optional and private to the owner's GA4 account.
No Snowflake credentials or live warehouse access are exposed to visitors.
Public examples contain no employer source code or datasets.
