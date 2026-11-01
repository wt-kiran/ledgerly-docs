# Troubleshooting safely

Keep the exact error, installed version and platform before changing anything. Do not delete databases, reset the installation or replace private data to make a screen appear. Back up before any recovery that could replace records.

## Application will not open

**macOS:** log into the account that installed Ledgerly, then open the current Ledgerly.app. Build 3 should use **https://localhost** on 443. Earlier :8443 bookmarks are superseded. A successful-install build marker distinguishes a complete installation from copied application code; reopening the latest bundle retries incomplete setup. Allow Terminal and administrator prompts to finish.

**Windows:** use the Ledgerly Start Menu shortcut and check **Ledgerly** and **LedgerlyCaddy** in Services. The app requires both the backend and HTTPS service. A network change can stale the printed LAN-IP address; the installation administrator should check the configured local endpoint instead of moving databases.

A local browser error means the listener may not be running; it does not establish database loss. On Mac, `logs/launch.log`, `install.log`, `update.log` and `ledgerly-error.log` under private data help diagnosis. On Windows use `C:\ProgramData\Ledgerly\logs\install.log` and service logs.

## HTTPS and certificate warnings

A responding application and a trusted certificate are different checks. The installer attempts local CA trust and may request administrator approval. If a warning persists, confirm the expected local address and installation before asking the administrator to repair trust. Do not switch to plain HTTP, disable Secure cookies or bypass warnings as normal financial use.

On macOS, installer-managed Caddy uses a system service for port 443. A bind error can mean permissions or another listener: retain the exact log. An unrelated existing Caddyfile is deliberately preserved; integration needs administrator review. Do not delete other applications' networking configurations. Windows includes local/LAN names; other client devices need their own trust setup if used.

## Windows services are stopped

In Services, inspect only **Ledgerly** and **LedgerlyCaddy**. Record missing/stopped states and try their normal Start/Restart controls with administrator help. If they fail again, use logs rather than repeatedly reinstalling or removing services. The installer should stop both before an upgrade and restart with health checks.

## Import failures

- Confirm original comma-separated CSV, not PDF/Excel, and a combined request below 20 MiB.
- Read per-file results and check the account/owner. If a mapping redirect occurred mid-batch, submit the remaining files separately.
- Map Date, Description and Signed amount or Debit/Credit. Verify day/month dates, sign convention and a preview row against the original statement.
- Avoid decimal commas, bracket negatives or CR/DR suffixes unless your dedicated parser explicitly handles the export.
- An old remembered header mapping can reuse the wrong account. Native same-bank naming can also be ambiguous. Stop bulk importing and seek support; no profile editor/force-mapper or import-undo button exists.
- If an upload token is missing/expired, return to Import Statements and choose the file again.

## Transfers and duplicates

Import both accounts, check exact opposite amounts and dates within three days, and inspect Reconciliation candidates. An unmatched side can mean a missing account, not an error. Rejecting a pair does not undo transfer categories; review Transactions carefully.

For duplicates, compare parsed/new/duplicate counts with bank originals. Overlaps normally deduplicate, but identical genuine rows may collapse and changed descriptions/types can import again. There is no transaction delete or split UI; do not edit a database to compensate without reviewed recovery.

## Unexpected headroom

Check these in order:

1. Correct household and expected income overrides in Plan.
2. Genuine recurring fixed/saving types and **monthly equivalents**, not mixed per-occurrence headline totals.
3. Essential-category overrides, fixed-family exclusions and one-off treatment.
4. Latest imported month exclusion and incomplete history; compare 3m/6m/full references.
5. Additional saving and existing allocations, avoiding overlap.
6. Active Funded Goal provision and its Plan coverage. Tracking, Paused and Completed add no reserve.
7. Saved Allocate allowance/extra investing versus Plan's optional lifestyle budget and Forecast's historical baseline.
8. Whether the displayed figure is actual surplus, monthly capacity, scenario or Wealth.

After a Plan validation error, inspect all saved fields because some earlier values can persist. Individual responsibility summaries may differ from household total through rounding or missing account ownership; this is separate from exact Funded provision aggregation.

## Household and member problems

Check the sidebar household and sign-in selection. Households administration requires Owner/Admin; financial members do not automatically have login accounts. Removing a member with records requires another active member for reassignment. The primary household cannot be deleted.

If records appear in the wrong household, stop making changes and contact support; do not manually move database files. Be aware that Viewer is not read-only and startup can grant primary-household ownership. Only trusted login users should use this release.

## Login and password problems

Check username, selected household and password; usernames are case-insensitive. Wait after repeated failed attempts (five failures within 15 minutes are rate-limited by client address). An invalid form token needs a refresh/sign-in, not a database reset. Session expiry can require signing in again after up to eight hours.

There is no email reset. The installation administrator can use the installed interactive local user tool with the correct private-data environment; ask support rather than launching it against an unintended empty runtime database.

## Upgrade or recovery concerns

Preserve the original data directory and retained backups. A health-check failure does not invoke an implemented automatic code rollback in this version. Do not rely on the legacy restore command for the modern layout. Follow [backups and recovery](backups.md) and retain redacted logs for [support](support.md).

## Tax or Wealth results look surprising

Tax models are static simplified estimates, not complete legislation/relief engines. Confirm the chosen tax year and every input; read scenario-specific omissions. Wealth uses latest **snapshot date**, not entry order, and a negative net worth can be displayed without a minus sign. Check the underlying asset/liability totals before interpreting the result.
