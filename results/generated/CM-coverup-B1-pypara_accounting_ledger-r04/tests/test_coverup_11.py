# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from types import SimpleNamespace
from unittest.mock import sentinel

from pypara.accounting.ledger import LedgerEntry


def test_credit_returns_posting_amount_when_entry_is_credit():
    posting = SimpleNamespace(amount=sentinel.amount, is_credit=True)
    entry = LedgerEntry(
        ledger=sentinel.ledger,
        posting=posting,
        balance=sentinel.balance,
    )

    assert entry.credit is sentinel.amount


def test_credit_returns_none_when_entry_is_not_credit():
    posting = SimpleNamespace(amount=sentinel.amount, is_credit=False)
    entry = LedgerEntry(
        ledger=sentinel.ledger,
        posting=posting,
        balance=sentinel.balance,
    )

    assert entry.credit is None
