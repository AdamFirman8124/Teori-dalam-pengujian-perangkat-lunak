# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_credit_returns_amount_for_credit_posting():
    amount = Decimal("12.34")
    posting = SimpleNamespace(amount=amount, is_credit=True)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=Decimal("12.34"))

    assert entry.credit == amount
    assert entry.credit is amount


def test_ledger_entry_credit_returns_none_for_non_credit_posting():
    posting = SimpleNamespace(amount=Decimal("12.34"), is_credit=False)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=Decimal("0"))

    assert entry.credit is None
