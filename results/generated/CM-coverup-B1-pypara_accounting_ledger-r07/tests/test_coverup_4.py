# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

from datetime import date
from decimal import Decimal
from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


def test_ledger_entry_date_returns_posting_date():
    """
    ``LedgerEntry.date`` must delegate to the date of the underlying posting
    (covers line 55: ``return self.posting.date``).
    """
    # Arrange: build a ledger entry with a mock posting carrying a known date.
    entry_date = date(2024, 5, 17)
    posting = Mock(spec=["date"])
    posting.date = entry_date
    ledger = Mock(spec=["account"])
    balance = Quantity(Decimal("100"))

    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)

    # Act
    result = entry.date

    # Assert: the property returns exactly the posting's date.
    assert result == entry_date
    assert result is posting.date
