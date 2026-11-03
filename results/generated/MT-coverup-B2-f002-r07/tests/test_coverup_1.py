# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive_fractional():
    """For a positive number with a fractional part, the result is the
    fractional part of the number."""
    result = truncate_number(3.5)
    assert result == pytest.approx(0.5)


def test_truncate_number_integer_value():
    """For a number whose fractional part is zero, the result is zero."""
    result = truncate_number(4.0)
    assert result == pytest.approx(0.0)


def test_truncate_number_negative():
    """For a negative number, Python's modulo returns a positive remainder
    in [0.0, 1.0)."""
    result = truncate_number(-1.25)
    assert result == pytest.approx(0.75)
    assert 0.0 <= result < 1.0


def test_truncate_number_result_always_fractional():
    """The result is always in the interval [0.0, 1.0) for any input."""
    result = truncate_number(123.456)
    assert 0.0 <= result < 1.0
    assert result == pytest.approx(0.456)
