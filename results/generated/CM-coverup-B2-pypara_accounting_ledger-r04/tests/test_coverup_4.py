# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import Mock

from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_date_returns_posting_date():
    """
    Test that the ``date`` property of a ledger entry delegates to the date of
    its underlying posting (covers line 55 of ledger.py).
    """
    date = datetime.date(2021, 1, 15)

    journal = JournalEntry(date=date, description="Test journal entry", source=None)
    posting = Posting(
        journal=journal,
        date=date,
        account=Mock(),
        direction=None,
        amount=Decimal("100"),
    )
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Decimal("100"))

    # Postcondition: the ledger entry's date equals the posting's date.
    assert entry.date == date
    assert entry.date == posting.date
    assert isinstance(entry.date, datetime.date)
