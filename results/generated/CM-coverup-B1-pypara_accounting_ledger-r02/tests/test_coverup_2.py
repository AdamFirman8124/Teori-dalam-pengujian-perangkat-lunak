# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Quantity


def test_last_balance_uses_initial_balance_when_ledger_is_empty():
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("10.00")))
    ledger = Ledger(account=object(), initial=initial)

    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("10.00"))


def test_add_appends_entries_and_uses_previous_entry_balance():
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("10.00")))
    ledger = Ledger(account=object(), initial=initial)
    increase = SimpleNamespace(
        amount=Decimal("2.50"),
        direction=Direction.INC,
    )
    decrease = SimpleNamespace(
        amount=Decimal("3.00"),
        direction=Direction.DEC,
    )

    first_entry = ledger.add(increase)
    second_entry = ledger.add(decrease)

    assert ledger.entries == [first_entry, second_entry]
    assert first_entry.ledger is ledger
    assert first_entry.posting is increase
    assert first_entry.balance == Quantity(Decimal("12.50"))
    assert second_entry.ledger is ledger
    assert second_entry.posting is decrease
    assert second_entry.balance == Quantity(Decimal("9.50"))
    assert ledger._last_balance == Quantity(Decimal("9.50"))
