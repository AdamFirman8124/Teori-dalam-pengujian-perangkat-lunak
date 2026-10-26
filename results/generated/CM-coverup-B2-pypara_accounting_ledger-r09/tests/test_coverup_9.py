# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

import datetime
from decimal import Decimal

import pytest

from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


class _FakePosting:
    """Minimal stand-in for Posting exposing the is_credit property."""

    def __init__(self, is_credit: bool) -> None:
        self._is_credit = is_credit
        self.is_credit_reads = 0

    @property
    def is_credit(self) -> bool:
        self.is_credit_reads += 1
        return self._is_credit


def _make_entry(is_credit: bool) -> tuple[LedgerEntry, _FakePosting]:
    posting = _FakePosting(is_credit)
    entry = LedgerEntry(
        ledger=None,
        posting=posting,
        balance=Quantity(Decimal("0")),
    )
    return entry, posting


@pytest.mark.parametrize("credit", [True, False])
def test_ledger_entry_is_credit_delegates_to_posting(credit: bool) -> None:
    entry, posting = _make_entry(credit)

    result = entry.is_credit

    assert result is credit
    assert isinstance(result, bool)
    assert posting.is_credit_reads == 1


def test_ledger_entry_is_credit_is_a_property() -> None:
    assert isinstance(LedgerEntry.is_credit, property)


def test_ledger_entry_is_credit_reflects_posting_changes() -> None:
    entry, posting = _make_entry(True)
    assert entry.is_credit is True

    posting._is_credit = False
    assert entry.is_credit is False
    assert posting.is_credit_reads == 2
