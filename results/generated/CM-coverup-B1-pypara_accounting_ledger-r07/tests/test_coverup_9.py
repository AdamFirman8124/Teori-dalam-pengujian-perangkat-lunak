# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import Mock

import pytest

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


def _make_entry(is_credit: bool) -> LedgerEntry:
    """Build a LedgerEntry whose posting reports the given credit flag."""
    posting = Mock()
    posting.is_credit = is_credit
    return LedgerEntry(
        ledger=Mock(),
        posting=posting,
        balance=Quantity(Decimal("0")),
    )


@pytest.mark.parametrize("flag", [True, False])
def test_is_credit_delegates_to_posting(flag):
    entry = _make_entry(flag)

    assert entry.is_credit is flag
    assert entry.posting.is_credit is flag


def test_is_credit_is_not_cached():
    entry = _make_entry(True)
    assert entry.is_credit is True

    entry.posting.is_credit = False
    assert entry.is_credit is False


def test_is_credit_with_real_posting_like_object():
    class _StubPosting:
        def __init__(self, is_credit: bool) -> None:
            self.is_credit = is_credit

    entry = LedgerEntry(
        ledger=Mock(),
        posting=_StubPosting(True),
        balance=Quantity(Decimal("10")),
    )

    assert entry.is_credit is True
    assert entry.balance == Decimal("10")
