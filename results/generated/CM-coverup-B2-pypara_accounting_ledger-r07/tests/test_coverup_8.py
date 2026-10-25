# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


class _StubPosting:
    """Minimal posting stand-in exposing the ``is_debit`` property."""

    def __init__(self, is_debit: bool) -> None:
        self._is_debit = is_debit

    @property
    def is_debit(self) -> bool:
        return self._is_debit


@pytest.mark.parametrize("posting_is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(posting_is_debit):
    posting = _StubPosting(posting_is_debit)
    entry = LedgerEntry(ledger=None, posting=posting, balance=None)

    result = entry.is_debit

    assert result is posting_is_debit
    assert isinstance(result, bool)
