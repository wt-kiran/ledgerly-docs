# How the financial plan fits together

Ledgerly separates **actual records**, **monthly planning commitments**, **saved wealth snapshots** and **hypothetical scenarios**. A number in one area does not automatically transfer cash or update another.

<div class="workflow"><strong>CSV transactions</strong> → <strong>Review & reconcile</strong> → <strong>Recurring + history</strong> → <strong>Plan</strong> → <strong>Goals</strong> → <strong>Allocate / Forecast</strong></div>

## Actual transactions

Overview and Reconciliation summarise imported income/expenses. Transfers between accounts are not another income/expense, and investment outflows are distinct from consumption. One-off treatment leaves actual spending intact but removes exceptional items from normal planning history.

## Monthly commitments

Recurring approves fixed bills and saving/investment with cadence converted to monthly equivalents. Plan adds expected income, variable-essential history/overrides, existing cash allocations and additional saving. An active additional Funded Goal is another reserve; a Tracking Goal is not.

## Capacity, context and allocation

Raw headroom is expected income after those commitments, before lifestyle. The selected historical lifestyle is a reference estimated from category medians. Allocate uses a deliberate lifestyle allowance and extra investing to leave a forward safety buffer. Plan's optional planned-lifestyle field is separate from Allocate's allowance; Forecast starts from the historical reference.

## Wealth and tax are separate

Wealth is a manually updated stock of assets and debt, not a monthly flow or automatic imported balance. Tax Scenarios are independently entered annual estimates. Neither silently changes Plan, makes payments or funds a goal.

## Forecast is hypothetical

Saved Forecast changes recalculate against the current Plan and do not replace it. To adopt a decision, explicitly change the real underlying inputs.

Read the [worked monthly example](example.md) and [glossary](glossary.md). For detailed formulas, [Plan](../guide/plan.md), [Goals](../guide/goals.md) and [Allocate](../guide/allocate.md) are the primary guides.
