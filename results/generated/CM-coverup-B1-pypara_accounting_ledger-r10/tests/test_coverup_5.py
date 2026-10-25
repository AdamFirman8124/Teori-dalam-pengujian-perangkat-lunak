# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

import datetime
from unittest.mock import MagicMock

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_description_delegates_to_journal():
    """
    Test that the description of a ledger entry is delegated to the
    description of the underlying journal entry (covers line 62).
    """
    # Arrange: build a minimal object graph with mocks so that no
    # Direction/Account/Quantity construction details are required.
    journal = MagicMock()
    journal.description = "Test journal entry"

    posting = MagicMock(spec=Posting)
    posting.journal = journal
    posting.date = datetime.date(2024, 1, 1)

    ledger = MagicMock()
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=100)

    # Act
    result = entry.description

    # Assert: postcondition is that the ledger entry's description is
    # exactly the description of its posting's journal entry.
    assert result == "Test journal entry"
    assert result == entry.posting.journal.description
    assert isinstance(result, str)
