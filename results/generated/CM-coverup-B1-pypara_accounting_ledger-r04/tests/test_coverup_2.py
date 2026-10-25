# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def test_last_balance_returns_initial_value_for_empty_ledger():
    account = object()
    initial = Balance(
        date=datetime.date(2024, 1, 1),
        value=Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=account, initial=initial)

    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("100.00"))


def test_add_appends_entries_and_uses_previous_balance():
    account = object()
    ledger = Ledger(
        account=account,
        initial=Balance(
            date=datetime.date(2024, 1, 1),
            value=Quantity(Decimal("100.00")),
        ),
    )
    increment = Posting(
        journal=None,
        date=datetime.date(2024, 1, 2),
        account=account,
        direction=Direction.INC,
        amount=Amount(Decimal("25.00")),
    )
    decrement = Posting(
        journal=None,
        date=datetime.date(2024, 1, 3),
        account=account,
        direction=Direction.DEC,
        amount=Amount(Decimal("10.00")),
    )

    first_entry = ledger.add(increment)
    second_entry = ledger.add(decrement)

    assert isinstance(first_entry, LedgerEntry)
    assert isinstance(second_entry, LedgerEntry)
    assert ledger.entries == [first_entry, second_entry]
    assert first_entry.ledger is ledger
    assert first_entry.posting is increment
    assert first_entry.balance == Quantity(Decimal("125.00"))
    assert second_entry.ledger is ledger
    assert second_entry.posting is decrement
    assert second_entry.balance == Quantity(Decimal("115.00"))
    assert ledger._last_balance == Quantity(Decimal("115.00"))
