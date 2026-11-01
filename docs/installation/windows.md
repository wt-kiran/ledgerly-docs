# Install on Windows

## Requirements and download

Use **Windows 11 x64 or ARM64**. The single EXE supports both; do not choose a separate Python/Caddy package manually. Administrator rights and internet access are needed for the initial bootstrap. A verified minimum RAM/disk figure and support for older Windows versions are not established here.

Choose the Windows asset on [Downloads](../downloads.md). The published {{ release_link }} contains **Ledgerly-Setup-3.8.5.exe**. Verify its SHA-256 identity if desired.

## Install and first launch

1. Run **Ledgerly-Setup-3.8.5.exe** and allow the normal UAC administrator prompt.
2. The installer sets up required Python, Caddy and the Windows service wrapper when needed. You should not need to install these components manually. Windows Package Manager (winget) is used if Python needs installing; an unavailable dependency produces an installer error to retain for support.
3. Wait for application and HTTPS health checks. Keep the installer window open while it works.
4. Use the created **Ledgerly** Start Menu shortcut or the address printed by the installer.
5. Complete [first setup](../getting-started/setup.md), or sign in if this is an upgrade.

The build is unsigned, so Windows may show an unverified-publisher warning. Confirm the source/checksum before deciding whether to run it. Do not disable SmartScreen, your firewall or certificate checks globally.

## Services, files and HTTPS

| Item | Standard location or name |
|---|---|
| Runtime | `C:\Program Files\Ledgerly` |
| Private data | `C:\ProgramData\Ledgerly` |
| Persistent install log | `C:\ProgramData\Ledgerly\logs\install.log` |
| Application service | `Ledgerly` |
| HTTPS service | `LedgerlyCaddy` |

Both services are configured for automatic startup and restart after failure. On ARM64 the installer chooses native Caddy and an appropriate service wrapper; it can use the existing x64 wrapper fallback under Windows 11 ARM64 emulation.

Caddy provides local HTTPS on port **443** and attempts to trust its local CA on this PC. The current Windows configuration includes the installation LAN IP and localhost, and adds an inbound TCP 443 rule for the **Private** firewall profile. Unlike the macOS build, Windows is **not restricted to loopback**: another device on that private network may be able to reach the login page. Household names can be visible before sign-in. Use only on a network you trust; do not add router port forwarding.

Other client devices would need their own appropriate CA trust, but this guide does not claim a supported remote-access deployment. If the PC changes networks, the LAN-IP shortcut may become stale. Ask the installation administrator to check the locally configured `https://localhost` endpoint and services; do not apply the Mac launcher's Wi-Fi independence claim to the Windows shortcut.

## Upgrading an existing installation

Run the newer EXE using the same normal process. It stops **both** services, waits for them to stop, retains a private-data snapshot, replaces application file contents, installs/checks dependencies and restarts with health checks. Templates and static assets are copied into their existing directories rather than creating `templates\templates` or `static\static`.

Private databases, household files, secrets and existing backups stay in ProgramData. Do not choose a new empty data directory to resolve a problem. [Upgrade checklist](upgrading.md).

## If something fails

Record the exact error and retain `install.log`. In Windows **Services**, check whether both Ledgerly and LedgerlyCaddy exist and are running. Only start/restart the known Ledgerly services; do not remove services or delete application data. A certificate warning needs trust diagnosis, not encryption bypass. [Troubleshooting](../troubleshooting.md).

No complete supported uninstaller is supplied by the inspected installer; it is configured without an Inno uninstaller. Ask support for removal that preserves private data and does not remove dependencies used by other software. Building the EXE yourself is a maintainer task, not part of recipient installation.
