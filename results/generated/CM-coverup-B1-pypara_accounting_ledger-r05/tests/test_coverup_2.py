# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

from datetime import date
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger


def test_last_balance_returns_initial_value_when_ledger_has_no_entries():
    initial_value = Decimal("100.00")
    ledger = Ledger(
        account=object(),
        initial=Balance(date(2024, 1, 1), initial_value),
    )

    assert ledger.entries == []
    assert ledger._last_balance == initial_value


def test_add_creates_and_stores_entry_using_last_balance():
    initial_value = Decimal("100.00")
    posting_amount = Decimal("25.00")
    ledger = Ledger(
        account=object(),
        initial=Balance(date(2024, 1, 1), initial_value),
    )
    posting = Posting(
        journal=object(),
        date=date(2024, 1, 2),
        account=object(),
        direction=Direction.INC,
        amount=posting_amount,
    )

    entry = ledger.add(posting)

    assert entry in ledger.entries
    assert ledger.entries == [entry]
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == initial_value + posting_amount
    assert ledger._last_balance == entry.balance
