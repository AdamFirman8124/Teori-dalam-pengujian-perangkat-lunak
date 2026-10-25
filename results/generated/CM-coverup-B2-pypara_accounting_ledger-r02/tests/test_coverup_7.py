# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import Ledger, LedgerEntry


class _Account:
    """Minimal structural implementation of the ``Account`` protocol."""

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

    # Debit posting: counter accounts are the credit-side accounts only.
    cntraccts = ledger_entry.cntraccts
    assert cntraccts == [sales, tax]
    assert cash not in cntraccts

    # Credit posting: counter accounts are the debit-side accounts only.
    sales_ledger = Ledger(sales, Balance(date, Decimal("0")))
    sales_entry = sales_ledger.add(entry.postings[1])
    assert sales_entry.cntraccts == [cash]
    assert sales not in sales_entry.cntraccts
    assert tax not in sales_entry.cntraccts

    # Ledger state is local to the test; nothing global was mutated.
    assert ledger.entries == [ledger_entry]
    assert sales_ledger.entries == [sales_entry]
