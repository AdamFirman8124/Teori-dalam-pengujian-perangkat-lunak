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


class Q:
    """
    Minimal quantity/amount value supporting the operations used by
    ``JournalEntry.post`` and ``Ledger.add`` (``is_zero``, arithmetic,
    comparisons, ``abs``).
    """

    def __init__(self, value):
        self.value = Decimal(value) if not isinstance(value, Q) else value.value

    def is_zero(self) -> bool:
        return self.value == 0

    def __abs__(self) -> "Q":
        return Q(abs(self.value))

    def __neg__(self) -> "Q":
        return Q(-self.value)

    def __add__(self, other) -> "Q":
        return Q(self.value + (other.value if isinstance(other, Q) else Decimal(other)))

    __radd__ = __add__

    def __mul__(self, other) -> "Q":
        return Q(self.value * (other.value if isinstance(other, Q) else Decimal(other)))

    __rmul__ = __mul__

    def __gt__(self, other) -> bool:
        return self.value > (other.value if isinstance(other, Q) else Decimal(other))

    def __lt__(self, other) -> bool:
        return self.value < (other.value if isinstance(other, Q) else Decimal(other))

    def __eq__(self, other) -> bool:
        if isinstance(other, Q):
            return self.value == other.value
        return self.value == Decimal(other)

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"Q({self.value})"


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
    entry.post(date, cash, Q(120))    # debit
    entry.post(date, sales, Q(-100))  # credit
    entry.post(date, tax, Q(-20))     # credit

    assert len(entry.postings) == 3

    ledger = Ledger(cash, Balance(date, Q(0)))
    ledger_entry = ledger.add(entry.postings[0])

    assert isinstance(ledger_entry, LedgerEntry)

    # The counter accounts must be the accounts of the postings with a
    # direction different from the ledger entry's posting direction.
    cntraccts = ledger_entry.cntraccts
    assert cntraccts == [sales, tax]
    assert cash not in cntraccts

    # For a credit-side posting, only the debit posting (cash) is a
    # counter account; the other credit posting (tax) is not.
    sales_ledger = Ledger(sales, Balance(date, Q(0)))
    sales_entry = sales_ledger.add(entry.postings[1])
    assert sales_entry.cntraccts == [cash]
    assert sales not in sales_entry.cntraccts
    assert tax not in sales_entry.cntraccts
