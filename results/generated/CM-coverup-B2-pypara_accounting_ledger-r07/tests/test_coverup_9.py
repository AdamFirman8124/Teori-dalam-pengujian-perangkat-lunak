# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

from decimal import Decimal
from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_is_credit_true():
    mock_ledger = MagicMock()
    mock_posting = MagicMock()
    mock_posting.is_credit = True
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=Decimal("100"))
    assert entry.is_credit is True
    assert entry.posting is mock_posting
    assert entry.ledger is mock_ledger


def test_ledger_entry_is_credit_false():
    mock_ledger = MagicMock()
    mock_posting = MagicMock()
    mock_posting.is_credit = False
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=Decimal("100"))
    assert entry.is_credit is False
    assert entry.posting is mock_posting
    assert entry.ledger is mock_ledger
