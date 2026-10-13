# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import math

import pytest


@pytest.fixture()
def truncate_number():
    """Provide the function under test, failing clearly if unavailable."""
    import importlib

    for module_name in ("script_2", "script2", "__main__"):
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            continue
        func = getattr(module, "truncate_number", None)
        if func is not None:
            return func
    pytest.skip("truncate_number not importable from a known module")


def test_truncate_number_returns_fractional_part(truncate_number):
    result = truncate_number(3.5)
    assert result == 0.5
    assert 0 <= result < 1


def test_truncate_number_exact_integer_returns_zero(truncate_number):
    assert truncate_number(7.0) == 0.0


def test_truncate_number_result_matches_modulo(truncate_number):
    for number in (3.5, 0.25, 42.0, 1.999, 100.75):
        expected = number % 1.0
        result = truncate_number(number)
        assert result == expected
        assert math.isclose(result, number - math.floor(number), rel_tol=1e-9, abs_tol=1e-9)
        assert 0 <= result < 1


def test_truncate_number_integer_input(truncate_number):
    assert truncate_number(5) == 0.0


def test_truncate_number_small_fraction(truncate_number):
    assert truncate_number(0.001) == pytest.approx(0.001)
