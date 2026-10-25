# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def test_last_balance_returns_initial_value_when_ledger_is_empty():
    account = object()
    initial_value = Quantity(Decimal("100.00"))
    ledger = Ledger(
        account=account,
        initial=Balance(date=date(2024, 1, 1), value=initial_value),
    )

    assert ledger.entries == []
    assert ledger._last_balance == initial_value


def test_add_appends_entries_and_uses_previous_entry_balance():
    account = object()
    ledger = Ledger(
        account=account,
        initial=Balance(
            date=date(2024, 1, 1),
            value=Quantity(Decimal("100.00")),
        ),
    )
    increment = SimpleNamespace(value=Decimal("1"))
    decrement = SimpleNamespace(value=Decimal("-1"))

    first_posting = Posting(
        journal=object(),
        date=date(2024, 1, 2),
        account=account,
        direction=increment,
        amount=Amount(Decimal("25.00")),
    )
    second_posting = Posting(
        journal=object(),
        date=date(2024, 1, 3),
        account=account,
        direction=decrement,
        amount=Amount(Decimal("10.00")),
    )

    first_entry = ledger.add(first_posting)
    second_entry = ledger.add(second_posting)

    assert isinstance(first_entry, LedgerEntry)
    assert first_entry.ledger is ledger
    assert first_entry.posting is first_posting
    assert first_entry.balance == Quantity(Decimal("125.00"))

    assert isinstance(second_entry, LedgerEntry)
    assert second_entry.ledger is ledger
    assert second_entry.posting is second_posting
    assert second_entry.balance == Quantity(Decimal("115.00"))

    assert ledger.entries == [first_entry, second_entry]
    assert ledger._last_balance == Quantity(Decimal("115.00"))
