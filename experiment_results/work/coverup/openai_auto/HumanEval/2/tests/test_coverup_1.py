# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import importlib

import pytest


def _get_truncate_number():
    try:
        module = importlib.import_module("script_2")
    except ImportError:
        pytest.skip("script_2 module not importable")
    return getattr(module, "truncate_number", None)


def test_truncate_number_returns_decimal_part():
    func = _get_truncate_number()
    if func is None:
        pytest.skip("truncate_number not found in script_2")

    assert func(3.5) == 0.5
    assert func(3.5) == pytest.approx(0.5)


def test_truncate_number_on_integer_returns_zero():
    func = _get_truncate_number()
    if func is None:
        pytest.skip("truncate_number not found in script_2")

    result = func(7.0)
    assert result == 0.0
    assert result == pytest.approx(0.0)


def test_truncate_number_returns_value_below_one():
    func = _get_truncate_number()
    if func is None:
        pytest.skip("truncate_number not found in script_2")

    result = func(12.75)
    assert result == pytest.approx(0.75)
    assert 0.0 <= result < 1.0


def test_truncate_number_with_monkeypatched_dependency(monkeypatch):
    func = _get_truncate_number()
    if func is None:
        pytest.skip("truncate_number not found in script_2")

    monkeypatch.setattr("builtins.float", float, raising=False)
    assert func(0.25) == pytest.approx(0.25)
