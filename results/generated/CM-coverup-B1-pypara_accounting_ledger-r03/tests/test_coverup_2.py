# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.accounts import Account, AccountType, Code
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


class _Account:
    """Minimal concrete implementation of the Account protocol."""

    def __init__(self, code: str, name: str, type_: AccountType):
        self._code = Code(code)
        self._name = name
        self._type = type_

    @property
    def code(self) -> Code:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> AccountType:
        return self._type

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None


def _make_posting(account: Account, direction: Direction, amount: Amount) -> Posting:
    journal = JournalEntry(datetime.date(2024, 1, 1), "test entry", None)
    return Posting(journal, datetime.date(2024, 1, 1), account, direction, amount)


def test_last_balance_falls_back_to_initial_when_no_entries():
    """Lines 127-130: empty ledger returns the initial balance value."""
    account = _Account("100", "Cash", AccountType.ASSETS)
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100")))
    ledger = Ledger(account, initial)

    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("100"))


def test_last_balance_returns_last_entry_balance():
    """Lines 127-128: non-empty ledger returns the balance of the last entry."""
    account = _Account("100", "Cash", AccountType.ASSETS)
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100")))
    ledger = Ledger(account, initial)

    ledger.add(_make_posting(account, Direction.INC, Amount(Decimal("50"))))
    ledger.add(_make_posting(account, Direction.DEC, Amount(Decimal("20"))))

    assert len(ledger.entries) == 2
    assert ledger._last_balance == ledger.entries[-1].balance
    assert ledger._last_balance == Quantity(Decimal("130"))


def test_add_creates_and_appends_entry_debit():
    """Lines 140-146: add() computes balance, appends entry, and returns it (increment)."""
    account = _Account("100", "Cash", AccountType.ASSETS)
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100")))
    ledger = Ledger(account, initial)

    posting = _make_posting(account, Direction.INC, Amount(Decimal("50")))
    entry = ledger.add(posting)

    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("150"))
    assert ledger.entries == [entry]
    assert entry.date == posting.date
    assert entry.is_debit is True


def test_add_creates_and_appends_entry_credit():
    """Lines 140-146: add() computes balance, appends entry, and returns it (decrement)."""
    account = _Account("200", "Payables", AccountType.LIABILITIES)
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("300")))
    ledger = Ledger(account, initial)

    posting = _make_posting(account, Direction.DEC, Amount(Decimal("120")))
    entry = ledger.add(posting)

    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("180"))
    assert ledger.entries == [entry]
    assert entry.date == posting.date
    assert entry.is_credit is True
