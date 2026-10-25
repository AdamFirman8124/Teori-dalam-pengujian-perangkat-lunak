# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_amount_returns_posting_amount():
    expected_amount = Mock(name="amount")
    posting = Mock(name="posting")
    posting.amount = expected_amount
    entry = LedgerEntry(
        ledger=Mock(name="ledger"),
        posting=posting,
        balance=Mock(name="balance"),
    )

    assert entry.amount is expected_amount
