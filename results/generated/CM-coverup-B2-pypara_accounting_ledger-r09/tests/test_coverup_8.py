# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

from types import SimpleNamespace
from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_is_debit_when_posting_is_debit():
    posting = SimpleNamespace(is_debit=True)
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_debit is True


def test_ledger_entry_is_debit_when_posting_is_credit():
    posting = SimpleNamespace(is_debit=False)
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_debit is False
