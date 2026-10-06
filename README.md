# Bhavuk Jain | Data Engineering Portfolio

A responsive portfolio with runnable RouteScope and AWS Retail Sales Pipeline projects, professional background, and contact links.

Website: https://bhavukj100.github.io/

## Featured projects

- **RouteScope:** synthetic route coverage analytics using Python and SQL. Download `carrier-priority-demo.zip`, extract it, and run `python pipeline.py` and `python -m unittest discover -s tests -v` in `routescope-analytics`.
- **[AWS Retail Sales Pipeline](https://github.com/bhavukj100/aws-retail-sales-pipeline):** synthetic orders, payments, returns, and products reconciled with PySpark. Includes Parquet outputs, four local tests, Terraform for S3/Glue/Athena, and an optional Airflow DAG. AWS infrastructure has not been deployed; Airflow execution has not been tested.

## Files and hosting

`index.html` contains the responsive website and interactive RouteScope demo. `.nojekyll` enables static serving. GitHub Pages publishes the `master` branch from the repository root. `.github/workflows/daily-checks.yml` validates the website and packaged RouteScope project, then updates `ACTIVITY.md` with automated maintenance results.

The projects are new AI-assisted portfolio implementations using synthetic data. Public examples contain no employer source code, datasets, or internal system details.
