# file: project/blib2to3/pgen2/literals.py:58-64
# asked: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}
# gained: {"lines": [59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}

import blib2to3.pgen2.literals as literals_module


def test_test_loops_over_all_256_values(monkeypatch, capsys):
    calls = []
    orig_eval = literals_module.evalString

    def counting_eval(s):
        calls.append(s)
        return orig_eval(s)

    monkeypatch.setattr(literals_module, "evalString", counting_eval)
    result = literals_module.test()
    capsys.readouterr()
    assert result is None
    assert len(calls) == 256
    for i in range(256):
        assert calls[i] == repr(chr(i))


def test_test_prints_on_mismatch(monkeypatch, capsys):
    sentinel = "NOT_EQUAL_SENTINEL_12345_XYZ"
    calls = []

    def fake_eval(s):
        calls.append(s)
        return sentinel

    monkeypatch.setattr(literals_module, "evalString", fake_eval)
    result = literals_module.test()
    out, err = capsys.readouterr()
    assert result is None
    assert len(calls) == 256
    assert out.count(sentinel) == 256
    assert err == ""
    assert "0 " in out
    assert "255 " in out
