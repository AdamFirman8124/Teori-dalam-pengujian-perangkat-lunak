# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

import datetime
from unittest.mock import Mock

import pytest

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry


def _make_entry(description: str) -> LedgerEntry:
    journal = Mock()
    journal.description = description
    posting = Posting(
        journal=journal,
        date=datetime.date(2024, 1, 1),
        account=Mock(),
        direction=Mock(),
        amount=Mock(),
    )
    return LedgerEntry(ledger=Mock(), posting=posting, balance=Mock())


def test_ledger_entry_description_returns_journal_description():
    entry = _make_entry("Opening balance entry")

    assert entry.description == "Opening balance entry"
    assert entry.description is entry.posting.journal.description


def test_ledger_entry_description_is_read_from_journal_each_time():
    entry = _make_entry("First description")
    assert entry.description == "First description"

    entry.posting.journal.description = "Second description"

    assert entry.description == "Second description"


def test_ledger_entry_description_with_empty_journal_description():
    entry = _make_entry("")

    assert entry.description == ""
