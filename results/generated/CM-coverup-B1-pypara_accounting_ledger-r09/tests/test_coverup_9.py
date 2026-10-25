# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

import pytest
from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("is_credit", [True, False])
def test_ledger_entry_is_credit_delegates_to_posting(is_credit):
    posting = Mock()
    posting.is_credit = is_credit
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_credit is is_credit


def test_ledger_entry_is_credit_reflects_posting_changes():
    posting = Mock()
    posting.is_credit = True
    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())

    assert entry.is_credit is True

    posting.is_credit = False

    assert entry.is_credit is False
