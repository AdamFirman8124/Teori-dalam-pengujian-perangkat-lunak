# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from decimal import Decimal

from pypara.accounting.ledger import build_general_ledger
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry, Posting
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


class _DirectionStub:
    """
    Minimal stand-in for the journaling ``Direction`` enum.

    ``Ledger.add`` only needs ``posting.direction.value``, so a plain object with
    a numeric ``value`` is sufficient and avoids depending on the exact enum
    member names of the installed pypara version.
    """

    def __init__(self, value: Decimal):
        self.value = value

    def __repr__(self):
        return f"_DirectionStub({self.value})"


INCREASE = _DirectionStub(Decimal(1))
DECREASE = _DirectionStub(Decimal(-1))


class AccountStub:
    """Minimal duck-typed implementation of the Account protocol."""

    def __init__(self, code: str, name: str):
        self._code = code
        self._name = name

    @property
    def code(self):
        return self._code

    @property
    def name(self):
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


def _make_journal_entry(date: datetime.date, description: str = "test entry") -> JournalEntry:
    return JournalEntry(date=date, description=description, source=None)


def _make_posting(journal: JournalEntry, date: datetime.date, account: AccountStub,
                  direction, amount: Decimal) -> Posting:
    posting = Posting(journal=journal, date=date, account=account,
                      direction=direction, amount=amount)
    journal.postings.append(posting)
    return posting


def test_build_general_ledger_with_initial_balances_and_new_accounts():
    """
    Covers all target lines: initial ledger creation (174), journal iteration with
    period filtering (177), creation of ledgers for unseen accounts (179-180),
    adding postings (183), and returning the general ledger (186).
    """
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since=since, until=until)

    cash = AccountStub("100", "Cash")
    sales = AccountStub("400", "Sales")
    rent = AccountStub("500", "Rent")

    ## Journal entries: two inside the period, two outside (one before, one after):
    entry_in_1 = _make_journal_entry(datetime.date(2023, 3, 15))
    posting_cash_in = _make_posting(entry_in_1, datetime.date(2023, 3, 15), cash,
                                    INCREASE, Decimal("1000"))
    posting_sales_in = _make_posting(entry_in_1, datetime.date(2023, 3, 15), sales,
                                     DECREASE, Decimal("1000"))

    entry_in_2 = _make_journal_entry(datetime.date(2023, 6, 1))
    posting_rent_in = _make_posting(entry_in_2, datetime.date(2023, 6, 1), rent,
                                    INCREASE, Decimal("250"))

    entry_before = _make_journal_entry(datetime.date(2022, 12, 31))
    posting_before = _make_posting(entry_before, datetime.date(2022, 12, 31), cash,
                                   INCREASE, Decimal("99999"))

    entry_after = _make_journal_entry(datetime.date(2024, 1, 1))
    posting_after = _make_posting(entry_after, datetime.date(2024, 1, 1), cash,
                                  INCREASE, Decimal("88888"))

    journal = [entry_before, entry_in_1, entry_in_2, entry_after]

    initial = {cash: Balance(date=since, value=Quantity(Decimal("500")))}

    ledger = build_general_ledger(period, journal, initial)

    ## Postcondition: the returned general ledger carries the requested period:
    assert ledger.period == period

    ## Postcondition: ledgers exist for the initially-balanced account and for
    ## accounts seen in in-period postings only:
    assert set(ledger.ledgers.keys()) == {cash, sales, rent}

    ## Postcondition: the initially-balanced account keeps its opening balance
    ## and only the in-period posting was added:
    cash_ledger = ledger.ledgers[cash]
    assert cash_ledger.account is cash
    assert cash_ledger.initial == Balance(date=since, value=Quantity(Decimal("500")))
    assert len(cash_ledger.entries) == 1
    assert cash_ledger.entries[0].posting is posting_cash_in
    assert cash_ledger._last_balance == Quantity(Decimal("1500"))

    ## Postcondition: a ledger was created on the fly for the unseen account,
    ## with a zero opening balance dated at the period start:
    sales_ledger = ledger.ledgers[sales]
    assert sales_ledger.account is sales
    assert sales_ledger.initial == Balance(date=since, value=Quantity(Decimal("0")))
    assert len(sales_ledger.entries) == 1
    assert sales_ledger.entries[0].posting is posting_sales_in
    assert sales_ledger._last_balance == Quantity(Decimal("-1000"))

    ## Postcondition: the second in-period entry produced its own ledger:
    rent_ledger = ledger.ledgers[rent]
    assert rent_ledger.account is rent
    assert rent_ledger.initial == Balance(date=since, value=Quantity(Decimal("0")))
    assert len(rent_ledger.entries) == 1
    assert rent_ledger.entries[0].posting is posting_rent_in
    assert rent_ledger._last_balance == Quantity(Decimal("250"))

    ## Postcondition: out-of-period postings were filtered out entirely:
    all_postings = [e.posting for lgr in ledger.ledgers.values() for e in lgr.entries]
    assert posting_before not in all_postings
    assert posting_after not in all_postings
    assert len(all_postings) == 3


def test_build_general_ledger_with_initial_balances_only():
    """
    Covers the initial-ledger dict comprehension (174) and the return (186) when
    the journal contributes no in-period postings.
    """
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since=since, until=until)

    cash = AccountStub("100", "Cash")
    bank = AccountStub("101", "Bank")

    ## A journal entry entirely outside the period must be ignored:
    entry_outside = _make_journal_entry(datetime.date(2022, 6, 1))
    _make_posting(entry_outside, datetime.date(2022, 6, 1), cash,
                  INCREASE, Decimal("777"))

    initial = {
        cash: Balance(date=since, value=Quantity(Decimal("100"))),
        bank: Balance(date=since, value=Quantity(Decimal("200"))),
    }

    ledger = build_general_ledger(period, [entry_outside], initial)

    assert ledger.period == period
    assert set(ledger.ledgers.keys()) == {cash, bank}
    assert ledger.ledgers[cash].initial == Balance(date=since, value=Quantity(Decimal("100")))
    assert ledger.ledgers[bank].initial == Balance(date=since, value=Quantity(Decimal("200")))
    ## No in-period postings, so no ledger entries anywhere:
    assert all(len(lgr.entries) == 0 for lgr in ledger.ledgers.values())


def test_build_general_ledger_empty_inputs():
    """
    Covers the degenerate case: no initial balances and no journal entries,
    exercising the generator expression over an empty journal (177) and the
    return (186).
    """
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 1, 31)
    period = DateRange(since=since, until=until)

    ledger = build_general_ledger(period, [], {})

    assert ledger.period == period
    assert ledger.ledgers == {}
