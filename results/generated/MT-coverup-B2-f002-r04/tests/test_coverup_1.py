# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_integer_part_only():
    """An integer float has no fractional part; result must be 0.0."""
    assert truncate_number(5.0) == 0.0


def test_truncate_number_fractional_part():
    """The fractional part of 3.75 is 0.75."""
    assert truncate_number(3.75) == pytest.approx(0.75)


def test_truncate_number_negative_number():
    """Python's % yields a result with the sign of the divisor (1.0), so -1.5 -> 0.5."""
    assert truncate_number(-1.5) == pytest.approx(0.5)


def test_truncate_number_negative_integer():
    """-4.0 % 1.0 is 0.0."""
    assert truncate_number(-4.0) == 0.0


def test_truncate_number_zero():
    """Zero has no fractional part."""
    assert truncate_number(0.0) == 0.0


def test_truncate_number_large_value():
    """Large values still return only the fractional part."""
    assert truncate_number(123456.789) == pytest.approx(0.789)


def test_truncate_number_result_in_unit_interval():
    """Postcondition: result is always in [0.0, 1.0) for any finite input."""
    for value in (0.0, 1.0, 2.5, -3.25, 100.999, -0.001):
        result = truncate_number(value)
        assert 0.0 <= result < 1.0
        assert result == pytest.approx(value % 1.0)
