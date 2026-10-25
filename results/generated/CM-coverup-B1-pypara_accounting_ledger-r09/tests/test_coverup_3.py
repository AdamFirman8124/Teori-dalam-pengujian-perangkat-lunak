# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, compile_general_ledger_program
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


@dataclass(frozen=True)
class MockAccount:
    """Minimal concrete implementation of the Account protocol."""

    code: str
    name: str
    type: object = None
    coa: object = None
    parent: Optional["MockAccount"] = None


PERIOD = DateRange(date(2021, 1, 1), date(2021, 12, 31))


def test_compile_general_ledger_program_builds_general_ledger():
    """
    compile_general_ledger_program must return a program which, when invoked with a
    period, reads initial balances and journal entries for that exact period and
    builds a general ledger from them.
    """
    cash = MockAccount("100", "Cash")
    sales = MockAccount("400", "Sales")

    initial = {cash: Balance(PERIOD.since, Quantity(Decimal("1000")))}

    ## A journal entry inside the period with two postings:
    entry1 = JournalEntry(date(2021, 3, 1), "Sale", "src-1")
    entry1 = entry1.post(date(2021, 3, 1), cash, Quantity(Decimal("250")))
    entry1 = entry1.post(date(2021, 3, 1), sales, Quantity(Decimal("-250")))

    ## A journal entry outside the period; its postings must be ignored:
    entry_outside = JournalEntry(date(2020, 6, 1), "Prior year", "src-2")
    entry_outside = entry_outside.post(date(2020, 6, 1), cash, Quantity(Decimal("999")))

    entries = [entry1, entry_outside]

    calls = {"initial": [], "journal": []}

    def read_initial_balances(period):
        calls["initial"].append(period)
        return initial

    def read_journal_entries(period):
        calls["journal"].append(period)
        return entries

    ## Compile the program (this is the `return _program` line under test):
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Invoke the compiled program (this executes the body of `_program`):
    result = program(PERIOD)

    ## Both algebra implementations must have been called with the given period:
    assert calls["initial"] == [PERIOD]
    assert calls["journal"] == [PERIOD]

    ## The result must be a general ledger for the requested period:
    assert isinstance(result, GeneralLedger)
    assert result.period == PERIOD

    ## Only the in-period posting accounts appear; the out-of-period posting is excluded:
    assert set(result.ledgers) == {cash, sales}

    ## The ledger for `cash` carries the initial balance as given:
    assert result.ledgers[cash].initial is initial[cash]
    assert result.ledgers[cash].initial.date == PERIOD.since

    ## Exactly one in-period posting was applied to each account ledger:
    assert len(result.ledgers[cash].entries) == 1
    assert len(result.ledgers[sales].entries) == 1

    ## The ledger for `sales` was created fresh with a zero balance dated at period start:
    assert result.ledgers[sales].initial.date == PERIOD.since
    assert result.ledgers[sales].initial.value == Quantity(Decimal("0"))


def test_compile_general_ledger_program_is_reusable():
    """
    The compiled program must be callable multiple times, forwarding each period
    to the underlying algebra implementations.
    """
    account = MockAccount("100", "Cash")
    period1 = DateRange(date(2021, 1, 1), date(2021, 12, 31))
    period2 = DateRange(date(2022, 1, 1), date(2022, 12, 31))

    def read_initial_balances(period):
        return {account: Balance(period.since, Quantity(Decimal("10")))}

    def read_journal_entries(period):
        entry = JournalEntry(period.since, "Entry", "src")
        return [entry.post(period.since, account, Quantity(Decimal("5")))]

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    result1 = program(period1)
    result2 = program(period2)

    assert result1.period == period1
    assert result2.period == period2
    assert result1 is not result2
    assert result1.ledgers[account].initial.date == period1.since
    assert result2.ledgers[account].initial.date == period2.since
    assert len(result1.ledgers[account].entries) == 1
    assert len(result2.ledgers[account].entries) == 1
