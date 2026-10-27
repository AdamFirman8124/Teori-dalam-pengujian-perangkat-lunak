# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_debit_returns_amount_for_debit_posting():
    amount = object()
    posting = SimpleNamespace(is_debit=True, amount=amount)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=object())

    assert entry.debit is amount


def test_ledger_entry_debit_returns_none_for_credit_posting():
    amount = object()
    posting = SimpleNamespace(is_debit=False, amount=amount)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=object())

    assert entry.debit is None
