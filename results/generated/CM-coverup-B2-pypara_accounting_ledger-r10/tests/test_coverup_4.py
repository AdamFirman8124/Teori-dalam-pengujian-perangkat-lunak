# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import Mock

import pytest

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


def _make_entry(date: datetime.date):
    """Build a LedgerEntry whose posting carries the given date."""
    posting = Mock(spec=Posting)
    posting.date = date
    ledger = Mock()
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=Quantity(Decimal("0")))
    return entry, posting


def test_ledger_entry_date_returns_posting_date():
    """LedgerEntry.date must delegate to the underlying posting's date."""
    expected = datetime.date(2024, 3, 15)
    entry, posting = _make_entry(expected)

    assert entry.date == expected
    assert isinstance(entry.date, datetime.date)
    assert entry.date is posting.date


def test_ledger_entry_date_tracks_posting_date_changes():
    """LedgerEntry.date must not cache a stale value."""
    entry, posting = _make_entry(datetime.date(2020, 1, 1))
    assert entry.date == datetime.date(2020, 1, 1)

    posting.date = datetime.date(2021, 12, 31)

    assert entry.date == datetime.date(2021, 12, 31)


def test_ledger_entry_date_is_read_only():
    """LedgerEntry.date is a property without a setter."""
    entry, _ = _make_entry(datetime.date(2022, 6, 1))

    with pytest.raises(AttributeError):
        entry.date = datetime.date(2023, 6, 1)

    assert entry.date == datetime.date(2022, 6, 1)


def test_ledger_entry_date_with_real_posting():
    """LedgerEntry.date works with a genuine Posting instance."""
    expected = datetime.date(2019, 9, 9)
    posting = Posting(
        journal=Mock(),
        date=expected,
        account=Mock(),
        direction=Mock(),
        amount=Mock(),
    )
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Quantity(Decimal("0")))

    assert entry.date == expected
    assert entry.date is posting.date
    assert entry.posting is posting
