# Known limitations in v3.8.5

These boundaries were found in the implemented screens and code, not inferred from product ambitions. They are important when testing Ledgerly with real records.

| Area | Current boundary | What to do |
|---|---|---|
| User roles | Viewer can edit financial records; startup can add primary-household Owner membership to users missing it | Use only trusted login users; do not promise strong role/household isolation |
| Windows network | HTTPS includes LAN IP; Private-profile inbound rule is created | Use a trusted network; do not port-forward |
| Account imports | Dedicated native formats use fixed account names; remembered headers reuse saved account/owner | Test one file and verify destination; seek support for same-bank ambiguity |
| Duplicate matching | Genuine identical entries can collapse; changed descriptions/types can evade dedupe | Compare counts/totals with original statements |
| Currency | No conversion and no currency check in transfer pairing | Use GBP records for reliable comparable totals |
| Transaction editing | No amount/date edit, delete, split or general export UI | Retain original statements; use supported category/treatment corrections |
| Recurring | No cadence editor; expected amounts do not consistently reject invalid input; mixed-cadence headline is not a monthly total | Use positive per-occurrence values and check Plan |
| Plan | Some failed validations can leave earlier fields saved; member breakdown may differ with rounding/unassigned ownership | Review saved values, owners and responsibility |
| Cash pots | No visible create/delete/name/source-account editor for Plan allocations | Do not assume example pots are seeded in a fresh household |
| Goals | Provision is independent of savings forecast; no automatic accrual; archive has no restore UI | Use Pause for a resumable goal and update actual saved balance deliberately |
| Wealth | Manual snapshots; no delete/history/type-edit UI; negative net-worth display may omit minus sign | Check liabilities versus assets manually; use same name/date to correct amount |
| Tax | Static simplified rules; future-year options are bundled assumptions, not live legal verification | Read scenario-specific limits and check material decisions independently |
| Backup/recovery | No scheduled/cloud backup or verified modern one-click restore; no automatic code rollback | Keep independent backups; seek support-assisted restoration |
| Uninstall | No complete general uninstaller verified | Ask support; deleting the launcher does not remove services/data |
| Forecast | Monthly deltas only; removed Capital Decision Modeller is not available | Use current Forecast controls only |

Installation scripts are inspected and packaging checks passed, but that does not prove a full fresh install/upgrade/reboot on every supported machine. Published files and hashes are verified on Downloads; no installer assets are changed by the documentation project.

For practical next steps use [troubleshooting](troubleshooting.md), [FAQ](faq.md) or [support](support.md).
