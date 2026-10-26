# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from datetime import date
from decimal import Decimal
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.commons.numbers import Amount, Quantity

class _StubAccount:
    """Minimal stand-in satisfying the Account protocol."""
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None

def test_ledger_entry_amount_delegates_to_posting_amount():
    """
    Covers LedgerEntry.amount (line 69): it must return the amount of
    the underlying posting.
    """
    account = _StubAccount("100", "Cash")
    journal = JournalEntry(date(2024, 1, 1), "Test entry", object())
    posting = Posting(
        journal=journal,
        date=date(2024, 1, 1),
        account=account,
        direction=Direction.INC,
        amount=Amount(Decimal("100.00")),
    )
    ledger = Ledger(account=account, initial=Quantity(Decimal("0")))
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=Quantity(Decimal("100.00")))
    assert entry.amount == posting.amount
    assert entry.amount == Amount(Decimal("100.00"))
