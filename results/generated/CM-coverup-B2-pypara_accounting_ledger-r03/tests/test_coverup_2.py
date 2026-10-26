# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from unittest.mock import Mock

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Amount, Quantity


def _make_ledger(initial=100):
    return Ledger(
        account=Mock(),
        initial=Balance(
            date=datetime.date(2024, 1, 1),
            value=Quantity(initial),
        ),
    )


def _make_posting(amount, direction):
    return Posting(
        journal=Mock(),
        date=datetime.date(2024, 1, 2),
        account=Mock(),
        direction=direction,
        amount=Amount(amount),
    )


def test_last_balance_with_no_entries_returns_initial_value():
    ledger = _make_ledger(initial=100)

    assert ledger.entries == []
    assert ledger._last_balance == Quantity(100)
    assert ledger._last_balance == ledger.initial.value


def test_add_first_entry_uses_initial_balance_for_increment():
    ledger = _make_ledger(initial=100)
    posting = _make_posting(30, Direction.INC)

    entry = ledger.add(posting)

    assert entry.balance == Quantity(130)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert ledger.entries == [entry]
    assert ledger.entries[-1] is entry
    # Now the try-branch of _last_balance is exercised.
    assert ledger._last_balance == Quantity(130)


def test_add_first_entry_uses_initial_balance_for_decrement():
    ledger = _make_ledger(initial=100)
    posting = _make_posting(40, Direction.DEC)

    entry = ledger.add(posting)

    assert entry.balance == Quantity(60)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(60)


def test_add_second_entry_uses_last_entry_balance():
    ledger = _make_ledger(initial=100)
    first_posting = _make_posting(30, Direction.INC)
    second_posting = _make_posting(20, Direction.DEC)

    first = ledger.add(first_posting)
    second = ledger.add(second_posting)

    assert first.balance == Quantity(130)
    assert second.balance == Quantity(110)
    assert second.ledger is ledger
    assert second.posting is second_posting
    assert ledger.entries == [first, second]
    assert ledger.entries[-1] is second
    assert ledger._last_balance == Quantity(110)
