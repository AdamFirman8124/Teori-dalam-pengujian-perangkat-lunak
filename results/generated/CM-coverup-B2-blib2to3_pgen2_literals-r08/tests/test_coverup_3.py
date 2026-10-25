# file: project/blib2to3/pgen2/literals.py:58-64
# asked: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}
# gained: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}

"""Tests covering the module-level test() helper in blib2to3/pgen2/literals.py."""

import blib2to3.pgen2.literals as literals


def test_eval_string_round_trips_every_byte_value() -> None:
    """Postcondition: repr() of every chr(i), i in range(256), round-trips."""
    for i in range(256):
        c = chr(i)
        s = repr(c)
        assert literals.evalString(s) == c, (i, c, s)


def test_module_test_function_executes_loop_without_mismatches(capsys) -> None:
    """Calling test() runs lines 59-63 and prints nothing when all match."""
    literals.test()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_module_test_function_prints_on_mismatch(monkeypatch, capsys) -> None:
    """Force a mismatch so the print branch (line 64) executes."""
    real_eval = literals.evalString
    calls = []

    def fake_eval(s):
        calls.append(s)
        if len(calls) == 1:
            return "\x00wrong"
        return real_eval(s)

    monkeypatch.setattr(literals, "evalString", fake_eval)
    literals.test()

    out = capsys.readouterr().out
    lines = out.splitlines()
    assert len(lines) == 1
    assert lines[0].startswith("0 ")
    assert "wrong" in lines[0]
    assert len(calls) == 256

    # Cleanup check: monkeypatch restores the original function.
    monkeypatch.undo()
    assert literals.evalString is real_eval
    assert literals.evalString(repr("\x00")) == "\x00"
