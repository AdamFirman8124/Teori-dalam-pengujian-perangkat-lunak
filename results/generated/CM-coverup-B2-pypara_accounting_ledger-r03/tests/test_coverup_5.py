# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_ledgerentry_description_returns_journal_description():
    expected_description = "Test journal description"
    journal_mock = MagicMock()
    journal_mock.description = expected_description
    posting_mock = MagicMock()
    posting_mock.journal = journal_mock
    ledger_mock = MagicMock()
    balance_mock = MagicMock()
    entry = LedgerEntry(ledger=ledger_mock, posting=posting_mock, balance=balance_mock)
    actual = entry.description
    assert actual == expected_description
    assert actual == entry.posting.journal.description
