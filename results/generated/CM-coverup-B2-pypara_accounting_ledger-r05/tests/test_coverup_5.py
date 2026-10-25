# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_description_returns_journal_description():
    journal = SimpleNamespace(description="Test journal entry")
    posting = SimpleNamespace(journal=journal)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=0)

    assert entry.description == "Test journal entry"
