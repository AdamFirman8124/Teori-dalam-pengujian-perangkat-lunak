# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f097.multiply.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching/teardown is required; each test leaves no state behind.
"""

import pytest

from f097 import multiply


def test_multiply_single_digit_positive():
    # Plain product of the last digits.
    assert multiply(3, 4) == 12
    assert multiply(9, 9) == 81


def test_multiply_negative_operands():
    # Python's % with a positive modulus yields non-negative results:
    # -3 % 10 == 7, -4 % 10 == 6.
    assert multiply(-3, 4) == 28   # 7 * 4
    assert multiply(3, -4) == 18   # 3 * 6
    assert multiply(-3, -4) == 42  # 7 * 6


def test_multiply_multi_digit_operands():
    # Only the last digit of each operand contributes.
    assert multiply(15, 23) == 15  # 5 * 3
    assert multiply(10, 10) == 0   # 0 * 0
    assert multiply(123, 456) == 18  # 3 * 6


def test_multiply_zero_operands():
    assert multiply(0, 0) == 0
    assert multiply(0, 7) == 0
    assert multiply(7, 0) == 0


def test_multiply_float_operands():
    # Floats are supported too: -2.5 % 10 == 7.5.
    assert multiply(2.5, 4) == pytest.approx(10.0)
    assert multiply(-2.5, 4) == pytest.approx(30.0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (-1, 2, 18),   # (-1 % 10) == 9
        (1, -2, 8),    # (-2 % 10) == 8
        (-1, -2, 72),  # 9 * 8
        (12, 34, 8),   # 2 * 4
        (-12, -34, 48),  # 8 * 6
        (0, 5, 0),
    ],
)
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected
