# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("expected", [True, False])
def test_ledger_entry_is_credit_delegates_to_posting(expected):
    class PostingStub:
        is_credit = expected

    entry = LedgerEntry(
        ledger=None,
        posting=PostingStub(),
        balance=None,
    )

    assert entry.is_credit is expected
