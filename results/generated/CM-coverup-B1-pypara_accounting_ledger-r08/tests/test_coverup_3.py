# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

from unittest.mock import Mock, call, sentinel

import pypara.accounting.ledger as ledger


def test_compile_general_ledger_program_reads_inputs_and_builds_ledger(monkeypatch):
    calls = []
    period = sentinel.period
    initial_balances = sentinel.initial_balances
    journal_entries = sentinel.journal_entries
    expected_ledger = sentinel.general_ledger

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
        side_effect=lambda received_period, received_journal, received_initial: (
            calls.append(
                (
                    "build",
                    received_period,
                    received_journal,
                    received_initial,
                )
            ),
            expected_ledger,
        )[1]
    )
    monkeypatch.setattr(ledger, "build_general_ledger", build_general_ledger)

    program = ledger.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )

    assert callable(program)
    assert calls == []

    result = program(period)

    assert result is expected_ledger
    assert calls == [
        ("initial", period),
        ("journal", period),
        ("build", period, journal_entries, initial_balances),
    ]
    assert read_initial_balances.call_args_list == [call(period)]
    assert read_journal_entries.call_args_list == [call(period)]
    assert build_general_ledger.call_args_list == [
        call(period, journal_entries, initial_balances)
    ]
