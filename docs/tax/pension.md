# Pension Withdrawal

Use Pension Withdrawal to explore a gross annual withdrawal with an entered tax-free percentage and other income. The percentage is an assumption, not a verified entitlement.

## Open and save a scenario

1. Select **Tax Scenarios → Pension Withdrawal**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Total pension withdrawal before tax £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Your other taxable income this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Tax-free portion % | Optional; default 25. HTML 0–100 step .1; server engine clamps to 0–100 rather than rejecting out-of-range input. | Entered assumption, not entitlement calculation; gross withdrawal × percent treated as tax free. |

## Calculation and dependencies

The tax-free amount is gross withdrawal × entered percentage. Remaining taxable withdrawal is stacked after other income using remaining Personal Allowance and the stored main rates. The engine clamps the tax-free percentage to 0–100; the normal form also provides that range. Net withdrawal is gross less estimated tax.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

In 2026/27, withdrawal £10,000, tax-free portion 25% and other income £30,000 produce **£1,500 estimated Income Tax** and **£8,500 net withdrawal** in the model.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

Lump-sum allowances/caps, MPAA, scheme-specific rights, emergency PAYE codes and death-benefit rules are not modelled. The default 25% is not a statement that you can take that share tax-free. Confirm your own entitlement separately.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
