# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import math

import pytest

from script_2 import truncate_number


def test_truncate_number_documented_example():
    assert truncate_number(3.5) == 0.5


def test_truncate_number_integer_part():
    assert truncate_number(4.0) == 0.0


def test_truncate_number_negative_remainder():
    # Python modulo keeps the sign of the divisor, so the result stays in [0, 1)
    assert truncate_number(-2.25) == pytest.approx(0.75)
    assert truncate_number(-0.5) == pytest.approx(0.5)


def test_truncate_number_always_fractional():
    for value in (0.0, 1.5, 7.125, 123.999, -0.5, -3.75):
        result = truncate_number(value)
        assert 0.0 <= result < 1.0
        # decompose into floor part and decimals
        assert value == pytest.approx(math.floor(value) + result)
