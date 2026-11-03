# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_positive_float():
    result = truncate_number(3.5)
    assert result == pytest.approx(0.5)


def test_truncate_number_negative_float():
    # Python's % follows the sign of the divisor, so -3.5 % 1.0 == 0.5
    result = truncate_number(-3.5)
    assert result == pytest.approx(0.5)


def test_truncate_number_integer_value():
    result = truncate_number(4.0)
    assert result == pytest.approx(0.0)


def test_truncate_number_less_than_one():
    result = truncate_number(0.25)
    assert result == pytest.approx(0.25)
