# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

import datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from unittest.mock import MagicMock

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, JournalEntry
from pypara.accounting.ledger import GeneralLedger, compile_general_ledger_program
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


@dataclass(frozen=True)
class _Account:
    """
    A minimal concrete account satisfying the ``Account`` protocol.
    """
    code: str
    name: str
    type: object = None
    coa: object = None
    parent: Optional["_Account"] = None


def test_compile_general_ledger_program_executes_inner_program():
    """
    Tests that the compiled program (the inner ``_program`` closure) reads initial
    balances and journal entries for the given period and builds a general ledger,
    filtering out journal entries outside the period.
    """
    period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))

    cash = _Account("1000", "Cash")
    sales = _Account("4000", "Sales")

    initial = {cash: Balance(period.since, Quantity(Decimal("100")))}
    read_initial_balances = MagicMock(return_value=initial)

    ## A journal entry within the period, with two postings:
    entry_in_period = JournalEntry(datetime.date(2021, 6, 15), "Sale", "src-doc")
    entry_in_period.post(datetime.date(2021, 6, 15), cash, Quantity(Decimal("50")))
    entry_in_period.post(datetime.date(2021, 6, 15), sales, Quantity(Decimal("50")))

    ## A journal entry outside the period, which must be filtered out:
    entry_out_of_period = JournalEntry(datetime.date(2022, 1, 1), "Next year sale", "src-doc")
    entry_out_of_period.post(datetime.date(2022, 1, 1), cash, Quantity(Decimal("999")))

    read_journal_entries = MagicMock(return_value=[entry_in_period, entry_out_of_period])

    ## Compile the program and execute it (this covers lines 220-237):
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## The algebra implementations must have been invoked with the period:
    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    ## Postconditions on the produced general ledger:
    assert isinstance(ledger, GeneralLedger)
    assert ledger.period == period
    assert set(ledger.ledgers) == {cash, sales}

    ## The initial balance must be carried over into the ledger of the account:
    assert ledger.ledgers[cash].initial == initial[cash]

    ## Only the in-period posting must have been posted to the cash ledger:
    assert len(ledger.ledgers[cash].entries) == 1
    assert ledger.ledgers[cash].entries[0].posting is entry_in_period.postings[0]

    ## The sales ledger must have received its posting:
    assert len(ledger.ledgers[sales].entries) == 1
    assert ledger.ledgers[sales].entries[0].posting is entry_in_period.postings[1]


def test_compile_general_ledger_program_with_no_data():
    """
    Tests that the compiled program produces an empty general ledger when there
    are no initial balances and no journal entries.
    """
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    read_initial_balances = MagicMock(return_value={})
    read_journal_entries = MagicMock(return_value=[])

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    assert isinstance(ledger, GeneralLedger)
    assert ledger.period == period
    assert ledger.ledgers == {}
