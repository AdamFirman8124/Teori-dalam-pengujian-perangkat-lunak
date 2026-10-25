# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_credit_returns_posting_amount_for_credit_entry():
    amount = object()
    posting = SimpleNamespace(amount=amount, is_credit=True)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=object())

    assert entry.is_credit is True
    assert entry.credit is amount


def test_credit_returns_none_for_non_credit_entry():
    posting = SimpleNamespace(amount=object(), is_credit=False)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=object())

    assert entry.is_credit is False
    assert entry.credit is None
