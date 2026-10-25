# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from decimal import Decimal
from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount


def _make_entry(amount: Amount, is_credit: bool) -> LedgerEntry:
    posting = Mock()
    posting.amount = amount
    posting.is_credit = is_credit
    posting.is_debit = not is_credit
    return LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())


def test_credit_returns_amount_when_entry_is_credit():
    amount = Amount(Decimal("12.34"))
    entry = _make_entry(amount, is_credit=True)

    assert entry.is_credit is True
    assert entry.credit is amount
    assert entry.credit == amount
    assert entry.debit is None


def test_credit_returns_none_when_entry_is_debit():
    amount = Amount(Decimal("5.00"))
    entry = _make_entry(amount, is_credit=False)

    assert entry.is_credit is False
    assert entry.credit is None
    assert entry.debit is amount


def test_credit_returns_zero_amount_for_zero_valued_credit_entry():
    amount = Amount(Decimal("0"))
    entry = _make_entry(amount, is_credit=True)

    assert entry.credit is amount
    assert entry.credit == Amount(Decimal("0"))
    assert entry.credit is not None
