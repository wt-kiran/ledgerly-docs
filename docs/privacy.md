# Data, privacy and local security

Ledgerly's financial application stores records on the computer running it. It has no configured Ledgerly-hosted financial-data upload, Open Banking connection, cloud sync or telemetry service in the inspected v3.8.5 code. Warwick Technologies does not automatically receive your household transactions through normal local application use.

This public documentation site is separate and hosted by GitHub Pages. Visiting it or GitHub downloads makes normal web requests to those services; it does not upload your local financial database. The documentation uses bundled theme/search assets and system fonts, with no added analytics or remote font service.

## Where data lives

| Platform | Runtime | Private data |
|---|---|---|
| macOS | `~/Applications/Ledgerly` | `~/Library/Application Support/Ledgerly` |
| Windows | `C:\Program Files\Ledgerly` | `C:\ProgramData\Ledgerly` |

Private data includes the primary database, isolated household databases, the session-signing secret, pending import files, logs and backups. Household files are physically separate; the primary database also stores login users, memberships and the household registry. This organisation prevents accidental mixing in ordinary use, but it is not a complete access-isolation guarantee.

## Internet and local networking

Internet is needed to download installers/dependencies and may be needed for dependency updates. Normal installed use and charts can work offline. Support email and external HMRC/documentation links need their usual network access.

macOS build 3 listens only on loopback at **https://localhost**. Windows also configures a LAN IP and a Private-profile inbound HTTPS firewall rule, so its login page can be reachable from other devices on that network. Do not describe Windows as loopback-only, and do not expose either installation through router port forwarding.

## Authentication and permissions

Passwords are locally hashed with PBKDF2-SHA256 (600,000 iterations), not stored as plain text. Sessions use a persistent signing secret; cookies are configured Secure, HttpOnly and SameSite Lax by the normal installers. Forms require a matching session security token. Sessions last up to eight hours; failed sign-ins are temporarily rate-limited by client address in process memory.

HTTPS encrypts the browser connection once local CA trust is set up correctly. It does **not** mean SQLite databases, CSVs, logs or backups are encrypted at rest. Their protection also depends on operating-system account permissions, disk encryption and the people with access to the computer. No universal other-local-user exclusion has been verified.

!!! warning "Trusted-user installation only"
    Viewer is not enforced read-only. Startup can grant primary-household Owner access to an existing user missing that membership. Household names are visible in the login selector. Use Ledgerly only with trusted login users and a trusted network; do not rely on role labels or separate databases to isolate untrusted people. [Actual permissions](guide/households.md#roles-and-actual-permissions).

## Backups, upgrades and portability

Updaters retain pre-upgrade snapshots; there is no verified scheduled/cloud backup or modern one-click restore. Routine upgrades preserve data, but independent backups are still needed. Keep the database, household files and secret together in recovery planning. [Backup guidance](backups.md).

There is no general CSV export, Open Banking export or complete portability UI. Retaining original statement CSVs preserves your source records; SQLite files are implementation storage rather than a documented interoperable export format.

## Support information

Share version, platform, a redacted error/log excerpt and preferably a fictional Demo screenshot. Do not email real databases, `.ledgerly-secret`, complete backups, raw bank exports, account numbers or passwords. Pending CSV uploads/logs can also contain private information. [Support checklist](support.md).

## Installer-managed configuration

Normal users should not need to edit service environment variables. The installed data root, primary database path and secret-file path point to the private directories above; a separate secret override is possible for administrator configuration. Secure cookies are on by default. The upload limit is 20 MiB for the whole request. These are not preferences on a Settings page, and changing storage paths without a migration can create an apparently empty installation. Ask support before altering them.
