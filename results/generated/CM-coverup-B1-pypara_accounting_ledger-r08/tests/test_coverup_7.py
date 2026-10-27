# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_cntraccts_returns_only_opposite_direction_accounts():
    ledger_mock = MagicMock()
    balance_mock = MagicMock()
    contra_account_1 = MagicMock()
    contra_account_2 = MagicMock()
    same_account = MagicMock()

    main_posting = MagicMock()
    main_posting.direction = "DEBIT"
    main_posting.account = same_account

    same_direction_posting = MagicMock()
    same_direction_posting.direction = "DEBIT"
    same_direction_posting.account = same_account

    contra_posting_1 = MagicMock()
    contra_posting_1.direction = "CREDIT"
    contra_posting_1.account = contra_account_1

    contra_posting_2 = MagicMock()
    contra_posting_2.direction = "CREDIT"
    contra_posting_2.account = contra_account_2

    journal_mock = MagicMock()
    journal_mock.postings = [main_posting, same_direction_posting, contra_posting_1, contra_posting_2]
    main_posting.journal = journal_mock

    entry = LedgerEntry(ledger=ledger_mock, posting=main_posting, balance=balance_mock)

    result = entry.cntraccts

    assert result == [contra_account_1, contra_account_2]


def test_cntraccts_empty_when_no_opposite_direction():
    ledger_mock = MagicMock()
    balance_mock = MagicMock()

    main_posting = MagicMock()
    main_posting.direction = "CREDIT"
    main_posting.account = MagicMock()

    other_same = MagicMock()
    other_same.direction = "CREDIT"
    other_same.account = MagicMock()

    journal_mock = MagicMock()
    journal_mock.postings = [main_posting, other_same]
    main_posting.journal = journal_mock

    entry = LedgerEntry(ledger=ledger_mock, posting=main_posting, balance=balance_mock)

    result = entry.cntraccts

    assert result == []


def test_cntraccts_empty_journal_postings():
    ledger_mock = MagicMock()
    balance_mock = MagicMock()

    main_posting = MagicMock()
    main_posting.direction = "DEBIT"

    journal_mock = MagicMock()
    journal_mock.postings = []
    main_posting.journal = journal_mock

    entry = LedgerEntry(ledger=ledger_mock, posting=main_posting, balance=balance_mock)

    result = entry.cntraccts

    assert result == []
