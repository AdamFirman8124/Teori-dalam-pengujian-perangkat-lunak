# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    expected_amount = Decimal("12.34")
    posting = SimpleNamespace(amount=expected_amount)
    entry = LedgerEntry(
        ledger=object(),
        posting=posting,
        balance=Decimal("0"),
    )

    assert entry.amount is expected_amount
