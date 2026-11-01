# Download Ledgerly

**Latest published application release: v{{ version }}.** These are early testing installers. Keep independent backups of important financial records, and check the [known limitations](limitations.md) before relying on estimates or household permissions.

{{ download_cards }}

The macOS release contains bundle build **3.8.5.3**, which uses `https://localhost` on port **443**. The Windows installer supports **x64 and ARM64**. Mac dependencies are obtained for the host computer; the bundle declares macOS 13 as its minimum, but this is not a claim that every hardware/OS combination has been tested.

[macOS installation](installation/macos.md) · [Windows installation](installation/windows.md) · [Upgrade safely](installation/upgrading.md) · [Release notes](releases.md)

## What was verified?

Both assets were downloaded from the existing {{ release_link }} and hashed on **{{ verification_date }}**. The byte counts and SHA-256 digests above match the published asset metadata. This verifies file identity, not the absence of defects or a successful installation on your computer. Neither installer has been replaced by this documentation project.

Installer links open a separate tab or start a download while leaving this page available. Your browser may download the file without showing another tab.

## Check your downloaded file

On macOS, open Terminal and run this in the folder containing the download:

```sh
shasum -a 256 Ledgerly-3.8.5.dmg
```

On Windows, open PowerShell in the download folder:

```powershell
Get-FileHash .\Ledgerly-Setup-3.8.5.exe -Algorithm SHA256
```

Compare the complete result with the appropriate digest above. Case does not matter. If it differs, do not run that file; download again from the verified release link and contact [support](support.md) if the mismatch remains.

## Before you install

You need internet access for the first dependency installation. The existing build is unsigned; macOS or Windows may identify the publisher as unverified. Confirm the source and checksum before deciding whether to open it. Administrator approval is required for some installation and certificate steps.

Read the platform guide before upgrading an existing household. Do not delete databases, secrets or backup folders to solve an installation error.
