# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(is_debit):
    class PostingStub:
        def __init__(self, value):
            self.is_debit = value

    posting = PostingStub(is_debit)
    entry = LedgerEntry(ledger=None, posting=posting, balance=None)

    assert entry.is_debit is is_debit
