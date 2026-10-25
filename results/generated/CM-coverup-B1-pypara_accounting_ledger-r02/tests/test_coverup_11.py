# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_credit_returns_posting_amount_for_credit_entry():
    amount = Decimal("125.50")
    posting = SimpleNamespace(is_credit=True, amount=amount)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=Decimal("125.50"))

    assert entry.credit is amount


def test_credit_returns_none_for_non_credit_entry():
    amount = Decimal("125.50")
    posting = SimpleNamespace(is_credit=False, amount=amount)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=Decimal("0"))

    assert entry.credit is None
