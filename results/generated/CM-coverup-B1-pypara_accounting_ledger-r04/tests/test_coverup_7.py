# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def _make_posting(journal, account, direction):
    return SimpleNamespace(
        journal=journal,
        date=datetime.date(2024, 1, 1),
        account=account,
        direction=direction,
        amount=Decimal("10"),
    )


def test_cntraccts_returns_accounts_of_opposite_direction():
    debit = object()
    credit = object()
    journal = SimpleNamespace(postings=[])
    debit_account = object()
    credit_account = object()
    other_credit_account = object()
    entry_posting = _make_posting(journal, debit_account, debit)
    counter1 = _make_posting(journal, credit_account, credit)
    counter2 = _make_posting(journal, other_credit_account, credit)
    same_direction = _make_posting(journal, object(), debit)
    postings = [entry_posting, counter1, counter2, same_direction]
    journal.postings = postings

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    result = entry.cntraccts

    assert result == [credit_account, other_credit_account]
    assert result is not journal.postings
    assert journal.postings == postings
    assert len(journal.postings) == 4


def test_cntraccts_empty_when_no_opposite_direction_postings():
    debit = object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, object(), debit)
    same_direction = _make_posting(journal, object(), debit)
    postings = [entry_posting, same_direction]
    journal.postings = postings

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    assert entry.cntraccts == []
    assert journal.postings == postings


def test_cntraccts_empty_when_journal_has_no_postings():
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, object(), object())

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    assert entry.cntraccts == []
    assert journal.postings == []
