# Property Sale / Capital Gains Tax

Explore a simplified annual property disposal using the Property Sale / CGT tab. It does not establish that a sale is taxable or calculate home-specific relief.

## Open and save a scenario

1. Select **Tax Scenarios → Property Sale / Capital Gains Tax**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Sale price £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| What you paid for it £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Buying costs £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Lasting improvements £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Selling costs £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Capital losses you can use £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Your other taxable income this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

Cost basis adds purchase price, buying costs, lasting improvements and selling costs. Gain is sale proceeds less basis and usable losses, floored at zero. The bundled annual exempt amount is £3,000. Remaining gain is split between the model's available lower-rate band and higher rate after other entered taxable income; stored CGT rates are 18% and 24%.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

Sale £50,000 and purchase £40,000, with other fields zero in 2026/27, produce a £10,000 gain, £7,000 taxable after the model's £3,000 exemption, and **£1,260 estimated CGT**.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

No Private Residence Relief, lettings/business relief, non-resident rules or trusts are calculated. Do not enter a main-home sale and assume this estimate includes the relief you may need. Other income is annual income for band context, not another gain. High-income band-edge calculations remain simplified.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/capital-gains-tax/rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
