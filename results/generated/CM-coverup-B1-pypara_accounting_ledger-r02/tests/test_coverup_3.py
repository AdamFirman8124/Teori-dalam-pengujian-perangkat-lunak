# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

from datetime import date

from pypara.accounting import ledger as ledger_module
from pypara.commons.zeitgeist import DateRange


def test_compile_general_ledger_program_reads_inputs_and_builds_ledger(monkeypatch):
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))
    initial_balances = object()
    journal_entries = object()
    expected_ledger = object()
    calls = []

    def read_initial_balances(received_period):
        calls.append(("initial", received_period))
        return initial_balances

    def read_journal_entries(received_period):
        calls.append(("journal", received_period))
        return journal_entries

    def build_general_ledger(received_period, received_journal, received_initial):
        calls.append(
            ("build", received_period, received_journal, received_initial)
        )
        return expected_ledger

    monkeypatch.setattr(
        ledger_module, "build_general_ledger", build_general_ledger
    )

    program = ledger_module.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )
    result = program(period)

    assert result is expected_ledger
    assert calls == [
        ("initial", period),
        ("journal", period),
        ("build", period, journal_entries, initial_balances),
    ]
