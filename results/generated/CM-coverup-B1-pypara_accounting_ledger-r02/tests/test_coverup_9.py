# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

from types import SimpleNamespace

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("posting_is_credit", [True, False])
def test_ledger_entry_is_credit_delegates_to_posting(posting_is_credit):
    posting = SimpleNamespace(is_credit=posting_is_credit)
    entry = LedgerEntry(ledger=None, posting=posting, balance=None)

    assert entry.is_credit is posting_is_credit
