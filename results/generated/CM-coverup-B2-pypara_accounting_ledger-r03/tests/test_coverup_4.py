# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from unittest import mock

import pytest

from pypara.accounting.ledger import LedgerEntry
from pypara.accounting.journaling import Posting, Direction
from pypara.commons.numbers import Quantity


def test_ledger_entry_date_returns_posting_date():
    """
    Test that `LedgerEntry.date` returns the date of the underlying posting,
    thereby executing line 55 (`return self.posting.date`).
    """
    # Arrange: build a mock posting with a known date.
    posting = mock.Mock(spec=Posting)
    expected_date = datetime.date(2023, 5, 17)
    posting.date = expected_date

    # Build a mock ledger (not used by the `date` property, but required by the dataclass).
    ledger = mock.Mock()

    # Build the ledger entry.
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=Quantity(100))

    # Act: access the `date` property (this executes line 55).
    actual_date = entry.date

    # Assert: the returned date is the posting's date.
    assert actual_date == expected_date
    assert actual_date is expected_date
