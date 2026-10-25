# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from unittest.mock import Mock

import pytest

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry


def _make_posting(date):
    """Build a Posting with stub collaborators (Posting does not validate types)."""
    return Posting(
        journal=Mock(name="journal"),
        date=date,
        account=Mock(name="account"),
        direction=Mock(name="direction"),
        amount=Mock(name="amount"),
    )


def _make_entry(posting, balance=None):
    return LedgerEntry(
        ledger=Mock(name="ledger"),
        posting=posting,
        balance=balance if balance is not None else Mock(name="balance"),
    )


def test_ledger_entry_date_returns_posting_date():
    date = datetime.date(2024, 1, 31)
    posting = _make_posting(date)
    entry = _make_entry(posting)

    assert entry.date == date
    assert entry.date is posting.date
    assert isinstance(entry.date, datetime.date)


def test_ledger_entry_date_is_derived_from_posting_not_hardcoded():
    first = _make_entry(_make_posting(datetime.date(1999, 12, 31)))
    second = _make_entry(_make_posting(datetime.date(2025, 6, 1)))

    assert first.date == datetime.date(1999, 12, 31)
    assert second.date == datetime.date(2025, 6, 1)
    assert first.date != second.date


def test_ledger_entry_date_is_a_read_only_property():
    assert isinstance(LedgerEntry.date, property)

    entry = _make_entry(_make_posting(datetime.date(2024, 3, 15)))
    with pytest.raises(AttributeError):
        entry.date = datetime.date(2024, 3, 16)


def test_ledger_entry_date_access_does_not_mutate_state():
    date = datetime.date(2024, 2, 29)
    posting = _make_posting(date)
    balance = Mock(name="balance")
    entry = _make_entry(posting, balance=balance)

    before_posting_date = posting.date
    before_balance = entry.balance

    assert entry.date == date

    # Postconditions: nothing was mutated by reading the property.
    assert posting.date is before_posting_date
    assert entry.balance is before_balance
    assert entry.posting is posting
    assert entry.date == posting.date
