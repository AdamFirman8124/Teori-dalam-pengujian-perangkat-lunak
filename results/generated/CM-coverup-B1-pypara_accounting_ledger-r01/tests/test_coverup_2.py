# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Amount, Quantity


def test_ledger_add_uses_initial_then_latest_balance() -> None:
    account = object()
    journal = object()
    date = datetime.date(2024, 1, 1)
    ledger = Ledger(
        account=account,
        initial=Balance(date=date, value=Quantity(Decimal("100"))),
    )

    increment = Posting(
        journal=journal,
        date=date,
        account=account,
        direction=Direction.INC,
        amount=Amount(Decimal("25")),
    )
    first_entry = ledger.add(increment)

    assert first_entry.ledger is ledger
    assert first_entry.posting is increment
    assert first_entry.balance == Decimal("125")
    assert ledger.entries == [first_entry]
    assert ledger._last_balance == Decimal("125")

    decrement = Posting(
        journal=journal,
        date=date,
        account=account,
        direction=Direction.DEC,
        amount=Amount(Decimal("5")),
    )
    second_entry = ledger.add(decrement)

    assert second_entry.ledger is ledger
    assert second_entry.posting is decrement
    assert second_entry.balance == Decimal("120")
    assert ledger.entries == [first_entry, second_entry]
    assert ledger._last_balance == Decimal("120")
