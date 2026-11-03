# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive_float():
    """Calling with a positive float executes line 3 (return number % 1.0)."""
    result = truncate_number(3.75)
    assert result == pytest.approx(0.75)
    assert 0.0 <= result < 1.0


def test_truncate_number_integer_value():
    """An integral float has no fractional part."""
    result = truncate_number(5.0)
    assert result == pytest.approx(0.0)


def test_truncate_number_negative_float():
    """Python's % with a positive divisor yields a non-negative remainder."""
    result = truncate_number(-2.25)
    assert result == pytest.approx(0.75)
    assert 0.0 <= result < 1.0


def test_truncate_number_less_than_one():
    """A value already in [0, 1) is returned unchanged."""
    result = truncate_number(0.5)
    assert result == pytest.approx(0.5)
