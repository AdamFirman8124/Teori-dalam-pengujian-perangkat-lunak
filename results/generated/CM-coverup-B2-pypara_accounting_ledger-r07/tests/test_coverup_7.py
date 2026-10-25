# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.accounts import Account
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Quantity


def _make_account(code: str, name: str) -> Account:
    account = MagicMock(spec=Account)
    account.code = code
    account.name = name
    return account


def test_ledger_entry_cntraccts_returns_opposite_direction_accounts():
    cash = _make_account("100", "Cash")
    sales = _make_account("400", "Sales")
    tax = _make_account("210", "Sales Tax Payable")

    date = datetime.date(2021, 1, 1)
    entry = JournalEntry(date, "Sale of goods", None)
    entry.post(date, cash, Quantity(Decimal("120")))
    entry.post(date, sales, Quantity(Decimal("-100")))
    entry.post(date, tax, Quantity(Decimal("-20")))

    assert len(entry.postings) == 3

    debit_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=entry.postings[0],
        balance=Quantity(Decimal("120")),
    )
    assert debit_entry.cntraccts == [sales, tax]
    assert cash not in debit_entry.cntraccts

    credit_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=entry.postings[1],
        balance=Quantity(Decimal("-100")),
    )
    assert credit_entry.cntraccts == [cash]
    assert sales not in credit_entry.cntraccts
    assert tax not in credit_entry.cntraccts


def test_ledger_entry_cntraccts_empty_when_no_opposite_postings():
    cash = _make_account("100", "Cash")
    other = _make_account("101", "Other Cash")

    date = datetime.date(2021, 1, 2)
    entry = JournalEntry(date, "Transfer", None)
    entry.post(date, cash, Quantity(Decimal("50")))
    entry.post(date, other, Quantity(Decimal("50")))

    assert len(entry.postings) == 2

    ledger_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=entry.postings[0],
        balance=Quantity(Decimal("50")),
    )
    assert ledger_entry.cntraccts == []
