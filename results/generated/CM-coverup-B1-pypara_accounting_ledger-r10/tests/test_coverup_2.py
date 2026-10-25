# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Amount, Quantity


class StubAccount:
    """Minimal stub satisfying the Account protocol."""

    def __init__(self):
        self._code = "100"
        self._name = "Cash"
        self._type = None
        self._coa = None
        self._parent = None

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def coa(self):
        return self._coa

    @property
    def parent(self):
        return self._parent


def _make_posting(account, direction, amount):
    journal = JournalEntry(datetime.date(2021, 1, 1), "test entry", None)
    return Posting(journal, datetime.date(2021, 1, 1), account, direction, Amount(amount))


def test_last_balance_empty_returns_initial():
    account = StubAccount()
    initial = Balance(datetime.date(2021, 1, 1), Quantity(Decimal("100")))
    ledger = Ledger(account, initial)
    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("100"))


def test_last_balance_nonempty_returns_last_entry_balance():
    account = StubAccount()
    initial = Balance(datetime.date(2021, 1, 1), Quantity(Decimal("100")))
    ledger = Ledger(account, initial)
    inc = Direction.of(Decimal("1"))
    dec = Direction.of(Decimal("-1"))
    first = ledger.add(_make_posting(account, inc, Decimal("50")))
    assert ledger._last_balance == first.balance
    assert first.balance == Quantity(Decimal("100") + Decimal("50") * inc.value)
    second = ledger.add(_make_posting(account, dec, Decimal("20")))
    assert ledger._last_balance == second.balance
    assert second.balance == Quantity(first.balance + Decimal("20") * dec.value)
    assert ledger.entries == [first, second]


def test_add_appends_and_returns_entry():
    account = StubAccount()
    initial = Balance(datetime.date(2021, 1, 1), Quantity(Decimal("200")))
    ledger = Ledger(account, initial)
    inc = Direction.of(Decimal("1"))
    posting = _make_posting(account, inc, Decimal("25"))
    expected = Quantity(Decimal("200") + Decimal("25") * inc.value)
    entry = ledger.add(posting)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == expected
    assert len(ledger.entries) == 1
    assert ledger.entries[0] is entry
    assert ledger._last_balance == expected
