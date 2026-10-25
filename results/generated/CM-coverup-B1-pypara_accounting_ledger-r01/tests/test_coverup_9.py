# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_is_credit_when_posting_is_credit():
    posting = Mock()
    posting.is_credit = True
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_credit is True


def test_ledger_entry_is_not_credit_when_posting_is_not_credit():
    posting = Mock()
    posting.is_credit = False
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_credit is False
