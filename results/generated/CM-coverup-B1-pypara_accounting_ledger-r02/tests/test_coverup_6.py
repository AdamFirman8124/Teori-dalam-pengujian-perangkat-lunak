# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount


def test_ledger_entry_amount_returns_posting_amount():
    expected_amount = Amount(Decimal("42.50"))
    posting = SimpleNamespace(amount=expected_amount)
    entry = LedgerEntry(
        ledger=SimpleNamespace(),
        posting=posting,
        balance=None,
    )

    assert entry.amount == expected_amount
