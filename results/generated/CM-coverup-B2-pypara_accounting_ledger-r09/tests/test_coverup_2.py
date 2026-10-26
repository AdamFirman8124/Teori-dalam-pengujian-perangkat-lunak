# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Quantity


class _StubAccount:
    """Minimal stand-in satisfying the Account protocol."""

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None


def _make_posting(account: Account, direction: Direction, amount: Decimal) -> Posting:
    journal = JournalEntry(datetime.date(2024, 1, 1), "test entry", None)
    return Posting(journal, datetime.date(2024, 1, 1), account, direction, amount)


def test_last_balance_falls_back_to_initial_when_empty():
    """Lines 127-130: an empty ledger must return the initial balance value."""
    account = _StubAccount("100", "Cash")
    initial_value = Quantity(Decimal("500"))
    ledger = Ledger(account, Balance(datetime.date(2024, 1, 1), initial_value))

    assert ledger.entries == []
    assert ledger._last_balance == initial_value


def test_add_creates_entry_and_updates_balance():
    """Lines 140-146: add() must create a LedgerEntry, append it, and return it."""
    account = _StubAccount("100", "Cash")
    ledger = Ledger(account, Balance(datetime.date(2024, 1, 1), Quantity(Decimal("500"))))

    posting = _make_posting(account, Direction.DEC, Decimal("200"))
    entry = ledger.add(posting)

    # The returned entry is a LedgerEntry linked to this ledger and posting.
    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting

    # Balance: initial 500 - 200 = 300.
    assert entry.balance == Quantity(Decimal("300"))

    # The entry was appended to the ledger buffer.
    assert ledger.entries == [entry]

    # A second add must chain on the last balance (covers the non-IndexError path too).
    posting2 = _make_posting(account, Direction.INC, Decimal("50"))
    entry2 = ledger.add(posting2)
    assert entry2.balance == Quantity(Decimal("350"))
    assert ledger.entries == [entry, entry2]
    assert ledger._last_balance == Quantity(Decimal("350"))
