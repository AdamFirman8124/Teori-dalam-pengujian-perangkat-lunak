# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

from typing import Any

import pytest

from pypara.accounting.ledger import LedgerEntry


class _FakeLedger:
    """Minimal stand-in for a Ledger instance; not used by is_debit."""


class _FakePosting:
    """Minimal stand-in for a Posting with controllable direction flags."""

    def __init__(self, is_debit: bool):
        self._is_debit = is_debit

    @property
    def is_debit(self) -> bool:
        return self._is_debit

    @property
    def is_credit(self) -> bool:
        return not self._is_debit


@pytest.mark.parametrize("posting_is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(posting_is_debit: bool):
    """
    Line 83 (``return self.posting.is_debit``) must execute and delegate
    to the underlying posting's ``is_debit`` property, for both debit
    and credit postings.
    """
    ledger = _FakeLedger()
    posting = _FakePosting(is_debit=posting_is_debit)
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=0)

    # Postcondition: the entry's is_debit reflects the posting's direction.
    assert entry.is_debit is posting_is_debit
    # Postcondition: the inverse (is_credit) is also consistent.
    assert entry.is_credit is (not posting_is_debit)
