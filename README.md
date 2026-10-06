# Bhavuk Jain | Data Engineering Portfolio

A responsive static portfolio with an interactive RouteScope travel-data demo, engineering case studies, and professional background.

## Contents
- `index.html`: complete website, CSS, and browser demo.
- `carrier-priority-demo.zip`: downloadable project package.
- `projects/routescope-analytics/`: Python + SQL implementation with synthetic data.
- `screenshots/`: screenshots captured from the published website in a separate browser.
- `.nojekyll`: serves the website as static files.

## Publish
1. Sign into GitHub as `bhavukj100`.
2. Create a public repository named `bhavukj100.github.io`.
3. Extract this ZIP and upload its contents to the repository root. Upload `index.html` at the root, not inside another folder.
4. Open repository Settings > Pages. Under Build and deployment, choose Deploy from a branch, select main and / (root), then Save.
5. Wait for GitHub to confirm deployment and use the URL shown there. Expected address: https://bhavukj100.github.io/.

## Run the project
```bash
cd projects/routescope-analytics
python pipeline.py
python -m unittest discover -s tests -v
```

RouteScope is a new implementation prepared with AI assistance. It uses synthetic flight observations and contains no employer code or datasets. EventLens and WarehouseBridge are conceptual design case studies, not runnable public implementations.

## Design
Responsive layouts, semantic headings, keyboard focus styles, configurable route coverage, expandable project descriptions, project download, email contact, and a GitHub profile link. No build tooling or third-party JavaScript required.
