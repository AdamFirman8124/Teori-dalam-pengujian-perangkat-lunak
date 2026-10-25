# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def test_ledger_entry_amount_returns_posting_amount() -> None:
    amount = Amount(Decimal("123.45"))
    posting = SimpleNamespace(amount=amount)
    entry = LedgerEntry(
        ledger=None,
        posting=posting,
        balance=Quantity(Decimal("0")),
    )

    assert entry.amount is amount
