# Combined Income

Use Combined Income when employment, rental profit, savings interest and dividends need to share allowances within one simplified annual comparison.

## Open and save a scenario

1. Select **Tax Scenarios → Combined Income**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Gross employment income for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Rent received this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Property running costs £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Taxable savings interest for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Dividend income for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

Property profit is max(0, rent − expenses). The model allocates the Personal Allowance in order to employment, property, savings and dividends, then applies its stored bands/starting-rate and allowances. The headline is total estimated **Income Tax only**. Employee NI is deliberately excluded; it is included in Salary / Bonus instead.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

For 2026/27, employment £30,000, rent £12,000, expenses £2,000, interest £2,000 and dividends £1,000 return **£5,739.75 estimated total Income Tax** in v3.8.5.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

No separate bonus, pension, other-income or finance-cost input is offered in this combined form. It inherits the simplified savings/dividend/band interactions of the individual models. Do not add standalone tax totals mechanically or assume this combined estimate includes NI, specialist reliefs or every source of taxable income.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
