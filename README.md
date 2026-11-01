# Ledgerly official documentation — v3.8.5 preview

MkDocs Material source for https://ledgerly-app.com. This checkout is a **local, unpublished preview**. Do not merge/push to the live site's default branch before owner approval: that branch currently uses legacy GitHub Pages publishing.

## Local build and preview

Use Python 3.11+ (the pinned build was tested with 3.13):

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs build --strict
python scripts/validate_site.py
mkdocs serve --dev-addr 127.0.0.1:8000
```

On Windows activate with `.venv\Scripts\Activate.ps1`, or invoke `.venv\Scripts\python.exe` and `.venv\Scripts\mkdocs.exe` directly. The preview is at http://127.0.0.1:8000. `site/` is generated output; don't edit it.

## Structure and release maintenance

- `docs/`: public user manual, fictional Demo screenshots and brand stylesheet.
- `overrides/`: reused text wordmark and Material layout adaptation.
- `release.json`: version, exact release/installer URLs, bytes and verified SHA-256 values. The build hook generates all installer links with new-tab safety attributes.
- `scripts/validate_site.py`: internal links/anchors, download attributes, active assets, search/CNAME and private-payload checks.
- `DEPLOYMENT.md`: owner-approved transition to the existing GitHub Pages host.

To prepare a later release, inspect the actual GitHub Release, download each published installer privately and compute SHA-256. Update `release.json` only after checking names, sizes and digests. The header badge reads this same configuration. Update version-specific documentation, then build/test. Do not invent future asset URLs. Missing assets should be shown as unavailable rather than guessed.

The application is proprietary. Never copy Flask/Jinja/Python application sources, schemas, runtime directories, household data, secrets, CSVs, installer binaries or release-builder ZIPs into this repository. Installer distribution stays in GitHub Releases. The private source/field audits and PDF review are deliberately outside this checkout.
