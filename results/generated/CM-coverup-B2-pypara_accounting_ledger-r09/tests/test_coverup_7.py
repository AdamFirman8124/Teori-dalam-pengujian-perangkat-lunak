# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from types import SimpleNamespace

import pytest

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry

DEBIT = object()
CREDIT = object()


def _make_posting(journal, account, direction):
    return Posting(
        journal=journal,
        date=datetime.date(2024, 1, 1),
        account=account,
        direction=direction,
        amount=None,
    )


def _make_entry(posting):
    return LedgerEntry(ledger=None, posting=posting, balance=None)


def test_cntraccts_returns_only_opposite_direction_accounts(monkeypatch):
    acct_a, acct_b, acct_c = object(), object(), object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, acct_a, DEBIT)
    counter_posting = _make_posting(journal, acct_b, CREDIT)
    same_direction_posting = _make_posting(journal, acct_c, DEBIT)
    monkeypatch.setattr(
        journal,
        "postings",
        [entry_posting, counter_posting, same_direction_posting],
    )

    entry = _make_entry(entry_posting)

    result = entry.cntraccts

    assert result == [acct_b]
    assert isinstance(result, list)
    assert journal.postings == [entry_posting, counter_posting, same_direction_posting]


def test_cntraccts_preserves_journal_order_for_multiple_counter_accounts(monkeypatch):
    acct_a, acct_b, acct_c, acct_d = object(), object(), object(), object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, acct_a, CREDIT)
    first_counter = _make_posting(journal, acct_b, DEBIT)
    second_counter = _make_posting(journal, acct_c, DEBIT)
    same_direction = _make_posting(journal, acct_d, CREDIT)
    monkeypatch.setattr(
        journal,
        "postings",
        [entry_posting, first_counter, same_direction, second_counter],
    )

    entry = _make_entry(entry_posting)

    assert entry.cntraccts == [acct_b, acct_c]


def test_cntraccts_returns_empty_list_when_no_counter_postings(monkeypatch):
    acct_a, acct_b = object(), object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, acct_a, DEBIT)
    same_direction = _make_posting(journal, acct_b, DEBIT)
    monkeypatch.setattr(journal, "postings", [entry_posting, same_direction])

    entry = _make_entry(entry_posting)

    result = entry.cntraccts

    assert result == []
    assert isinstance(result, list)


def test_cntraccts_returns_empty_list_when_journal_has_only_entry_posting(monkeypatch):
    acct = object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, acct, DEBIT)
    monkeypatch.setattr(journal, "postings", [entry_posting])

    entry = _make_entry(entry_posting)

    assert entry.cntraccts == []


def test_cntraccts_returns_fresh_list_each_call(monkeypatch):
    acct_a, acct_b = object(), object()
    journal = SimpleNamespace(postings=[])
    entry_posting = _make_posting(journal, acct_a, DEBIT)
    counter_posting = _make_posting(journal, acct_b, CREDIT)
    monkeypatch.setattr(journal, "postings", [entry_posting, counter_posting])

    entry = _make_entry(entry_posting)

    first = entry.cntraccts
    second = entry.cntraccts

    assert first == second == [acct_b]
    assert first is not second
    first.append(object())
    assert entry.cntraccts == [acct_b]
