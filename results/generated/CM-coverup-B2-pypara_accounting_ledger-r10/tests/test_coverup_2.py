# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry


def _make_account():
    return MagicMock()


def _make_initial(value="100"):
    return Balance(date=datetime.date(2023, 1, 1), value=Decimal(value))


def _make_journal():
    return JournalEntry(
        date=datetime.date(2023, 1, 2),
        description="test journal",
        source="test-source",
    )


def _make_posting(account, direction, amount, journal=None, date=None):
    if journal is None:
        journal = _make_journal()
    if date is None:
        date = datetime.date(2023, 1, 2)
    return Posting(
        journal=journal,
        date=date,
        account=account,
        direction=direction,
        amount=Decimal(amount),
    )


def test_last_balance_empty_returns_initial_value():
    account = _make_account()
    initial = _make_initial("100")
    ledger = Ledger(account=account, initial=initial)
    assert ledger.entries == []
    assert ledger._last_balance == Decimal("100")
    assert ledger._last_balance == initial.value


def test_last_balance_with_existing_entry_returns_last_balance():
    account = _make_account()
    initial = _make_initial("100")
    ledger = Ledger(account=account, initial=initial)
    journal = _make_journal()
    posting = _make_posting(account, Direction.INC, "50", journal=journal)
    seeded = LedgerEntry(ledger=ledger, posting=posting, balance=Decimal("150"))
    ledger.entries.append(seeded)
    try:
        assert ledger._last_balance == Decimal("150")
        assert ledger._last_balance == ledger.entries[-1].balance
    finally:
        ledger.entries.clear()


def test_add_first_posting_uses_initial_balance():
    account = _make_account()
    initial = _make_initial("100")
    ledger = Ledger(account=account, initial=initial)
    journal = _make_journal()
    posting = _make_posting(account, Direction.INC, "25", journal=journal)
    try:
        entry = ledger.add(posting)
        assert isinstance(entry, LedgerEntry)
        assert entry.ledger is ledger
        assert entry.posting is posting
        assert entry.balance == Decimal("125")
        assert ledger.entries == [entry]
        assert ledger._last_balance == Decimal("125")
    finally:
        ledger.entries.clear()


def test_add_chains_balances_and_handles_dec_direction():
    account = _make_account()
    initial = _make_initial("100")
    ledger = Ledger(account=account, initial=initial)
    journal = _make_journal()
    posting1 = _make_posting(account, Direction.INC, "20", journal=journal)
    posting2 = _make_posting(account, Direction.DEC, "30", journal=journal)
    try:
        entry1 = ledger.add(posting1)
        assert entry1.balance == Decimal("120")
        assert ledger._last_balance == Decimal("120")
        entry2 = ledger.add(posting2)
        assert entry2.ledger is ledger
        assert entry2.posting is posting2
        # 120 + (30 * -1) = 90
        assert entry2.balance == Decimal("90")
        assert ledger.entries == [entry1, entry2]
        assert ledger.entries[-1] is entry2
        assert ledger._last_balance == Decimal("90")
        assert len(ledger.entries) == 2
    finally:
        ledger.entries.clear()
