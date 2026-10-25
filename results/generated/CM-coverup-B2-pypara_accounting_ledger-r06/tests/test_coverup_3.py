# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

import datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, compile_general_ledger_program
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


@dataclass(frozen=True)
class AccountStub:
    """Minimal Account implementation satisfying the Account protocol."""

    code: str
    name: str
    type: object = None
    coa: object = None
    parent: Optional["AccountStub"] = None


def _make_entry(date: datetime.date, description: str, source: str) -> JournalEntry:
    """Creates an empty journal entry."""
    return JournalEntry(date, description, source)


class TestCompileGeneralLedgerProgram:
    """
    Tests that `compile_general_ledger_program` compiles the algebra into a working
    general ledger program (covers the inner `_program` function and its return).
    """

    def test_should_produce_general_ledger_from_initial_balances_and_journal(self) -> None:
        period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))
        cash = AccountStub("100", "Cash")
        sales = AccountStub("400", "Sales")
        receivable = AccountStub("120", "Receivables")

        initial_balances: Dict[AccountStub, Balance] = {
            cash: Balance(period.since, Quantity(Decimal("1000"))),
        }

        initial_calls: List[DateRange] = []
        journal_calls: List[DateRange] = []

        def read_initial_balances(p: DateRange) -> Dict[AccountStub, Balance]:
            initial_calls.append(p)
            return initial_balances

        def read_journal_entries(p: DateRange) -> List[JournalEntry]:
            journal_calls.append(p)

            in_period = _make_entry(datetime.date(2021, 3, 1), "Cash sale", "src-1")
            in_period.post(datetime.date(2021, 3, 1), cash, Quantity(Decimal("250")))
            in_period.post(datetime.date(2021, 3, 1), sales, Quantity(Decimal("-250")))

            out_of_period = _make_entry(datetime.date(2020, 6, 1), "Prior-year entry", "src-2")
            out_of_period.post(datetime.date(2020, 6, 1), receivable, Quantity(Decimal("999")))

            return [in_period, out_of_period]

        program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

        ## The compiler must return a callable program (line 237):
        assert callable(program)

        ledger = program(period)

        ## Both algebra implementations must have been invoked exactly once, with the period:
        assert initial_calls == [period]
        assert journal_calls == [period]

        ## Postconditions on the produced general ledger:
        assert isinstance(ledger, GeneralLedger)
        assert ledger.period == period

        ## The out-of-period account must not appear; in-period accounts must:
        assert set(ledger.ledgers) == {cash, sales}

        ## The cash ledger starts from the initial balance and includes the debit posting:
        cash_ledger = ledger.ledgers[cash]
        assert cash_ledger.initial == initial_balances[cash]
        assert len(cash_ledger.entries) == 1
        assert cash_ledger.entries[0].balance == Quantity(Decimal("1250"))

        ## The sales ledger has no initial balance and includes the credit posting:
        sales_ledger = ledger.ledgers[sales]
        assert sales_ledger.initial.value == Quantity(Decimal("0"))
        assert len(sales_ledger.entries) == 1
        assert sales_ledger.entries[0].balance == Quantity(Decimal("-250"))

    def test_should_produce_empty_general_ledger_when_no_data(self) -> None:
        period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))

        def read_initial_balances(p: DateRange) -> Dict[AccountStub, Balance]:
            return {}

        def read_journal_entries(p: DateRange) -> List[JournalEntry]:
            return []

        program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
        ledger = program(period)

        assert isinstance(ledger, GeneralLedger)
        assert ledger.period == period
        assert ledger.ledgers == {}
