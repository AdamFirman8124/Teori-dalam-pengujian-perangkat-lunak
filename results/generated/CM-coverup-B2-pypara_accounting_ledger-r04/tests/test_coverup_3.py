# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

"""
Tests for :py:func:`pypara.accounting.ledger.compile_general_ledger_program`.

These tests specifically target the previously uncovered inner ``_program``
closure (lines 220-237), which is only executed when the program returned by
the compiler is actually invoked.
"""

import datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional

import pypara.accounting.ledger as ledger_module
from pypara.accounting.generic import Balance
from pypara.accounting.ledger import (
    GeneralLedger,
    Ledger,
    compile_general_ledger_program,
)
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


@dataclass(frozen=True)
class _StubAccount:
    """
    A minimal, hashable concrete implementation of the ``Account`` protocol.
    """

    code: str
    name: str
    type: str = "ASSET"
    coa: str = "test-coa"
    parent: Optional["_StubAccount"] = None


def test_compile_general_ledger_program_wires_algebra_together(monkeypatch):
    """
    The compiled program must pass the given period to both algebra readers and
    hand their outputs, together with the period, over to ``build_general_ledger``,
    returning whatever it produces.
    """
    period = DateRange(since=datetime.date(2021, 1, 1), until=datetime.date(2021, 12, 31))
    account = _StubAccount(code="100", name="Cash")
    initial_balances: Dict = {account: Balance(datetime.date(2020, 12, 31), Quantity(Decimal("100")))}
    journal_entries: List = []
    sentinel = GeneralLedger(period, {})

    calls: List[tuple] = []

    def fake_read_initial_balances(received_period):
        calls.append(("read_initial_balances", received_period))
        return initial_balances

    def fake_read_journal_entries(received_period):
        calls.append(("read_journal_entries", received_period))
        return journal_entries

    def fake_build_general_ledger(received_period, journal, initial):
        calls.append(("build_general_ledger", received_period, journal, initial))
        return sentinel

    ## Patch ``build_general_ledger`` so we can observe how the compiled program
    ## wires the algebra implementations together (restored automatically):
    monkeypatch.setattr(ledger_module, "build_general_ledger", fake_build_general_ledger)

    program = compile_general_ledger_program(fake_read_initial_balances, fake_read_journal_entries)

    ## The compiler must return a callable program:
    assert callable(program)

    ## Invoke the compiled program:
    result = program(period)

    ## The readers must have been invoked, in order, with the given period, and their
    ## outputs must have been forwarded to ``build_general_ledger``:
    assert calls == [
        ("read_initial_balances", period),
        ("read_journal_entries", period),
        ("build_general_ledger", period, journal_entries, initial_balances),
    ]

    ## The program must return the general ledger produced by ``build_general_ledger``:
    assert result is sentinel

    ## A second invocation must re-execute the whole pipeline (no caching of results):
    another_period = DateRange(since=datetime.date(2022, 1, 1), until=datetime.date(2022, 12, 31))
    result2 = program(another_period)
    assert calls[3:] == [
        ("read_initial_balances", another_period),
        ("read_journal_entries", another_period),
        ("build_general_ledger", another_period, journal_entries, initial_balances),
    ]
    assert result2 is sentinel


def test_compile_general_ledger_program_produces_general_ledger():
    """
    An end-to-end invocation with the real ``build_general_ledger`` must produce a
    general ledger reflecting the initial balances read for the requested period.
    """
    period = DateRange(since=datetime.date(2021, 1, 1), until=datetime.date(2021, 12, 31))
    cash = _StubAccount(code="100", name="Cash")
    sales = _StubAccount(code="400", name="Sales")
    initial_balances = {
        cash: Balance(datetime.date(2020, 12, 31), Quantity(Decimal("1000"))),
    }

    program = compile_general_ledger_program(
        lambda received_period: initial_balances,
        lambda received_period: [],  # no journal entries within the period
    )

    general_ledger = program(period)

    ## The produced general ledger must be bound to the requested period:
    assert isinstance(general_ledger, GeneralLedger)
    assert general_ledger.period == period

    ## A ledger must have been created for each account with an initial balance:
    assert set(general_ledger.ledgers) == {cash}
    cash_ledger = general_ledger.ledgers[cash]
    assert isinstance(cash_ledger, Ledger)
    assert cash_ledger.account == cash
    assert cash_ledger.initial == initial_balances[cash]
    assert cash_ledger.entries == []

    ## Accounts without initial balances and without postings must not appear:
    assert sales not in general_ledger.ledgers

    ## A subsequent invocation with different algebra outputs must produce a fresh
    ## general ledger (i.e., the compiled program itself holds no state):
    empty_ledger = compile_general_ledger_program(lambda received_period: {}, lambda received_period: [])(period)
    assert empty_ledger.period == period
    assert empty_ledger.ledgers == {}
