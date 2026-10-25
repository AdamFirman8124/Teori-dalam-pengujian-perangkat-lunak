# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def _make_entry(*, is_debit: bool) -> LedgerEntry:
    posting = Mock()
    posting.is_debit = is_debit
    posting.is_credit = not is_debit
    posting.amount = Mock(name="amount")
    return LedgerEntry(
        ledger=Mock(name="ledger"),
        posting=posting,
        balance=Mock(name="balance"),
    )


def test_debit_returns_amount_when_entry_is_debit():
    entry = _make_entry(is_debit=True)

    assert entry.is_debit is True
    assert entry.debit is entry.posting.amount


def test_debit_returns_none_when_entry_is_credit():
    entry = _make_entry(is_debit=False)

    assert entry.is_debit is False
    assert entry.debit is None
