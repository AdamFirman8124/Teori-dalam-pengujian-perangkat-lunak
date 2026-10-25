# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

import pytest

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def _posting(direction, amount, date=datetime.date(2024, 1, 2)):
    return Posting(
        journal=None,
        date=date,
        account=None,
        direction=direction,
        amount=Amount(Decimal(amount)),
    )


@pytest.fixture
def ledger():
    ledger = Ledger(
        account=None,
        initial=Balance(
            date=datetime.date(2024, 1, 1),
            value=Quantity(Decimal("100")),
        ),
    )
    yield ledger
    ledger.entries.clear()


def test_last_balance_returns_initial_value_when_no_entries(ledger):
    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("100"))


def test_add_creates_entry_and_appends_it(ledger):
    posting = _posting(Direction.INC, "50")

    entry = ledger.add(posting)

    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("150"))
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(Decimal("150"))


def test_add_uses_last_entry_balance_for_subsequent_entries(ledger):
    first = ledger.add(_posting(Direction.INC, "50"))
    second = ledger.add(_posting(Direction.DEC, "30"))

    assert first.balance == Quantity(Decimal("150"))
    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]
    assert ledger._last_balance == Quantity(Decimal("120"))
