# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

import datetime
from unittest.mock import MagicMock

import pytest

from pypara.accounting.ledger import LedgerEntry


def _make_entry(is_credit: bool) -> LedgerEntry:
    """Build a LedgerEntry whose posting reports the given credit flag."""
    posting = MagicMock()
    posting.is_credit = is_credit
    posting.is_debit = not is_credit
    posting.date = datetime.date(2024, 1, 1)
    posting.amount = MagicMock()
    posting.account = MagicMock()

    ledger = MagicMock()
    ledger.account = posting.account

    return LedgerEntry(ledger=ledger, posting=posting, balance=MagicMock())


def test_is_credit_returns_true_for_credit_posting():
    entry = _make_entry(True)

    assert entry.is_credit is True
    assert entry.posting.is_credit is True


def test_is_credit_returns_false_for_debit_posting():
    entry = _make_entry(False)

    assert entry.is_credit is False
    assert entry.posting.is_credit is False


def test_is_credit_delegates_to_posting_on_each_access():
    posting = MagicMock()
    posting.is_credit = True
    entry = LedgerEntry(ledger=MagicMock(), posting=posting, balance=MagicMock())

    assert entry.is_credit is True
    assert entry.is_credit is True
    assert posting.is_credit is True

    posting.is_credit = False
    assert entry.is_credit is False


def test_is_credit_is_consistent_with_is_debit():
    credit_entry = _make_entry(True)
    debit_entry = _make_entry(False)

    assert credit_entry.is_credit is not credit_entry.posting.is_debit
    assert debit_entry.is_credit is not debit_entry.posting.is_debit
