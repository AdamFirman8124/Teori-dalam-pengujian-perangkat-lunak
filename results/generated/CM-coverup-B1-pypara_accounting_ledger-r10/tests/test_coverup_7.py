# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

from types import SimpleNamespace
from pypara.accounting.ledger import LedgerEntry


def _make_entry(posting, ledger=None, balance=0):
    if ledger is None:
        ledger = SimpleNamespace()
    return LedgerEntry(ledger=ledger, posting=posting, balance=balance)


def test_cntraccts_returns_only_opposite_direction_accounts():
    main_account = object()
    same_account = object()
    contra_account = object()
    main_posting = SimpleNamespace(account=main_account, direction="DEBIT", journal=None)
    same_posting = SimpleNamespace(account=same_account, direction="DEBIT", journal=None)
    contra_posting = SimpleNamespace(account=contra_account, direction="CREDIT", journal=None)
    journal = SimpleNamespace(postings=[main_posting, same_posting, contra_posting])
    main_posting.journal = journal
    same_posting.journal = journal
    contra_posting.journal = journal
    entry = _make_entry(main_posting)
    result = entry.cntraccts
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] is contra_account


def test_cntraccts_empty_when_no_counter_accounts():
    main_account = object()
    other_account = object()
    main_posting = SimpleNamespace(account=main_account, direction="CREDIT", journal=None)
    other_posting = SimpleNamespace(account=other_account, direction="CREDIT", journal=None)
    journal = SimpleNamespace(postings=[main_posting, other_posting])
    main_posting.journal = journal
    other_posting.journal = journal
    entry = _make_entry(main_posting)
    result = entry.cntraccts
    assert result == []


def test_cntraccts_returns_multiple_counter_accounts_from_credit_side():
    main_account = object()
    contra1 = object()
    contra2 = object()
    main_posting = SimpleNamespace(account=main_account, direction="CREDIT", journal=None)
    contra_posting1 = SimpleNamespace(account=contra1, direction="DEBIT", journal=None)
    contra_posting2 = SimpleNamespace(account=contra2, direction="DEBIT", journal=None)
    journal = SimpleNamespace(postings=[main_posting, contra_posting1, contra_posting2])
    main_posting.journal = journal
    contra_posting1.journal = journal
    contra_posting2.journal = journal
    entry = _make_entry(main_posting)
    result = entry.cntraccts
    assert len(result) == 2
    assert result[0] is contra1
    assert result[1] is contra2
