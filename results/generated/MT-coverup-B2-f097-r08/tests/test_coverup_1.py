# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f097.multiply.

The function is pure (no state, no I/O, no side effects), so no cleanup or
monkeypatching is required; simply calling it executes line 3.
"""

import pytest

from f097 import multiply


def test_multiply_basic_positive():
    # 3 % 10 == 3 and 4 % 10 == 4
    assert multiply(3, 4) == 12


def test_multiply_multi_digit_inputs():
    # Only last digits are used: 25 -> 5, 17 -> 7
    assert multiply(25, 17) == 35


def test_multiply_negative_first_argument():
    # Python modulo semantics: -3 % 10 == 7
    assert multiply(-3, 4) == 7 * 4


def test_multiply_negative_second_argument():
    # -6 % 10 == 4
    assert multiply(5, -6) == 5 * 4


def test_multiply_both_negative():
    # -7 % 10 == 3 and -6 % 10 == 4
    assert multiply(-7, -6) == 12


def test_multiply_zero_argument():
    assert multiply(0, 5) == 0


def test_multiply_zero_result_when_multiple_of_ten():
    assert multiply(10, 9) == 0


def test_multiply_float_arguments():
    assert multiply(2.5, 3) == pytest.approx(7.5)
