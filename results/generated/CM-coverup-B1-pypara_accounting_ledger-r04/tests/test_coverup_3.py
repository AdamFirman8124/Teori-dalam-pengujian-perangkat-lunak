# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

from datetime import date
from unittest.mock import Mock

import pypara.accounting.ledger as ledger
from pypara.commons.zeitgeist import DateRange


def test_compile_general_ledger_program_reads_and_builds_ledger(monkeypatch):
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))
    initial_balances = {}
    journal_entries = ()
    expected = ledger.GeneralLedger(period, {})

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    build_general_ledger = Mock(return_value=expected)
    monkeypatch.setattr(ledger, "build_general_ledger", build_general_ledger)

    program = ledger.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )

    read_initial_balances.assert_not_called()
    read_journal_entries.assert_not_called()
    build_general_ledger.assert_not_called()

    result = program(period)

    assert result is expected
    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)
    build_general_ledger.assert_called_once_with(
        period,
        journal_entries,
        initial_balances,
    )
