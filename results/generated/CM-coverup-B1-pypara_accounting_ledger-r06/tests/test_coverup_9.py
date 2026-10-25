# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

from unittest.mock import Mock

from pypara.accounting.ledger import LedgerEntry


def _make_ledger_entry(is_credit: bool) -> LedgerEntry:
    posting = Mock()
    posting.is_credit = is_credit

    return LedgerEntry(
        ledger=Mock(),
        posting=posting,
        balance=Mock(),
    )


def test_ledger_entry_is_credit_true():
    entry = _make_ledger_entry(True)

    assert entry.is_credit is True


def test_ledger_entry_is_credit_false():
    entry = _make_ledger_entry(False)

    assert entry.is_credit is False
