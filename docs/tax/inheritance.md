# Inheritance Tax

Estimate a simplified estate liability and indicative beneficiary shares. Use the Inheritance tab for estate-planning comparisons, not probate reporting.

## Open and save a scenario

1. Select **Tax Scenarios → Inheritance**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26–2030/31; default **2026/27**.
3. Enter estate asset/fund values and outstanding debt balances—not annual income or monthly mortgage payments. Gifts is the total relevant amount over the previous seven years. Monetary fields default to zero, allow blank as zero and reject negative amounts; the tax year chooses the stored ruleset.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28, 2028/29, 2029/30, 2030/31. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Notes | Optional; default Blank. Surrounding spaces removed; blank means no note. | Stores assumptions; IHT only: general tax models have no Notes input. |
| Property value £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Cash and savings £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Investments £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Pensions / death benefits £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Other assets £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Debts and mortgages £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Money left to charity £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Home value passing to children/grandchildren £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Relevant gifts made in the previous 7 years £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Residence passes to direct descendants | Optional; checked by default. Checked enables this assumption; cleared disables it. | When checked and qualifying residence >0, makes residence nil-rate band eligible before taper. |
| Unused spouse/civil-partner allowance % | Optional; default 0. Whole-number percentage from 0 to 100. | Increases base NRB by this percentage. |
| Unused spouse/civil partner residence nil-rate band transferred % | Optional; default 0. Whole-number percentage from 0 to 100. | Increases base RNRB by this percentage before residence cap and taper. |
| Beneficiary 1 | Optional; default Blank. Optional label; a blank leaves it unnamed. | Label for displayed estimated share; there are two beneficiary slots. |
| Beneficiary 2 | Optional; default Blank. Optional label; a blank leaves it unnamed. | Label for displayed estimated share; there are two beneficiary slots. |
| Beneficiary 1 Share % | Optional; default 50. 0–100%, in 0.1 increments. The two shares together must not exceed 100% (apart from tiny rounding tolerance); they need not total 100%. | Applies percentage to estimated estate after charity and IHT. |
| Beneficiary 2 Share % | Optional; default 50. 0–100%, in 0.1 increments. The two shares together must not exceed 100% (apart from tiny rounding tolerance); they need not total 100%. | Applies percentage to estimated estate after charity and IHT. |

## Calculation and dependencies

Gross estate adds property, cash, investments and other assets. The bundled rules add pensions/death benefits from **2027/28** onward. Net estate is gross less debts, floored at zero. The standard nil-rate band is £325,000, increased by the entered transferred percentage and reduced by entered chargeable gifts.

When the direct-descendants box is checked, the residence band is limited by the entered qualifying home value and a £175,000 base increased by the transferred percentage. The model tapers that band by £1 for every £2 of net estate above £2 million. Taxable estate is net estate less charity and available bands, floored at zero; estimated IHT is 40% of that amount. Distributable estate is net less charity and IHT. Each beneficiary's displayed amount follows their entered percentage; shares may total less than 100% but cannot exceed it.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

Property £600,000, cash £200,000, investments £100,000, pensions £100,000, debts £100,000, qualifying home £600,000, direct descendants checked, and no gifts/charity/transferred bands produce **£120,000 estimated IHT for 2026/27**. Choosing 2027/28 in this stored model produces **£160,000**, illustrating its pension-year assumption—not verification of future legislation.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

There is no date-of-death field or manual pensions-in-estate checkbox in this UI. Tax year chooses the treatment. No gift-by-gift taper, reduced charitable 36% rate, business/agricultural relief, trusts or comprehensive spouse exemption is modelled. The form does not ensure qualifying home value is no greater than the entered property value; check it yourself. Beneficiary names/shares describe the estimate, not legal inheritance rights.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/inheritance-tax) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
