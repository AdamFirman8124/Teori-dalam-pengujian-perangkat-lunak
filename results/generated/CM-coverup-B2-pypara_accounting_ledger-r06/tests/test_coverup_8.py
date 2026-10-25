# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("expected", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(expected):
    class PostingStub:
        is_debit = expected

    entry = LedgerEntry(
        ledger=object(),
        posting=PostingStub(),
        balance=object(),
    )

    assert entry.is_debit is expected
