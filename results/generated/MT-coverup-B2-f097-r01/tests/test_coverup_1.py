# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f097.multiply to achieve full line and branch coverage.

The function is pure (no I/O, no global state), so no cleanup or
monkeypatching is required; each test is fully isolated.
"""

from f097 import multiply


def test_multiply_single_digits():
    assert multiply(3, 4) == 12


def test_multiply_uses_only_last_digits():
    assert multiply(13, 24) == 12
    assert multiply(123, 456) == 18


def test_multiply_negative_operands():
    # In Python, x % 10 is always non-negative for a positive modulus,
    # so abs() is a no-op here, but these calls exercise it anyway.
    assert multiply(-3, 4) == 28   # (-3 % 10) == 7
    assert multiply(3, -4) == 18   # (-4 % 10) == 6
    assert multiply(-3, -4) == 42  # 7 * 6


def test_multiply_zero_results():
    assert multiply(0, 5) == 0
    assert multiply(10, 20) == 0
