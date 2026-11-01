# Rental Income

Use Rental Income to compare annual rent, non-finance running costs, entered finance costs and other income. It is a scenario, not a property ledger.

## Open and save a scenario

1. Select **Tax Scenarios → Rental Income**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Rent received this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Property running costs £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Mortgage/loan interest & finance costs £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Your other taxable income this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

Property profit is max(0, rent − non-finance expenses). The model uses the remaining Personal Allowance and income bands after other income. Entered finance costs create a lower-rate tax reduction, capped by computed property tax and floored at zero, rather than being subtracted again from rental profit.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

For 2026/27, rent £12,000, expenses £2,000, finance costs £1,000 and other income £30,000 give £10,000 property profit, £2,000 tax before the model's £200 finance reduction, and **£1,800 estimated property Income Tax**.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

Restrictions on finance relief, carried losses, joint ownership, Rent a Room and the property allowance are not modelled. Do not enter mortgage capital repayment as interest or duplicate finance costs in running expenses. The result is rental tax, not total household Income Tax.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
