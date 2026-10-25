# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from types import SimpleNamespace
from unittest.mock import sentinel

from pypara.accounting.ledger import LedgerEntry


def test_credit_returns_posting_amount_for_credit_entry():
    posting = SimpleNamespace(is_credit=True, amount=sentinel.amount)
    entry = LedgerEntry(
        ledger=sentinel.ledger,
        posting=posting,
        balance=sentinel.balance,
    )

    assert entry.credit is sentinel.amount


def test_credit_returns_none_for_non_credit_entry():
    posting = SimpleNamespace(is_credit=False, amount=sentinel.amount)
    entry = LedgerEntry(
        ledger=sentinel.ledger,
        posting=posting,
        balance=sentinel.balance,
    )

    assert entry.credit is None
