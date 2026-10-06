# Bhavuk Jain | Data Engineering Portfolio

A responsive portfolio website with an interactive RouteScope travel-data demo, engineering case studies, and professional background.

## Website
https://bhavukj100.github.io/

## Repository contents
- `index.html`: website, CSS, and interactive JavaScript demo.
- `carrier-priority-demo.zip`: complete Python + SQL project, synthetic data, sample outputs, tests, and CI workflow.
- `.nojekyll`: static GitHub Pages configuration.

## Run RouteScope
Download and extract `carrier-priority-demo.zip`, then run these commands inside the extracted `routescope-analytics` folder:

```bash
python pipeline.py
python -m unittest discover -s tests -v
```

The pipeline validates synthetic flight observations, calculates route-level market shares, and selects the smallest ranked carrier prefix reaching a configurable coverage target. It exports recommendations and a quality report.

RouteScope is a new portfolio implementation prepared with AI assistance. EventLens and WarehouseBridge are conceptual design case studies. Public examples contain no employer source code or datasets.

## Website features
Responsive layout, accessible controls, route selection, adjustable coverage, expandable case studies, project download, email contact, and GitHub profile link. No build dependencies.

## Hosting
GitHub Pages publishes the `master` branch from the repository root.
