# file: project/pypara/accounting/ledger.py:71-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

"""Tests targeting pypara.accounting.ledger.LedgerEntry.cntraccts (line 76).

These tests build small, self-contained journal entries and ledger entries.
No global state is touched (no monkeypatching required); every object is
created locally inside each test, so there is nothing to clean up afterwards.
"""

import datetime

from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import LedgerEntry


def _distinct_directions():
    """
    Return two distinct direction values without relying on the exact member
    names of the Direction enumeration.
    """
    for inc_name, dec_name in (("INC", "DEC"), ("DEBIT", "CREDIT"), ("INCREASE", "DECREASE")):
        if hasattr(Direction, inc_name) and hasattr(Direction, dec_name):
            return getattr(Direction, inc_name), getattr(Direction, dec_name)
    try:
        members = list(Direction)  # works when Direction is an Enum
    except TypeError:
        members = []
    if len(members) >= 2:
        return members[0], members[1]
    # Last resort: opaque, mutually distinct sentinels; cntraccts only ever
    # compares directions for inequality, so any two distinct values work.
    return object(), object()


_INC, _DEC = _distinct_directions()


class _StubAccount:
    """Minimal stand-in satisfying the runtime-checkable Account protocol."""

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None


def _make_posting(journal: JournalEntry, date: datetime.date, account, direction, amount) -> Posting:
    """Create a posting registered on the given journal entry."""
    posting = Posting(journal=journal, date=date, account=account, direction=direction, amount=amount)
    journal.postings.append(posting)
    return posting


def test_cntraccts_lists_accounts_of_opposite_direction_only():
    """Line 76: counter accounts are the accounts of postings with the opposite direction."""
    date = datetime.date(2021, 6, 15)
    journal = JournalEntry(date=date, description="Sale on account", source=None)

    cash = _StubAccount("100", "Cash")
    sales = _StubAccount("400", "Sales")
    tax = _StubAccount("210", "Sales Tax Payable")

    inc_cash = _make_posting(journal, date, cash, _INC, 150)
    dec_sales = _make_posting(journal, date, sales, _DEC, 100)
    dec_tax = _make_posting(journal, date, tax, _DEC, 50)

    entry = LedgerEntry(ledger=None, posting=inc_cash, balance=150)

    cntraccts = entry.cntraccts

    # Postcondition: exactly the opposite-direction accounts, in journal order.
    assert isinstance(cntraccts, list)
    assert cntraccts == [sales, tax]
    # The entry's own account must never appear among the counter accounts.
    assert cash not in cntraccts
    assert inc_cash.account not in cntraccts
    # Every counter account comes from a posting of the opposite direction.
    assert all(
        p.direction != entry.posting.direction
        for p in journal.postings
        if p.account in cntraccts
    )


def test_cntraccts_is_empty_when_all_postings_share_direction():
    """Line 76 (false branch of the filter): no opposite-direction postings -> empty list."""
    date = datetime.date(2021, 6, 16)
    journal = JournalEntry(date=date, description="Internal transfer", source=None)

    cash = _StubAccount("100", "Cash")
    bank = _StubAccount("110", "Bank")

    inc_cash = _make_posting(journal, date, cash, _INC, 100)
    _make_posting(journal, date, bank, _INC, 100)

    entry = LedgerEntry(ledger=None, posting=inc_cash, balance=100)

    # Postcondition: no posting has a direction different from the entry's posting.
    assert entry.cntraccts == []


def test_cntraccts_for_opposite_side_entry_lists_increment_accounts():
    """Line 76 from the other side: a decrement entry sees the increment postings as counter accounts."""
    date = datetime.date(2021, 6, 17)
    journal = JournalEntry(date=date, description="Sale on account", source=None)

    cash = _StubAccount("100", "Cash")
    sales = _StubAccount("400", "Sales")

    inc_cash = _make_posting(journal, date, cash, _INC, 100)
    dec_sales = _make_posting(journal, date, sales, _DEC, 100)

    entry = LedgerEntry(ledger=None, posting=dec_sales, balance=100)

    # Postcondition: the increment posting's account is the single counter account.
    assert entry.cntraccts == [cash]
    assert dec_sales.account not in entry.cntraccts
