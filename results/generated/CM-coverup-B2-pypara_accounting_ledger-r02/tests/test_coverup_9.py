# file: project/pypara/accounting/ledger.py:85-90
# asked: {"lines": [90], "branches": []}
# gained: {"lines": [90], "branches": []}

from unittest.mock import Mock

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


def _make_ledger_entry(is_credit: bool) -> LedgerEntry:
    """
    Builds a ledger entry backed by a mock posting with the given credit flag.
    """
    posting = Mock(spec=Posting)
    posting.is_credit = is_credit
    posting.is_debit = not is_credit
    return LedgerEntry(ledger=Mock(), posting=posting, balance=Quantity("100"))


def test_ledger_entry_is_credit_true():
    """
    A ledger entry backed by a credit posting reports ``is_credit`` as True.
    """
    entry = _make_ledger_entry(is_credit=True)

    assert entry.is_credit is True


def test_ledger_entry_is_credit_false():
    """
    A ledger entry backed by a debit posting reports ``is_credit`` as False.
    """
    entry = _make_ledger_entry(is_credit=False)

    assert entry.is_credit is False
