# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

from datetime import date
from unittest.mock import Mock, call

from pypara.accounting import ledger
from pypara.commons.zeitgeist import DateRange


def test_compile_general_ledger_program_reads_inputs_and_builds_ledger(monkeypatch):
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))
    initial_balances = object()
    journal_entries = object()
    expected_ledger = object()
    calls = []

    read_initial_balances = Mock(
        side_effect=lambda received_period: (
            calls.append(("initial", received_period)),
            initial_balances,
        )[1]
    )
    read_journal_entries = Mock(
        side_effect=lambda received_period: (
            calls.append(("journal", received_period)),
            journal_entries,
        )[1]
    )
    build_general_ledger = Mock(
        side_effect=lambda *args: (
            calls.append(("build", args)),
            expected_ledger,
        )[1]
    )
    monkeypatch.setattr(
        ledger,
        "build_general_ledger",
        build_general_ledger,
    )

    program = ledger.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )

    assert callable(program)
    read_initial_balances.assert_not_called()
    read_journal_entries.assert_not_called()
    build_general_ledger.assert_not_called()

    result = program(period)

    assert result is expected_ledger
    assert read_initial_balances.call_args_list == [call(period)]
    assert read_journal_entries.call_args_list == [call(period)]
    assert build_general_ledger.call_args_list == [
        call(period, journal_entries, initial_balances)
    ]
    assert calls == [
        ("initial", period),
        ("journal", period),
        ("build", (period, journal_entries, initial_balances)),
    ]
