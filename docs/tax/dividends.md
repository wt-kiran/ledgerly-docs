# Dividend Income

Use Dividend Income for entered annual taxable dividends alongside other income. It does not import portfolio records or calculate ISA eligibility.

## Open and save a scenario

1. Select **Tax Scenarios → Dividend Income**. The tab labels may abbreviate Capital Gains Tax as CGT.
2. Enter a name and choose 2025/26, 2026/27 or 2027/28; default **2026/27**.
3. Enter the annual assumptions below. Monetary fields default to zero, allow blank as zero and reject negative amounts. Do not copy monthly values into annual fields.
4. Select **Save & calculate**. Read the headline, waterfall and displayed assumptions.
5. On a saved scenario use **Edit assumptions / Save changes** to revise it, or **Archive** to hide it. No archive-restore button is provided.

## Every field

| Field | Required, default and validation | Effect |
|---|---|---|
| Scenario name | Required; default Blank. Cannot be blank after surrounding spaces are removed. | Identifies saved scenario; does not alter actual accounts or Plan. |
| Tax year | Required; default 2026/27. Must be in the supported list for this scenario. Choices: 2025/26, 2026/27, 2027/28. | Selects a fixed bundled ruleset, not a live HMRC lookup. |
| Total dividend income for the tax year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |
| Your other taxable income this year £ | Optional; default 0.00. Blank becomes zero. Zero or positive; £ and grouping commas accepted. Rounded to the nearest penny. | Changes this scenario only. |

## Calculation and dependencies

The model tapers the Personal Allowance using entered total income, allocates it first against other income, then uses any remainder and a stored £500 dividend allowance. It taxes remaining dividends at the stored year's bands. Rates are 8.75%/33.75%/39.35% for 2025/26 and 10.75%/35.75%/39.35% for the later offered years.

Saved results recalculate from their entered assumptions; they do not import Wealth values or change Plan, bank transactions or a real tax payment. Financial values are rounded to pence. The bundled rules do not refresh from the internet.

## Worked application example

2026/27 dividends £1,000 and other income £30,000 leave £500 taxable in the model's lower dividend band and return **£53.75 estimated dividend tax**.

This is an executed example of the v3.8.5 model, not independent confirmation of a legal liability.

## Limits and common mistakes

This is a simplified band-stacking model: the implementation removes allowance amounts before some band positioning, even though exempt-rate income can affect real tax bands. Do not treat boundary cases as independently verified. ISA dividends are outside this model; the form does not test account exemption.

For any substantial decision, check current [HMRC guidance](https://www.gov.uk/income-tax-rates) and suitable professional advice. The [tax overview](index.md) explains shared limitations. Related: [FAQ](../faq.md#planning-and-tax), [tax troubleshooting](../troubleshooting.md#tax-or-wealth-results-look-surprising), [known limitations](../limitations.md).
