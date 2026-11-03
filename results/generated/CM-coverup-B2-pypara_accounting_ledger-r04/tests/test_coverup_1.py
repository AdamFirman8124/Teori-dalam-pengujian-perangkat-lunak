# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

from datetime import date
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, Ledger, build_general_ledger
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


class MockAccount:
    """
    Minimal concrete account satisfying the ``Account`` protocol.

    The code under test only uses accounts as dictionary keys, so default
    identity-based hashing/equality is sufficient. The test creates no global
    state (no files, no patches, no singletons), hence no teardown/monkeypatching
    is required; everything is garbage-collected with the test objects.
    """

    def __init__(self, code: str, name: str) -> None:
        self._code = code
        self._name = name

    @property
    def code(self) -> str:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self):
        return None

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None


def test_build_general_ledger_seeds_initial_balances_and_accumulates_in_period_postings():
    """
    Covers lines 174-186: ledgers are seeded from initial balances, in-period
    postings are accumulated (creating ledgers on the fly when an account has
    no opening balance), and out-of-period journal entries are ignored.
    """
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))
    cash = MockAccount("1000", "Cash")
    sales = MockAccount("4000", "Sales")
    capital = MockAccount("3000", "Capital")
    future = MockAccount("9000", "Future")

    ## Line 174: seed ledgers from initial balances (only `cash` has one).
    initial = {cash: Balance(period.since, Quantity(Decimal("100")))}

    ## Line 177 (true branch) and line 183: an in-period entry.
    entry_in_period = JournalEntry(date(2024, 6, 15), "Sale", None)
    entry_in_period.post(date(2024, 6, 15), cash, Quantity(Decimal("100")))
    entry_in_period.post(date(2024, 6, 15), sales, Quantity(Decimal("-100")))

    ## Boundary: an entry dated exactly on `period.until` is still included, and
    ## lines 179-180 create ledgers for accounts without initial balances.
    entry_on_last_day = JournalEntry(date(2024, 12, 31), "Year-end adjustment", None)
    entry_on_last_day.post(date(2024, 12, 31), capital, Quantity(Decimal("500")))
    entry_on_last_day.post(date(2024, 12, 31), cash, Quantity(Decimal("-500")))

    ## Line 177 (false branch): an entry outside the period must be filtered out.
    entry_out_of_period = JournalEntry(date(2025, 1, 15), "Future sale", None)
    entry_out_of_period.post(date(2025, 1, 15), cash, Quantity(Decimal("50")))
    entry_out_of_period.post(date(2025, 1, 15), future, Quantity(Decimal("-50")))

    ## Line 186: the general ledger is built and returned.
    result = build_general_ledger(
        period, [entry_in_period, entry_on_last_day, entry_out_of_period], initial
    )

    ## Postconditions:
    assert isinstance(result, GeneralLedger)
    assert result.period == period

    ## Only accounts touched by in-period postings (plus the seeded one) appear;
    ## the out-of-period entry left no trace whatsoever.
    assert set(result.ledgers.keys()) == {cash, sales, capital}
    assert future not in result.ledgers

    ## `cash` ledger was pre-created from the initial balance (line 174)...
    cash_ledger = result.ledgers[cash]
    assert isinstance(cash_ledger, Ledger)
    assert cash_ledger.account is cash
    assert cash_ledger.initial == Balance(period.since, Quantity(Decimal("100")))

    ## ...and received both in-period postings (line 183), with debits adding to
    ## and credits subtracting from the running balance.
    assert len(cash_ledger.entries) == 2
    assert cash_ledger.entries[0].posting is entry_in_period.postings[0]
    assert cash_ledger.entries[0].balance == Quantity(Decimal("200"))
    assert cash_ledger.entries[1].posting is entry_on_last_day.postings[1]
    assert cash_ledger.entries[1].balance == Quantity(Decimal("-300"))

    ## `sales` ledger was created on the fly with a zero opening balance (lines 179-180).
    sales_ledger = result.ledgers[sales]
    assert isinstance(sales_ledger, Ledger)
    assert sales_ledger.account is sales
    assert sales_ledger.initial == Balance(period.since, Quantity(Decimal(0)))
    assert len(sales_ledger.entries) == 1
    assert sales_ledger.entries[0].posting is entry_in_period.postings[1]
    assert sales_ledger.entries[0].balance == Quantity(Decimal("-100"))

    ## `capital` ledger was also created on the fly (lines 179-180).
    capital_ledger = result.ledgers[capital]
    assert capital_ledger.account is capital
    assert capital_ledger.initial == Balance(period.since, Quantity(Decimal(0)))
    assert len(capital_ledger.entries) == 1
    assert capital_ledger.entries[0].posting is entry_on_last_day.postings[0]
    assert capital_ledger.entries[0].balance == Quantity(Decimal("500"))

    ## No ledger entry originates from the out-of-period journal entry.
    assert all(
        entry.posting.journal is not entry_out_of_period
        for ledger in result.ledgers.values()
        for entry in ledger.entries
    )


def test_build_general_ledger_with_empty_journal_and_no_initial_balances():
    """
    Covers lines 174, 177 and 186 with empty inputs: the resulting general
    ledger must simply be empty.
    """
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))

    result = build_general_ledger(period, [], {})

    assert isinstance(result, GeneralLedger)
    assert result.period == period
    assert result.ledgers == {}
