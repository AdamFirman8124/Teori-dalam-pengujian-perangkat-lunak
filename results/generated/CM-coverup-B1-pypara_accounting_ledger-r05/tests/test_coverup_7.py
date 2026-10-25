# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("posting_is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(posting_is_debit):
    class PostingStub:
        is_debit = posting_is_debit

    entry = LedgerEntry(ledger=None, posting=PostingStub(), balance=None)

    assert entry.is_debit is posting_is_debit
