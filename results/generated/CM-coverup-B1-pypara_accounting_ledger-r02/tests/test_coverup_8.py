# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("posting_is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(posting_is_debit: bool):
    class _FakeLedger:
        pass

    class _FakePosting:
        def __init__(self, is_debit: bool):
            self._is_debit = is_debit

        @property
        def is_debit(self) -> bool:
            return self._is_debit

        @property
        def is_credit(self) -> bool:
            return not self._is_debit

    ledger = _FakeLedger()
    posting = _FakePosting(is_debit=posting_is_debit)
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=0)

    assert entry.is_debit is posting_is_debit
    assert entry.is_credit is (not posting_is_debit)
