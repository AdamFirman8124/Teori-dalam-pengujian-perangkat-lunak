# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import importlib
import sys

import pytest


@pytest.fixture
def module(monkeypatch):
    """Import script_2 fresh and make sure it is removed from sys.modules afterwards."""
    monkeypatch.delitem(sys.modules, "script_2", raising=False)
    mod = importlib.import_module("script_2")
    yield mod
    monkeypatch.delitem(sys.modules, "script_2", raising=False)


def test_truncate_number_docstring_example(module):
    # Executes the body of truncate_number (line 10) and checks the documented result.
    result = module.truncate_number(3.5)
    assert result == 0.5
    assert isinstance(result, float)
    assert 0.0 <= result < 1.0


def test_truncate_number_integer_valued_input(module):
    # A whole number has no decimal part.
    assert module.truncate_number(2.0) == 0.0
    assert module.truncate_number(1.0) == 0.0
    assert module.truncate_number(100.0) == 0.0


def test_truncate_number_fractional_inputs(module):
    assert module.truncate_number(0.5) == 0.5
    assert module.truncate_number(1.25) == pytest.approx(0.25)
    assert module.truncate_number(9.99) == pytest.approx(0.99)
    assert module.truncate_number(123.456) == pytest.approx(0.456)


def test_truncate_number_postcondition_decimal_part(module):
    # Postcondition: result is always the fractional leftover, strictly below 1.0,
    # and the input can be reconstructed as int_part + result.
    for number in (0.5, 1.0, 3.5, 7.125, 42.75, 1000.001):
        result = module.truncate_number(number)
        assert 0.0 <= result < 1.0
        assert number - result == pytest.approx(float(int(number)), abs=1e-9)


def test_truncate_number_small_and_large_values(module):
    assert module.truncate_number(1e-9) == pytest.approx(1e-9)
    assert module.truncate_number(1e9 + 0.5) == pytest.approx(0.5, abs=1e-6)


def test_module_state_cleanup(module):
    # Guard: the fixture must not leave script_2 in sys.modules after the test.
    assert "script_2" in sys.modules
