# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_cntraccts_returns_only_opposite_direction_accounts():
    debit = object()
    credit = object()
    entry_account = object()
    same_direction_account = object()
    first_counter_account = object()
    second_counter_account = object()

    journal = SimpleNamespace(postings=[])
    posting = SimpleNamespace(
        journal=journal,
        direction=debit,
        account=entry_account,
    )
    journal.postings = [
        posting,
        SimpleNamespace(direction=debit, account=same_direction_account),
        SimpleNamespace(direction=credit, account=first_counter_account),
        SimpleNamespace(direction=credit, account=second_counter_account),
    ]

    entry = LedgerEntry(ledger=None, posting=posting, balance=None)

    assert entry.cntraccts == [
        first_counter_account,
        second_counter_account,
    ]
