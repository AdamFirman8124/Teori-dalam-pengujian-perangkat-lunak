# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry


def test_last_balance_empty_returns_initial_value():
    account = MagicMock()
    initial = Balance(date=datetime.date(2023, 1, 1), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    assert ledger.entries == []
    assert ledger._last_balance == Decimal("100")
    assert ledger._last_balance == initial.value


def test_add_first_entry_uses_initial_balance():
    account = MagicMock()
    initial = Balance(date=datetime.date(2023, 1, 1), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    journal = JournalEntry(date=datetime.date(2023, 1, 2), description="first", source="src-1")
    posting = Posting(
        journal=journal,
        date=datetime.date(2023, 1, 2),
        account=account,
        direction=Direction.INC,
        amount=Decimal("25"),
    )
    entry = ledger.add(posting)
    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Decimal("125")
    assert len(ledger.entries) == 1
    assert ledger.entries[0] is entry
    assert ledger._last_balance == Decimal("125")


def test_add_second_entry_uses_last_balance():
    account = MagicMock()
    initial = Balance(date=datetime.date(2023, 1, 1), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    journal = JournalEntry(date=datetime.date(2023, 1, 2), description="multi", source="src-2")
    posting1 = Posting(
        journal=journal,
        date=datetime.date(2023, 1, 2),
        account=account,
        direction=Direction.INC,
        amount=Decimal("50"),
    )
    entry1 = ledger.add(posting1)
    assert entry1.balance == Decimal("150")
    assert ledger._last_balance == Decimal("150")
    assert ledger._last_balance == entry1.balance

    posting2 = Posting(
        journal=journal,
        date=datetime.date(2023, 1, 3),
        account=account,
        direction=Direction.DEC,
        amount=Decimal("30"),
    )
    entry2 = ledger.add(posting2)
    assert entry2.ledger is ledger
    assert entry2.posting is posting2
    assert entry2.balance == Decimal("120")
    assert len(ledger.entries) == 2
    assert ledger.entries[0] is entry1
    assert ledger.entries[1] is entry2
    assert ledger._last_balance == Decimal("120")
    assert ledger._last_balance == entry2.balance
