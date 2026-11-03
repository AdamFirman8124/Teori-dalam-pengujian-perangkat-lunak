# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

"""
Tests for :mod:`pypara.accounting.ledger`, targeting the previously uncovered
lines:

* ``Ledger._last_balance`` -- both branches: the empty-ledger ``IndexError``
  fallback to the initial balance, and the last-entry lookup;
* ``Ledger.add`` -- ledger entry creation, append to the entry buffer, and
  return of the new entry.

The tests only build local objects and never mutate module-level or global
state, hence no monkeypatching/teardown is required to avoid state pollution.
"""

import datetime
from decimal import Decimal
from typing import Optional

from pypara.accounting.accounts import Account
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import Ledger, LedgerEntry
from pypara.commons.numbers import Amount, Quantity


class StubAccount:
    """Minimal stand-in satisfying the ``Account`` protocol."""

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None


def _make_ledger(initial_value: str = "1000") -> Ledger:
    """Creates a ledger for a stub "Cash" account with the given initial balance."""
    account = StubAccount("100", "Cash")
    initial = Balance(datetime.date(2021, 1, 1), Quantity(Decimal(initial_value)))
    return Ledger(account=account, initial=initial)


def _make_posting(account: Account, direction: Direction, amount: str,
                  when: Optional[datetime.date] = None) -> Posting:
    """Creates a posting (with its backing journal entry) for the given account."""
    when = when if when is not None else datetime.date(2021, 1, 2)
    journal = JournalEntry(when, "Test journal entry", None)
    return Posting(journal, when, account, direction, Amount(Decimal(amount)))


def test_last_balance_of_empty_ledger_falls_back_to_initial_balance():
    """``_last_balance`` returns the initial balance when there are no entries yet."""
    ledger = _make_ledger("1000")

    assert ledger.entries == []
    # Exercises the ``except IndexError`` fallback branch:
    assert ledger._last_balance == Quantity(Decimal("1000"))


def test_add_creates_first_entry_from_initial_balance():
    """
    The first ``add`` must base the entry balance on the initial balance
    (empty-ledger branch of ``_last_balance``), append the entry to the
    ledger buffer and return it.
    """
    # The balance arithmetic below relies on these direction values:
    assert Direction.INC.value == 1
    assert Direction.DEC.value == -1

    ledger = _make_ledger("1000")
    account = ledger.account

    posting = _make_posting(account, Direction.INC, "250")
    entry = ledger.add(posting)

    # The new entry is returned and appended to the ledger buffer:
    assert isinstance(entry, LedgerEntry)
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert ledger.entries == [entry]
    assert ledger.entries[0] is entry

    # Balance = initial (1000) + amount (250) * direction (+1):
    assert entry.balance == Quantity(Decimal("1250"))

    # Delegation post-conditions:
    assert entry.date == posting.date
    assert entry.description == posting.journal.description
    assert entry.amount == posting.amount


def test_add_chains_balance_from_last_entry():
    """
    A subsequent ``add`` must base the new entry balance on the last entry's
    balance (non-empty branch of ``_last_balance``), taking the posting
    direction into account.
    """
    ledger = _make_ledger("1000")
    account = ledger.account

    entry1 = ledger.add(_make_posting(account, Direction.INC, "250"))
    posting2 = _make_posting(account, Direction.DEC, "400")
    entry2 = ledger.add(posting2)

    assert entry2.ledger is ledger
    assert entry2.posting is posting2
    # Balance = last balance (1250) + amount (400) * direction (-1):
    assert entry2.balance == Quantity(Decimal("850"))
    assert ledger.entries == [entry1, entry2]
    assert ledger.entries[1] is entry2

    # ``_last_balance`` now resolves via the last entry (non-empty branch):
    assert ledger._last_balance == entry2.balance
    assert ledger._last_balance == Quantity(Decimal("850"))
