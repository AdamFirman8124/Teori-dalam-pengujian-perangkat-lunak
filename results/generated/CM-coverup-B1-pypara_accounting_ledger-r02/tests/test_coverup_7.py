# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import LedgerEntry


class _FakeJournal:
    def __init__(self, postings=None):
        self.postings = [] if postings is None else postings


def _make_posting(journal, account, direction):
    return Posting(
        journal=journal,
        date=datetime.date(2024, 1, 1),
        account=account,
        direction=direction,
        amount=Decimal("10"),
    )


def test_cntraccts_returns_accounts_of_opposite_direction():
    journal = _FakeJournal()
    inc_account = object()
    dec_account = object()
    other_dec_account = object()
    entry_posting = _make_posting(journal, inc_account, Direction.INC)
    counter1 = _make_posting(journal, dec_account, Direction.DEC)
    counter2 = _make_posting(journal, other_dec_account, Direction.DEC)
    same_direction = _make_posting(journal, object(), Direction.INC)
    postings = [entry_posting, counter1, counter2, same_direction]
    journal.postings = postings

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    result = entry.cntraccts

    assert result == [dec_account, other_dec_account]
    assert result is not journal.postings
    assert journal.postings == postings
    assert len(journal.postings) == 4


def test_cntraccts_empty_when_no_opposite_direction_postings():
    journal = _FakeJournal()
    entry_posting = _make_posting(journal, object(), Direction.INC)
    same_direction = _make_posting(journal, object(), Direction.INC)
    postings = [entry_posting, same_direction]
    journal.postings = postings

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    assert entry.cntraccts == []
    assert journal.postings == postings


def test_cntraccts_empty_when_journal_has_no_postings():
    journal = _FakeJournal()
    entry_posting = _make_posting(journal, object(), Direction.DEC)

    entry = LedgerEntry(ledger=None, posting=entry_posting, balance=Decimal("0"))

    assert entry.cntraccts == []
    assert journal.postings == []
