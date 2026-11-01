# Release notes

## v{{ version }} — published 31 October 2026

The existing {{ release_link }} contains the verified macOS DMG and Windows EXE. See [Downloads](downloads.md) for exact sizes/checksums. Application version and macOS packaging build are different identifiers; the published DMG contains build **3.8.5.3**.

### New goal behaviour

Funded Goals reserve monthly headroom; Tracking Goals do not add another deduction. Existing goals default to Tracking using additive database columns, preserving values and ownership. Active/Paused/Completed statuses and explicit existing-Plan coverage keep provision separate from actual saved progress and prevent reuse of covered funding. Target attainment does not silently stop provision.

### Consistent planning figures

Plan, Overview, Allocate, Goals and Forecast use shared capacity calculations. Funded provision is included once. Savings contributions still drive goal progress forecasts; they do not accrue balances. Demo and local Help explain both types.

### macOS local access and packaging builds

The original LAN-IP dependency was removed. An initial loopback port-443 installation encountered user-service binding failure; build 2 temporarily used 8443. **Build 3 restores https://localhost on port 443 using administrator-approved system Caddy service registration**, keeping the financial app as the existing user service. It preserves externally managed Caddy configurations and checks installation completion/health before opening the browser.

A same-version build marker repairs interrupted installation, persistent logs help diagnose failures, and Chart.js is bundled for offline charts. Windows retains its current local/LAN HTTPS configuration rather than inheriting the Mac loopback networking claim.

### Upgrade considerations and limits

Use [the platform upgrade guide](installation/upgrading.md), not database replacement. Existing goal conversion to Tracking can increase a previous forward buffer until additional funding is explicitly marked Funded. Windows copying avoids nested asset directories and stops/restarts both services. Pre-upgrade data snapshots are retained.

Early-release limitations remain: Viewer is not read-only, primary-household startup membership needs care, imports/negative Wealth display/tax models have documented boundaries, and a modern one-click restore/uninstaller is not verified. [Known limitations](limitations.md).

## Earlier reliable records

These summaries use the retained release notes and reference guide, not a reconstructed claim that every historic release has been tested.

| Version | Reliable scope of record |
|---|---|
| 3.8.4 | Prior stable packaging baseline; macOS version-aware launcher/upgrade correction, Windows ARM64 wrapper fallback; visible Capital Decision Modeller remains removed |
| 3.8.3 | Release-builder notes exist, but no separate full feature changelog is verified; do not infer additional behaviour |
| 3.8.0 | Historical notes describe capital modelling work; that is not an available feature in the current visible Forecast UI |
| 3.7.0 | Cross-platform packaging/runtime-data separation baseline; platform installation records retained |
| 3.6.3 | Earlier complete user guide covers Mac-only/legacy-layout installation, workflow and prior recovery descriptions; current guides supersede changed installation, goals, allocation and recovery details |

For questions about an older installed version, note About's version and contact [support](support.md). Historic notes are not current installation or tax instructions.
