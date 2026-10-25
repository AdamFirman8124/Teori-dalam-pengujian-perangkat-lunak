# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Quantity


def _make_account(code: str, name: str) -> Account:
    account = MagicMock(spec=Account)
    account.code = code
    account.name = name
    return account


def test_ledger_entry_cntraccts():
    """
    Test that the ``cntraccts`` property of a ledger entry returns the
    accounts of the postings in the same journal entry whose direction
    differs from the posting of the ledger entry (line 76).
    """
    cash = _make_account("100", "Cash")
    sales = _make_account("400", "Sales")
    tax = _make_account("210", "Sales Tax Payable")

    date = datetime.date(2021, 1, 1)
    entry = JournalEntry(date, "Sale of goods", None)
    entry.post(date, cash, Quantity(Decimal("120")))    # debit
    entry.post(date, sales, Quantity(Decimal("-100")))  # credit
    entry.post(date, tax, Quantity(Decimal("-20")))     # credit

    assert len(entry.postings) == 3

    # Debit-side ledger entry: counter accounts are the credit postings.
    ledger = Ledger(cash, Balance(date, Quantity(Decimal("0"))))
    ledger_entry = ledger.add(entry.postings[0])

    assert isinstance(ledger_entry, LedgerEntry)
    assert ledger_entry.cntraccts == [sales, tax]
    assert cash not in ledger_entry.cntraccts

    # Credit-side ledger entry: only the debit posting is a counter account.
    sales_ledger = Ledger(sales, Balance(date, Quantity(Decimal("0"))))
    sales_entry = sales_ledger.add(entry.postings[1])

    assert sales_entry.cntraccts == [cash]
    assert sales not in sales_entry.cntraccts
    assert tax not in sales_entry.cntraccts


def test_ledger_entry_cntraccts_empty_when_no_counter_postings():
    """
    A journal entry whose postings all share the same direction yields an
    empty counter-account list.
    """
    cash = _make_account("100", "Cash")
    bank = _make_account("110", "Bank")

    date = datetime.date(2021, 2, 1)
    entry = JournalEntry(date, "Transfer", None)
    entry.post(date, cash, Quantity(Decimal("50")))   # debit
    entry.post(date, bank, Quantity(Decimal("25")))   # debit

    ledger = Ledger(cash, Balance(date, Quantity(Decimal("0"))))
    ledger_entry = ledger.add(entry.postings[0])

    assert ledger_entry.cntraccts == []
