# Upgrade without losing your data

A normal application update replaces code and preserves household records. Keep an independent backup before upgrading; a successful older release does not prove every new installer works on your exact computer.

## Before you start

- Note the version in **About Ledgerly**, your platform and the active household names.
- Keep original bank exports and a private backup of the complete data directory.
- Allow the installer to stop services. Do not copy/replace an active database manually.
- Download the new installer through [Downloads](../downloads.md). {{ release_link }} lists the existing v3.8.5 assets.

## macOS

Open the new DMG, replace Ledgerly.app in Applications, then launch it. The launcher checks both application version and successful-install build marker. Build 3 upgrades earlier v3.8.5 launchers, including an incomplete installation that already copied v3.8.5 application code.

Terminal performs the upgrade. It stops the application service, retains private-data/code snapshots, updates the runtime/dependencies and reuses installation health checks. Installer-managed Caddy is configured as the system service for port 443, so administrator approval can be requested. An external Caddyfile/service is preserved.

The normal address is **https://localhost**. The earlier :8443 workaround is superseded. Runtime remains `~/Applications/Ledgerly`; private data remains `~/Library/Application Support/Ledgerly`.

## Windows

Run the new single EXE. It stops Ledgerly and LedgerlyCaddy before the private-data backup and file replacement, then restarts both. Private data remains `C:\ProgramData\Ledgerly`; runtime remains under Program Files. Keep `logs\install.log` if the upgrade stops.

## What v3.8.5 changes in existing goals

Every existing goal defaults to **Tracking**. Target, saved balance, monthly savings contribution, date, responsibility and notes remain. No additional provision is invented. Overview/Allocate buffer can rise compared with an older version that deducted all contributions. Explicitly choose Funded and set provision where an additional monthly commitment is intended.

Other household files migrate when opened, using additive goal columns. Open each real household after upgrading and check Overview, Plan, Goals, Help/About, accounts and recent transactions. Verify a reboot on a disposable test installation before broader distribution.

## If the upgrade does not complete

Do not delete databases, secrets or backups. Keep the Terminal/installer error and version. The current updater retains backups but **does not implement the automatic code rollback described by the older v3.6.3 PDF**. The legacy restore command is not a verified one-click recovery for this layout.

Reopening a current macOS launcher retries incomplete setup; it does not declare success merely because app.py has a newer version. For a failed Windows upgrade, use its persistent log and retained snapshot with support. See [backups](../backups.md) and [troubleshooting](../troubleshooting.md).
