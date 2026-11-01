# Backups and recovery

Keep an independent, private backup of Ledgerly's complete data directory and your original bank CSVs. Local-first does not mean automatically backed up or encrypted. Store backups where only authorised people can access them, and protect the computer with your normal operating-system security.

## What upgrades retain

- **macOS:** after stopping the application, the updater retains primary database/sidecars, signing secret, household directory and a runtime-code snapshot (not the virtual environment). It keeps the five newest matching updater snapshots under the private backup directory.
- **Windows:** the installer stops both services and retains primary database/sidecars, secret and household directory before replacement. Its backup folder is preserved; the inspected installer does not impose the Mac five-snapshot retention rule.

These are **upgrade snapshots**, not timed/scheduled backups. Caddy CA storage is separate and is not included in these listed financial-data snapshots. Existing backups are private records, not files to put in a release or public repository.

## Before making an independent copy

Ask the installation administrator to stop the appropriate Ledgerly services so the copy is coherent. Do not copy only a live main database while ignoring active write-ahead files or other household databases. Record the app version and snapshot date. Preserve a complete matching set, including the secret and household files.

No new public backup-export button is available in v3.8.5. This guide deliberately avoids a destructive one-line shell command that might target the wrong installation.

## Recovering after a failure

1. Stop making further changes and keep the exact error/log.
2. Preserve current data and existing backups before attempting restoration.
3. Contact the administrator/support with platform, version and snapshot dates, not the backup contents.
4. Use a reviewed recovery procedure for the canonical runtime/data layout; do not overwrite an active database.
5. Verify each household, recent imports, Plan and login after recovery.

The older PDF describes automatic rollback and `restore_ledgerly.command`. The current updater does **not** implement that automatic rollback, and the supplied restore script still targets an older layout and has an enumeration problem. It is not verified for the v3.8.5 private-data separation. Do not run it as a normal undo or assume it will recover the current household safely.

**Example:** a new installer fails before HTTPS starts. Keep the pre-upgrade snapshot and logs, then retry the current Mac launcher or ask support as appropriate. Do not create a new empty database or delete the original household to make the login page appear.

Related: [upgrading](installation/upgrading.md), [troubleshooting](troubleshooting.md), [privacy](privacy.md).
