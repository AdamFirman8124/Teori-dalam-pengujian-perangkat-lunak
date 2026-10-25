# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.generic import Balance
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def test_last_balance_returns_initial_value_for_empty_ledger():
    initial = Balance(date(2024, 1, 1), Quantity(Decimal("100.00")))
    ledger = Ledger(account=object(), initial=initial)

    assert ledger.entries == []
    assert ledger._last_balance == Quantity(Decimal("100.00"))


def test_add_appends_entries_and_uses_previous_entry_balance():
    initial = Balance(date(2024, 1, 1), Quantity(Decimal("100.00")))
    ledger = Ledger(account=object(), initial=initial)
    debit = SimpleNamespace(
        amount=Amount(Decimal("25.00")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("10.00")),
        direction=SimpleNamespace(value=-1),
    )

    first_entry = ledger.add(debit)
    second_entry = ledger.add(credit)

    assert isinstance(first_entry, LedgerEntry)
    assert first_entry.ledger is ledger
    assert first_entry.posting is debit
    assert first_entry.balance == Quantity(Decimal("125.00"))

    assert isinstance(second_entry, LedgerEntry)
    assert second_entry.ledger is ledger
    assert second_entry.posting is credit
    assert second_entry.balance == Quantity(Decimal("115.00"))

    assert ledger.entries == [first_entry, second_entry]
    assert ledger._last_balance == Quantity(Decimal("115.00"))
