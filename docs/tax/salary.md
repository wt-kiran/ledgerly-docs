# Salary / Bonus

Use Salary / Bonus for an annual employment estimate using the standard main-rate/employee-NI assumptions. This is not a monthly payslip or PAYE reconciliation.

## Open and save a scenario

1. Select **Tax Scenarios → Salary / Bonus**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Gross salary for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Gross bonus for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

Gross salary plus bonus gives employment income. A stored £12,570 Personal Allowance tapers by £1 per £2 above £100,000 total income, floored at zero. Tax uses main 20%/40%/45% bands. Standard employee NI is modelled at 8% between £12,570 and £50,270 and 2% above £50,270. The headline adds Income Tax and NI; a separate row shows estimated net income.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

Salary £30,000 and bonus £5,000 in 2026/27 return Income Tax £4,486 and NI £1,794.40: **£6,280.40 combined deductions**, with **£28,719.60 net** in the stored model.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

No tax codes, benefits, student loans, salary sacrifice, Scottish main rates, employer NI or period-by-period PAYE timing are calculated. Do not enter a monthly salary into the annual field or confuse the deductions headline with take-home pay. Upper-band implementation is simplified.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
