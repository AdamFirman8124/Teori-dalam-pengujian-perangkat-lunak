# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.accounts import Account
from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.ledger import LedgerEntry


def _make_account(code: str, name: str) -> Account:
    account = MagicMock(spec=Account)
    account.code = code
    account.name = name
    return account


def _make_posting(journal, date, account, direction, amount):
    return Posting(
        journal=journal,
        date=date,
        account=account,
        direction=direction,
        amount=Decimal(amount),
    )


def test_ledger_entry_cntraccts_returns_opposite_direction_accounts():
    cash = _make_account("100", "Cash")
    sales = _make_account("400", "Sales")
    tax = _make_account("210", "Sales Tax Payable")

    date = datetime.date(2021, 1, 1)
    journal = JournalEntry(date, "Sale of goods", None)

    debit_posting = _make_posting(journal, date, cash, "DEBIT", "120")
    sales_posting = _make_posting(journal, date, sales, "CREDIT", "100")
    tax_posting = _make_posting(journal, date, tax, "CREDIT", "20")
    journal.postings.extend([debit_posting, sales_posting, tax_posting])

    debit_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=debit_posting,
        balance=Decimal("120"),
    )
    assert debit_entry.cntraccts == [sales, tax]
    assert cash not in debit_entry.cntraccts

    credit_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=sales_posting,
        balance=Decimal("100"),
    )
    assert credit_entry.cntraccts == [cash]
    assert sales not in credit_entry.cntraccts
    assert tax not in credit_entry.cntraccts


def test_ledger_entry_cntraccts_empty_when_no_opposite_direction_postings():
    cash = _make_account("100", "Cash")
    other_cash = _make_account("101", "Petty Cash")

    date = datetime.date(2021, 1, 2)
    journal = JournalEntry(date, "Transfer", None)

    posting = _make_posting(journal, date, cash, "DEBIT", "50")
    same_direction = _make_posting(journal, date, other_cash, "DEBIT", "50")
    journal.postings.extend([posting, same_direction])

    entry = LedgerEntry(
        ledger=MagicMock(),
        posting=posting,
        balance=Decimal("50"),
    )
    assert entry.cntraccts == []

    single_journal = JournalEntry(date, "Single posting", None)
    single_posting = _make_posting(single_journal, date, cash, "CREDIT", "10")
    single_journal.postings.append(single_posting)

    single_entry = LedgerEntry(
        ledger=MagicMock(),
        posting=single_posting,
        balance=Decimal("10"),
    )
    assert single_entry.cntraccts == []
