# file: project/pypara/accounting/ledger.py:207-237
# asked: {"lines": [220, 228, 231, 234, 237], "branches": []}
# gained: {"lines": [220, 228, 231, 234, 237], "branches": []}

import pypara.accounting.ledger as ledger_module


def test_compile_general_ledger_program_delegates_and_returns_ledger(monkeypatch):
    period = object()
    fake_initial_balances = object()
    fake_journal_entries = object()
    expected_ledger = object()
    seen = {}

    def fake_read_initial_balances(p):
        seen["initial_period"] = p
        return fake_initial_balances

    def fake_read_journal_entries(p):
        seen["journal_period"] = p
        return fake_journal_entries

    def fake_build_general_ledger(p, journal, initial):
        seen["build_args"] = (p, journal, initial)
        return expected_ledger

    monkeypatch.setattr(ledger_module, "build_general_ledger", fake_build_general_ledger)

    program = ledger_module.compile_general_ledger_program(
        fake_read_initial_balances, fake_read_journal_entries
    )

    assert callable(program)

    result = program(period)

    assert seen["initial_period"] is period
    assert seen["journal_period"] is period
    assert seen["build_args"][0] is period
    assert seen["build_args"][1] is fake_journal_entries
    assert seen["build_args"][2] is fake_initial_balances
    assert result is expected_ledger


def test_compile_general_ledger_program_forwards_each_period_independently(monkeypatch):
    calls = {"initial": [], "journal": [], "build": []}

    def fake_read_initial_balances(p):
        calls["initial"].append(p)
        return {"initial-for": p}

    def fake_read_journal_entries(p):
        calls["journal"].append(p)
        return ["journal-for", p]

    def fake_build_general_ledger(p, journal, initial):
        calls["build"].append((p, journal, initial))
        return ("ledger-for", p)

    monkeypatch.setattr(ledger_module, "build_general_ledger", fake_build_general_ledger)

    program = ledger_module.compile_general_ledger_program(
        fake_read_initial_balances, fake_read_journal_entries
    )

    period_one = object()
    period_two = object()

    result_one = program(period_one)
    result_two = program(period_two)

    assert calls["initial"] == [period_one, period_two]
    assert calls["journal"] == [period_one, period_two]
    assert len(calls["build"]) == 2
    assert calls["build"][0][0] is period_one
    assert calls["build"][1][0] is period_two
    assert calls["build"][0][1] == ["journal-for", period_one]
    assert calls["build"][0][2] == {"initial-for": period_one}
    assert calls["build"][1][1] == ["journal-for", period_two]
    assert calls["build"][1][2] == {"initial-for": period_two}
    assert result_one == ("ledger-for", period_one)
    assert result_two == ("ledger-for", period_two)
    assert result_one is not result_two


def test_compile_general_ledger_program_closures_are_independent(monkeypatch):
    seen = {}

    def fake_build_general_ledger(p, journal, initial):
        return (p, journal, initial)

    monkeypatch.setattr(ledger_module, "build_general_ledger", fake_build_general_ledger)

    def read_initial_a(p):
        return "initial-a"

    def read_journal_a(p):
        return "journal-a"

    def read_initial_b(p):
        return "initial-b"

    def read_journal_b(p):
        return "journal-b"

    program_a = ledger_module.compile_general_ledger_program(read_initial_a, read_journal_a)
    program_b = ledger_module.compile_general_ledger_program(read_initial_b, read_journal_b)

    assert program_a is not program_b

    period = object()
    result_a = program_a(period)
    result_b = program_b(period)

    assert result_a == (period, "journal-a", "initial-a")
    assert result_b == (period, "journal-b", "initial-b")
    assert seen == {}
