# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("expected", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(expected):
    class PostingStub:
        accesses = 0

        @property
        def is_debit(self):
            self.accesses += 1
            return expected

    posting = PostingStub()
    entry = LedgerEntry(ledger=object(), posting=posting, balance=object())

    assert entry.is_debit is expected
    assert posting.accesses == 1
