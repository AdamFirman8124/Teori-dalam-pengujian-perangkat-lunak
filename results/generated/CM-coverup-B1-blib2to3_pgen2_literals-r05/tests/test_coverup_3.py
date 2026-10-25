# file: project/blib2to3/pgen2/literals.py:58-64
# asked: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}
# gained: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}

import blib2to3.pgen2.literals as literals


def test_roundtrip_all_256_chars_no_mismatch(capsys):
    """Covers lines 59-63 and the False branch of line 63/64: every
    repr() of a single character must round-trip through evalString."""
    literals.test()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_roundtrip_mismatch_is_reported(capsys, monkeypatch):
    """Covers the True branch of the comparison on line 63 (print on
    line 64) by forcing evalString to return a wrong value for exactly
    one character. The monkeypatch is reverted automatically."""
    original_eval_string = literals.evalString

    def faulty_eval_string(s):
        result = original_eval_string(s)
        # Corrupt the round-trip only for NUL so exactly one mismatch occurs.
        if result == "\x00":
            return "\x01"
        return result

    monkeypatch.setattr(literals, "evalString", faulty_eval_string)

    literals.test()

    out = capsys.readouterr().out
    lines = out.splitlines()
    # Exactly one mismatch (i == 0) must have been printed by line 64.
    assert len(lines) == 1
    assert lines[0].startswith("0 ")
    assert "'\\x00'" in lines[0]
    assert lines[0].endswith("\x01")
