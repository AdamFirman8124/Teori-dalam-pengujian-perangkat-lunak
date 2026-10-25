# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def _make_entry(is_debit, amount):
    posting = SimpleNamespace(amount=amount, is_debit=is_debit)
    return LedgerEntry(ledger=object(), posting=posting, balance=object())


def test_ledger_entry_debit_returns_amount_when_is_debit():
    amount = object()
    entry = _make_entry(is_debit=True, amount=amount)

    assert entry.is_debit is True
    assert entry.amount is amount
    assert entry.debit is amount


def test_ledger_entry_debit_returns_none_when_not_is_debit():
    amount = object()
    entry = _make_entry(is_debit=False, amount=amount)

    assert entry.is_debit is False
    assert entry.amount is amount
    assert entry.debit is None
