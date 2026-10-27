# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_description_returns_journal_description():
    mock_journal = MagicMock()
    mock_journal.description = "Test journal description"
    mock_posting = MagicMock()
    mock_posting.journal = mock_journal
    mock_ledger = MagicMock()
    mock_balance = MagicMock()
    entry = LedgerEntry(ledger=mock_ledger, posting=mock_posting, balance=mock_balance)
    assert entry.description == "Test journal description"
    assert entry.description == mock_posting.journal.description


def test_ledger_entry_description_empty_string():
    mock_journal = MagicMock()
    mock_journal.description = ""
    mock_posting = MagicMock()
    mock_posting.journal = mock_journal
    entry = LedgerEntry(ledger=MagicMock(), posting=mock_posting, balance=MagicMock())
    assert entry.description == ""
