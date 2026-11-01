# Savings Interest

Use Savings Interest for taxable annual interest alongside other annual income. It does not obtain interest certificates from your bank.

## Open and save a scenario

1. Select **Tax Scenarios → Savings Interest**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Total taxable savings interest for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Your other taxable income this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

The model uses remaining Personal Allowance, starting-rate room and a Personal Savings Allowance before taxing remaining interest. Its starting-rate room begins at £5,000 less other taxable income, floored at zero. Stored savings rates are 20%/40%/45% through 2026/27 and 22%/42%/47% in its 2027/28 assumptions.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

In 2026/27, interest £2,000 and other income £30,000 use £1,000 of the model's Personal Savings Allowance and return **£200 estimated savings tax**.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

The model selects the savings-allowance tier from other taxable income rather than all combined income and simplifies allowance/band interaction. Verify cases near thresholds independently. ISA interest is outside this model. There is no currency conversion or personal entitlement assessment.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
