# file: project/pypara/accounting/ledger.py:99-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

from decimal import Decimal
from datetime import date, timedelta
from unittest.mock import MagicMock

import pytest

from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Quantity


def _make_entry(is_credit: bool) -> LedgerEntry:
    """
    Creates a ledger entry backed by mock ledger and posting objects.

    :param is_credit: whether the underlying posting is a credit posting
    :return: a ledger entry
    """
    ledger = MagicMock(spec=Ledger)
    posting = MagicMock()
    posting.date = date(2021, 1, 1)
    posting.description = "Test posting"
    posting.amount = Decimal("100")
    posting.is_credit = is_credit
    posting.is_debit = not is_credit
    return LedgerEntry(ledger=ledger, posting=posting, balance=Quantity(Decimal("10")))


def test_credit_returns_amount_for_credit_posting() -> None:
    """
    Tests that the ``credit`` property returns the amount when the entry is a credit.
    """
    entry = _make_entry(is_credit=True)

    assert entry.is_credit is True
    assert entry.credit == Decimal("100")


def test_credit_returns_none_for_debit_posting() -> None:
    """
    Tests that the ``credit`` property returns ``None`` when the entry is a debit.
    """
    entry = _make_entry(is_credit=False)

    assert entry.is_credit is False
    assert entry.credit is None
