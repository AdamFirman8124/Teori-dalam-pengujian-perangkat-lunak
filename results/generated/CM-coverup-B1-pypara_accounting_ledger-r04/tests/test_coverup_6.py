# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from decimal import Decimal
from unittest.mock import MagicMock
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    amount = Decimal("123.45")
    posting = MagicMock()
    posting.amount = amount
    ledger = MagicMock()
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=Decimal("123.45"))
    try:
        result = entry.amount
        assert result == amount
        assert result is posting.amount
    finally:
        del entry
        del posting
        del ledger


def test_ledger_entry_amount_zero():
    amount = Decimal("0")
    posting = MagicMock()
    posting.amount = amount
    ledger = MagicMock()
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=Decimal("0"))
    try:
        assert entry.amount == Decimal("0")
        assert entry.amount is posting.amount
    finally:
        del entry
        del posting
        del ledger
