# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from unittest.mock import Mock
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    mock_amount = Mock(name="amount")
    mock_posting = Mock(name="posting")
    mock_posting.amount = mock_amount
    mock_ledger = Mock(name="ledger")
    mock_balance = Mock(name="balance")
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    result = entry.amount
    assert result is mock_amount
    assert result == mock_posting.amount


def test_ledger_entry_amount_delegates_to_posting():
    sentinel_amount = object()
    mock_posting = Mock()
    mock_posting.amount = sentinel_amount
    entry = LedgerEntry(ledger=Mock(), posting=mock_posting, balance=Mock())
    assert entry.amount is sentinel_amount
