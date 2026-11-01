# Install on macOS

## Requirements and download

The v3.8.5 bundle declares **macOS 13 or later**. The bootstrap obtains Homebrew/Python/Caddy dependencies for the host Mac; this is not a guarantee that every Intel/Apple-silicon OS combination has been acceptance-tested. You need a normal macOS login account, free space for the application/data/dependencies and permission to approve installation prompts. No verified minimum RAM/disk figure is published.

Download the DMG from [Downloads](../downloads.md), check its checksum if desired, and keep internet access available for initial dependency setup. The existing {{ release_link }} contains macOS bundle build **3.8.5.3**.

## Install and first launch

1. Open **Ledgerly-3.8.5.dmg**.
2. Drag **Ledgerly.app** to **Applications**. Replace the previous launcher if upgrading.
3. Open Ledgerly.app. This launcher opens Terminal for installation or an upgrade; let it finish rather than closing the window mid-process.
4. If Apple Command Line Tools are missing, macOS may open its installation prompt and ask you to rerun Ledgerly after they finish. Approve Homebrew installation if requested.
5. Allow required Python/Caddy components and Python packages to install.
6. Enter your Mac administrator password when asked to register installer-managed Caddy as the system HTTPS service on port **443** and trust the local certificate authority. Terminal does not display characters while you type the password.
7. On successful application and HTTPS health checks, Ledgerly opens **`https://localhost`**. Complete [first setup](../getting-started/setup.md) or sign in to your existing household.

The build is unsigned. macOS may require its normal user-controlled Open/security process. Verify the source and checksum; do not weaken general system security or disable certificate validation to make a financial application open.

## Why a launcher, runtime and data folder?

| Item | Standard location |
|---|---|
| Visible launcher | `/Applications/Ledgerly.app` (or the Applications location you chose) |
| Installed runtime | `~/Applications/Ledgerly` |
| Private data | `~/Library/Application Support/Ledgerly` |
| Ledgerly logs | `~/Library/Application Support/Ledgerly/logs` |

The app bundle launches/updates a separate runtime. Your private databases are not inside the DMG. Replacing the launcher is not a reason to move or delete the private data directory.

## HTTPS, reboot and changing Wi-Fi

Build 3 uses the standard HTTPS port 443. Caddy runs as a system service so it can bind the privileged port, while the financial application remains the existing per-user service on loopback. Both HTTPS listeners are restricted to this Mac's loopback addresses. There is no static LAN IP or router port-forwarding requirement.

After a reboot, **log into the macOS account that installed Ledgerly**. Its application service starts after login, not while the Mac is still at the login screen. Open Ledgerly.app if needed; it checks the endpoint and can attempt service recovery before opening the browser.

The old build-2 `https://localhost:8443` address is superseded by `https://localhost`. A current build marker forces an upgrade from an earlier/partial same-version installation.

A responsive endpoint is not proof that your browser trusts its certificate. Complete the local CA trust step; do not dismiss a new warning blindly. [HTTPS troubleshooting](../troubleshooting.md#https-and-certificate-warnings).

## Existing Caddy and common installation problems

An externally managed Caddyfile is preserved and its service is not restarted. It must already provide the localhost HTTPS site to the local Ledgerly backend. If it does not, the installer reports a health-check failure: ask the Mac administrator to review integration instead of replacing another application's configuration.

If port 443 is occupied or unavailable, keep the Terminal message and log. Do not change random ports, delete data or remove another application's service. If installation stops after copying application files, reopen the latest launcher: its successful-install marker is written only after health checks, so a partial setup is retried.

## Upgrade and uninstallation

Follow [upgrading](upgrading.md) for an established household. Keep an independent backup before updating. No complete general uninstaller has been verified for this release. Removing Ledgerly.app alone does not unregister services or remove the separate runtime/private data; ask [support](../support.md) for a safe removal plan that preserves records and shared dependencies.
