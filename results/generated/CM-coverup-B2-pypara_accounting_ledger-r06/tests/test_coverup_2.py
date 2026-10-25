# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

from datetime import date
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Amount, Quantity


def test_last_balance_returns_initial_value_when_ledger_is_empty():
    account = object()
    initial_value = Quantity(Decimal("100.00"))
    ledger = Ledger(
        account=account,
        initial=Balance(date(2024, 1, 1), initial_value),
    )

    assert ledger.entries == []
    assert ledger._last_balance == initial_value


def test_add_appends_entries_and_uses_previous_entry_balance():
    account = object()
    journal = object()
    ledger = Ledger(
        account=account,
        initial=Balance(
            date(2024, 1, 1),
            Quantity(Decimal("100.00")),
        ),
    )
    increment = Posting(
        journal=journal,
        date=date(2024, 1, 2),
        account=account,
        direction=Direction.INC,
        amount=Amount(Decimal("25.00")),
    )
    decrement = Posting(
        journal=journal,
        date=date(2024, 1, 3),
        account=account,
        direction=Direction.DEC,
        amount=Amount(Decimal("5.00")),
    )

    first_entry = ledger.add(increment)
    second_entry = ledger.add(decrement)

    assert first_entry.ledger is ledger
    assert first_entry.posting is increment
    assert first_entry.balance == Decimal("125.00")
    assert second_entry.ledger is ledger
    assert second_entry.posting is decrement
    assert second_entry.balance == Decimal("120.00")
    assert ledger.entries == [first_entry, second_entry]
    assert ledger._last_balance == Decimal("120.00")
