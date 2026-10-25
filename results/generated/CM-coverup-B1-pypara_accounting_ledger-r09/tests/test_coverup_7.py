# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import Ledger, LedgerEntry


class _Account:
    """Minimal concrete implementation of the ``Account`` protocol."""

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None


def test_ledger_entry_cntraccts():
    """
    Test that the ``cntraccts`` property of a ledger entry returns the
    accounts of the postings in the same journal entry whose direction
    differs from the posting of the ledger entry (line 76).
    """
    cash = _Account("100", "Cash")
    sales = _Account("400", "Sales")
    tax = _Account("210", "Sales Tax Payable")

    assert isinstance(cash, Account)

    date = datetime.date(2021, 1, 1)
    entry = JournalEntry(date, "Sale of goods", None)
    entry.post(date, cash, Decimal("120"))    # debit
    entry.post(date, sales, Decimal("-100"))  # credit
    entry.post(date, tax, Decimal("-20"))     # credit

    assert len(entry.postings) == 3

    ledger = Ledger(cash, Balance(date, Decimal("0")))
    ledger_entry = ledger.add(entry.postings[0])

    assert isinstance(ledger_entry, LedgerEntry)
    assert ledger_entry.posting is entry.postings[0]
    assert ledger_entry.balance == Decimal("120")

    # Counter accounts are the accounts of postings with a different direction.
    cntraccts = ledger_entry.cntraccts
    assert cntraccts == [sales, tax]
    assert cash not in cntraccts

    # Same check from the credit side: only the debit posting (cash) is a
    # counter account; the other credit posting (tax) is excluded.
    sales_ledger = Ledger(sales, Balance(date, Decimal("0")))
    sales_entry = sales_ledger.add(entry.postings[1])

    assert sales_entry.balance == Decimal("-100")
    assert sales_entry.cntraccts == [cash]
    assert sales not in sales_entry.cntraccts
    assert tax not in sales_entry.cntraccts

    # Clean up shared state so nothing leaks between tests.
    entry.postings.clear()
    ledger.entries.clear()
    sales_ledger.entries.clear()
    assert entry.postings == []
    assert ledger.entries == []
    assert sales_ledger.entries == []
