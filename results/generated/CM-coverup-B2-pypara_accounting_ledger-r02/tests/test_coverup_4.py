# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_date_returns_posting_date():
    expected = datetime.date(2023, 5, 17)
    posting = Mock()
    posting.date = expected
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.date == expected
    assert entry.date is expected
    # Repeated access is consistent and still delegates to the posting.
    assert entry.date == expected


def test_ledger_entry_date_reflects_different_posting_date():
    expected = datetime.date(2024, 2, 29)
    posting = Mock()
    posting.date = expected
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    result = entry.date

    assert result == expected
    assert isinstance(result, datetime.date)
