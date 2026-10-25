# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    sentinel = object()
    mock_posting = MagicMock()
    mock_posting.amount = sentinel
    entry = LedgerEntry(ledger=MagicMock(), posting=mock_posting, balance=MagicMock())
    assert entry.amount is sentinel


def test_ledger_entry_amount_returns_posting_amount_value():
    from decimal import Decimal
    expected = Decimal("123.45")
    mock_posting = MagicMock()
    mock_posting.amount = expected
    entry = LedgerEntry(ledger=MagicMock(), posting=mock_posting, balance=MagicMock())
    assert entry.amount == expected
    assert entry.amount is expected
