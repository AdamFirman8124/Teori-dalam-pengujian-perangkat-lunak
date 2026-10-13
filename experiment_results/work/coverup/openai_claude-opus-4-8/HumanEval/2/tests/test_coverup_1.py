# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import importlib

import pytest


def test_truncate_number_covers_return(monkeypatch):
    script_2 = importlib.import_module("script_2")
    monkeypatch.setattr(script_2, "__name__", "script_2")

    assert script_2.truncate_number(3.5) == pytest.approx(0.5)
    assert script_2.truncate_number(0.5) == pytest.approx(0.5)
    assert script_2.truncate_number(4.0) == pytest.approx(0.0)
    assert script_2.truncate_number(123.456) == pytest.approx(0.456)
    result = script_2.truncate_number(-3.25)
    assert 0.0 <= result < 1.0
    assert result == pytest.approx(0.75)
