# Frequently asked questions

## Statement imports and accounts

### Which banks are supported?

Barclays, Chase UK, American Express and NatWest have dedicated formats. Lloyds/Halifax-style, HSBC, Santander-style, Nationwide, Monzo and Revolut layouts have header-based detection/generic mapping. Export variants can differ. See [the exact format table](guide/imports.md#supported-formats-what-detection-means).

### Can I import PDFs or Excel files?

No. Import transaction CSV exports. PDF statements, `.xlsx`, OFX, QIF and live Open Banking are not implemented import paths.

### Can I have several bank accounts?

Yes, multiple account records exist. However, dedicated same-bank imports can reuse fixed account names, and a remembered header profile reuses its saved account and owner. Do not assume account numbers/filenames separate all native exports. [Multiple-account limits](guide/imports.md#multiple-accounts-and-remembered-formats).

### What if I import overlapping dates twice?

Known fingerprint-identical transactions are counted as duplicates. Check the import result: genuine identical same-day entries can also collapse, while a changed description/type/account can appear new. There is no bulk import undo.

### Can I correct a category?

Use Transactions **This only** for one entry, **Merchant + future** for a whole family, or Review for pending families. Amount/date editing, custom-category creation and transaction deletion are not visible UI features. Refunds in an expense category offset spending.

### Why is a transfer missing from spending?

A movement between accounts is not consumption. Candidate pairs may already be transfer-classified; confirmation also learns future account relationships. Rejecting a candidate does not restore original categories. [Reconciliation](guide/reconciliation.md).

### Can I import currencies other than GBP?

A currency field can be retained, but Ledgerly presents and sums values in pounds without exchange conversion; transfer matching does not check currency. Do not rely on mixed-currency totals or pairs.

## Households, users and Demo

### How many households, login users or members can I create?

No explicit numerical cap is configured in the inspected implementation. This is not a tested unlimited-capacity guarantee. Every real household needs at least one active financial member.

### Is a financial member a login user?

No. Members represent finances; users authenticate. A member does not need a login. Create logins separately in Households when needed.

### Is Viewer read-only?

No. Viewer can submit financial changes. Owner/Admin manage Households, and deletion is Owner-only, but roles are not a complete security model. Startup can also grant primary-household Owner membership when absent. [Actual permissions](guide/households.md#roles-and-actual-permissions).

### Are household databases separate?

Yes, financial files are physically separated, and normal screen queries use the selected household. Do not treat that as a strong security boundary between untrusted logins, given the membership limitations above.

### Can I experiment in Demo without changing real records?

Demo has a separate fictional database, editable records and a Reset button. It does not show real households or Households administration. Do not put real financial data into Demo; edited Demo is shared on that installation until reset.

### How do I remove a member or household?

Reassign a member's owned/scoped records to another active member before removal. Keep at least one member. Only an Owner can permanently delete an eligible isolated household after exact-name confirmation; the primary household cannot be deleted. Backup first—there is no UI undo.

## Funded and Tracking Goals

### Which goal type should I choose?

Funded reserves monthly headroom for an additional commitment. Tracking monitors progress without another reserve. All pre-existing goals migrate to Tracking. [Complete Goals guide](guide/goals.md).

### Does provision increase Already saved?

No. It is a planning commitment, not a transfer. Actual saved balance is manual. Monthly savings contribution, separately, drives the progress forecast.

### Why does a fully provisioned goal still say it needs a monthly amount?

The on-track savings message uses Monthly savings contribution, not provision. With contribution zero, there is no savings completion forecast even if the full monthly provision is reserved. Review both fields deliberately.

### How do I avoid counting the same commitment twice?

Select Already covered by Plan and an existing funded commitment with enough remaining coverage. Later reductions create only the uncovered additional reserve. For a paid periodic bill, explicitly use appropriate one-off planning treatment or link the already recurring Plan commitment; history is not rewritten automatically.

### What stops provision and how do I renew?

Pause or Complete stops additional provision; target attainment alone does not. Renew by choosing Active and reviewing target, date and actual saved amount. Archive hides a goal without a visible restore action.

## Planning and tax

### Is headroom my bank balance?

No. It is expected monthly income less modelled commitments. Actual cash surplus, imported account flow, manual Wealth and monthly capacity are different measures. [Planning glossary](planning/glossary.md).

### Why do Plan, Allocate and Forecast have different lifestyle figures?

They share the history-window selection, but Plan has an optional planned budget, Allocate has a saved allowance and Forecast starts from historical lifestyle. Funded reserve is already included once in their base capacity.

### Is the six-month baseline the average of all spending?

No. It sums category medians over the selected imported months, excluding the latest imported month, fixed families and marked one-offs. It can differ from the median total spend. Missing history matters.

### Are Wealth values imported automatically?

No. Assets and liabilities are manual dated snapshots; latest date wins. They do not automatically populate goals, bank balances or tax forms.

### Can I file tax returns or rely on an exact tax liability?

No. Tax Scenarios are simplified bundled-year estimates with omitted reliefs and known band/allowance limitations. They do not submit returns or initiate payments. [Tax guide](tax/index.md) and current HMRC/professional advice are needed for material decisions.

## Installation, privacy and recovery

### Does the app work offline?

Normal installed use and charts can work offline. Initial downloads/dependencies, some updates, public docs, external guidance and email need internet. Mac build 3 uses localhost independent of Wi-Fi; the Windows LAN-IP shortcut can become stale after a network change.

### Does Warwick Technologies receive my financial records?

No automatic financial-data upload is configured in inspected normal application use. Files stay on the installation computer. Support email and the public GitHub-hosted site are separate services. [Data & privacy](privacy.md).

### Is my database encrypted or backed up automatically?

No at-rest database encryption or scheduled/cloud backup is implemented here. HTTPS protects the browser connection after trust setup, not files on disk. Upgrade snapshots are not a substitute for independent backups.

### Can I use the old restore command or expect automatic rollback?

Not as a verified v3.8.5 recovery path. The older guide's automatic rollback is absent, and its supplied restore script targets a legacy layout. [Recovery guidance](backups.md).

### Will an upgrade delete existing households?

The normal scripts preserve private databases/secrets and create pre-upgrade snapshots; the goal migration is additive. That is a designed/code-verified behaviour, not a guarantee against all installation failures. Backup first and verify households afterward.

### Why does Ledgerly not open after reboot?

On Mac, log into the installing macOS account so its user application service starts. On Windows, check both services. Use the launcher/shortcut and retain errors. [Troubleshooting](troubleshooting.md#application-will-not-open).

### What if I forgot my password?

There is no email/web reset. Ask the installation administrator for local recovery using the installed administration tool with the correct private data path. Do not delete a database or create a new empty installation.

### How do I get help?

Email [help@getledgerly.co.uk](mailto:help@getledgerly.co.uk) with version, platform, steps and a redacted error or Demo screenshot. Do not send databases, secrets or raw statements. [Support checklist](support.md).
