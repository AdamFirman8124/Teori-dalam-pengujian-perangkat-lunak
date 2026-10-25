# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

from datetime import date
from decimal import Decimal

from pypara.accounting.accounts import COA
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import build_general_ledger
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


def _coa_with_accounts():
    ## Default root accounts get codes "1".."5" for ASSETS..EXPENSES:
    coa = COA()
    assets = coa.add("1", "1000", "Cash")
    revenue = coa.add("4", "4000", "Sales")
    expenses = coa.add("5", "5000", "Rent")
    return coa, assets, revenue, expenses


def test_build_general_ledger_with_initial_balances_and_postings():
    period = DateRange(date(2021, 1, 1), date(2021, 12, 31))

    ## Accounts:
    coa, assets, revenue, expenses = _coa_with_accounts()

    ## Initial (opening) balances:
    initial = {assets: Balance(period.since, Quantity(Decimal("100")))}

    ## Journal entries: one inside the period, two outside (must be filtered out):
    inside = JournalEntry(date(2021, 6, 15), "Sale", None)
    inside.post(date(2021, 6, 15), assets, Quantity(Decimal("50")))
    inside.post(date(2021, 6, 15), revenue, Quantity(Decimal("50")))

    before = JournalEntry(date(2020, 12, 31), "Too early", None)
    before.post(date(2020, 12, 31), expenses, Quantity(Decimal("10")))

    after = JournalEntry(date(2022, 1, 1), "Too late", None)
    after.post(date(2022, 1, 1), expenses, Quantity(Decimal("20")))

    gl = build_general_ledger(period, [before, inside, after], initial)

    ## Postconditions:
    assert gl.period == period

    ## Only accounts touched by in-period postings or initial balances appear:
    assert set(gl.ledgers) == {assets, revenue}
    assert expenses not in gl.ledgers

    ## Ledger seeded from the initial balance:
    assets_ledger = gl.ledgers[assets]
    assert assets_ledger.account == assets
    assert assets_ledger.initial == Balance(period.since, Quantity(Decimal("100")))
    assert len(assets_ledger.entries) == 1
    assert assets_ledger.entries[-1].balance == Quantity(Decimal("150"))

    ## Ledger created on the fly for an account without an initial balance:
    revenue_ledger = gl.ledgers[revenue]
    assert revenue_ledger.account == revenue
    assert revenue_ledger.initial == Balance(period.since, Quantity(Decimal("0")))
    assert len(revenue_ledger.entries) == 1
    assert revenue_ledger.entries[-1].balance == Quantity(Decimal("50"))


def test_build_general_ledger_empty_journal_and_no_initial():
    period = DateRange(date(2021, 1, 1), date(2021, 12, 31))

    gl = build_general_ledger(period, [], {})

    ## Postconditions:
    assert gl.period == period
    assert gl.ledgers == {}


def test_build_general_ledger_decrement_on_new_account():
    period = DateRange(date(2021, 1, 1), date(2021, 12, 31))

    ## Accounts:
    coa, assets, revenue, expenses = _coa_with_accounts()

    entry = JournalEntry(date(2021, 3, 1), "Payment", None)
    entry.post(date(2021, 3, 1), assets, Quantity(Decimal("-30")))

    gl = build_general_ledger(period, [entry], {})

    ## Postconditions:
    assert set(gl.ledgers) == {assets}
    ledger = gl.ledgers[assets]
    assert ledger.initial == Balance(period.since, Quantity(Decimal("0")))
    assert len(ledger.entries) == 1
    assert ledger.entries[-1].balance == Quantity(Decimal("-30"))
