# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import build_general_ledger


@dataclass(frozen=True)
class MockAccount:
    """
    A minimal concrete implementation of the Account protocol for testing.
    """
    code: str
    name: str
    type: object = None
    coa: object = None
    parent: Optional["MockAccount"] = None


def test_build_general_ledger_empty():
    """
    Building a general ledger with no initial balances and an empty journal
    must yield an empty ledger map for the given period.
    """
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    gl = build_general_ledger(period, [], {})

    assert gl.period == period
    assert gl.ledgers == {}


def test_build_general_ledger_with_initial_balances_and_journal():
    """
    Building a general ledger must:
    - seed ledgers from initial balances (line 174),
    - skip journal entries outside the period (line 177 filter),
    - create ledgers on the fly for accounts without initial balances
      (lines 179-180),
    - attach postings to the correct ledgers (line 183),
    - return a GeneralLedger carrying the period (line 186).
    """
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since, until)

    cash = MockAccount("100", "Cash")
    sales = MockAccount("400", "Sales")
    rent = MockAccount("500", "Rent")

    # Initial balance only for 'cash':
    initial = {cash: Balance(since, Quantity(Decimal("100")))}

    # Entry within the period, touching an account with an initial balance
    # and an account without one:
    e1 = JournalEntry(datetime.date(2023, 3, 1), "sale", None)
    e1.post(datetime.date(2023, 3, 1), cash, Quantity(Decimal("50")))
    e1.post(datetime.date(2023, 3, 1), sales, Quantity(Decimal("-50")))

    # Entry before the period: must be filtered out entirely:
    e2 = JournalEntry(datetime.date(2022, 6, 1), "old sale", None)
    e2.post(datetime.date(2022, 6, 1), cash, Quantity(Decimal("999")))

    # Entry after the period: must be filtered out entirely:
    e3 = JournalEntry(datetime.date(2024, 1, 1), "future rent", None)
    e3.post(datetime.date(2024, 1, 1), rent, Quantity(Decimal("10")))

    # Entry within the period for an account with no initial balance:
    # exercises the 'posting.account not in ledgers' branch (lines 179-180).
    e4 = JournalEntry(datetime.date(2023, 7, 15), "rent expense", None)
    e4.post(datetime.date(2023, 7, 15), rent, Quantity(Decimal("30")))

    gl = build_general_ledger(period, [e1, e2, e3, e4], initial)

    # The returned general ledger carries the requested period:
    assert gl.period == period

    # Only accounts with initial balances or in-period postings appear;
    # 'rent' was created on the fly despite having no initial balance,
    # and no ledger exists for postings of out-of-period entries only.
    assert set(gl.ledgers.keys()) == {cash, sales, rent}

    # Ledger seeded from the initial balance keeps it as its opening balance:
    assert gl.ledgers[cash].initial == Balance(since, Quantity(Decimal("100")))
    assert gl.ledgers[cash].account == cash

    # Ledger created on the fly starts from a zero balance at period start:
    assert gl.ledgers[rent].initial == Balance(since, Quantity(Decimal("0")))
    assert gl.ledgers[rent].account == rent

    # In-period postings are attached to their ledgers exactly once:
    assert len(gl.ledgers[cash].entries) == 1
    assert len(gl.ledgers[sales].entries) == 1
    assert len(gl.ledgers[rent].entries) == 1

    # Out-of-period postings must not have been recorded anywhere:
    all_postings = [entry for ledger in gl.ledgers.values() for entry in ledger.entries]
    assert len(all_postings) == 3
