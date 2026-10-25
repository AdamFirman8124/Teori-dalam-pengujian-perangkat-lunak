# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from datetime import date as _date
from unittest.mock import Mock

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    """
    Test that the ``amount`` property of a ``LedgerEntry`` delegates to the
    amount of its underlying posting (covers line 69).
    """
    amount = Mock(name="amount")
    posting = Posting(
        journal=Mock(name="journal"),
        date=_date(2024, 1, 1),
        account=Mock(name="account"),
        direction=Mock(name="direction"),
        amount=amount,
    )
    entry = LedgerEntry(ledger=Mock(name="ledger"), posting=posting, balance=Mock(name="balance"))

    assert entry.amount is amount
