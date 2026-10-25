# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def _make_ledger(initial_value="100.00"):
    account = SimpleNamespace(code="1000", name="Cash")
    initial = Balance(
        date=datetime.date(2024, 1, 1),
        value=Quantity(Decimal(initial_value)),
    )
    return Ledger(account=account, initial=initial)


def _make_posting(account, direction, amount, day=2):
    return Posting(
        journal=None,
        date=datetime.date(2024, 1, day),
        account=account,
        direction=direction,
        amount=Amount(Decimal(amount)),
    )


def test_last_balance_empty_returns_initial_value():
    ledger = _make_ledger("100.00")
    try:
        assert ledger.entries == []
        assert ledger._last_balance == Quantity(Decimal("100.00"))
        assert ledger._last_balance == ledger.initial.value
    finally:
        ledger.entries.clear()


def test_last_balance_with_entries_returns_last_entry_balance():
    ledger = _make_ledger("100.00")
    try:
        posting = _make_posting(ledger.account, Direction.INC, "50.00")
        entry = LedgerEntry(
            ledger=ledger,
            posting=posting,
            balance=Quantity(Decimal("150.00")),
        )
        ledger.entries.append(entry)

        assert ledger._last_balance == Quantity(Decimal("150.00"))
        assert ledger._last_balance == entry.balance
    finally:
        ledger.entries.clear()


def test_add_first_posting_increment_uses_initial_balance():
    ledger = _make_ledger("100.00")
    try:
        posting = _make_posting(ledger.account, Direction.INC, "25.50")

        entry = ledger.add(posting)

        assert isinstance(entry, LedgerEntry)
        assert entry.ledger is ledger
        assert entry.posting is posting
        assert entry.balance == Quantity(Decimal("125.50"))
        assert ledger.entries == [entry]
        assert ledger.entries[-1] is entry
        assert ledger._last_balance == Quantity(Decimal("125.50"))
    finally:
        ledger.entries.clear()


def test_add_first_posting_decrement_uses_initial_balance():
    ledger = _make_ledger("100.00")
    try:
        posting = _make_posting(ledger.account, Direction.DEC, "40.00")

        entry = ledger.add(posting)

        assert isinstance(entry, LedgerEntry)
        assert entry.ledger is ledger
        assert entry.posting is posting
        assert entry.balance == Quantity(Decimal("60.00"))
        assert ledger.entries == [entry]
        assert ledger._last_balance == Quantity(Decimal("60.00"))
    finally:
        ledger.entries.clear()


def test_add_second_posting_uses_last_balance_not_initial():
    ledger = _make_ledger("100.00")
    try:
        first_posting = _make_posting(ledger.account, Direction.INC, "25.50", day=2)
        second_posting = _make_posting(ledger.account, Direction.DEC, "10.50", day=3)

        first_entry = ledger.add(first_posting)
        second_entry = ledger.add(second_posting)

        assert first_entry.balance == Quantity(Decimal("125.50"))
        assert second_entry.balance == Quantity(Decimal("115.00"))
        assert second_entry.ledger is ledger
        assert second_entry.posting is second_posting
        assert ledger.entries == [first_entry, second_entry]
        assert len(ledger.entries) == 2
        assert ledger._last_balance == Quantity(Decimal("115.00"))
    finally:
        ledger.entries.clear()
