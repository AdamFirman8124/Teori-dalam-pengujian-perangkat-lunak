# file: project/pypara/accounting/ledger.py:50-55
# asked: {"lines": [55], "branches": []}
# gained: {"lines": [55], "branches": []}

import datetime
from types import SimpleNamespace

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_date_returns_posting_date():
    expected_date = datetime.date(2024, 1, 31)
    posting = SimpleNamespace(date=expected_date)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=0)

    assert entry.date == expected_date
    assert entry.date is posting.date
