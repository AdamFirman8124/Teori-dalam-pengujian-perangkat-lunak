# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f138.is_equal_to_sum_even.

The function is pure (no I/O, no global state), so no monkeypatching or
cleanup is required; each test is self-contained and leaves no state behind.
"""

from f138 import is_equal_to_sum_even


def test_even_and_at_least_eight_returns_true():
    # Covers branch: (n % 2 == 0) is True AND (n >= 8) is True.
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(100) is True


def test_even_but_below_eight_returns_false():
    # Covers branch: (n % 2 == 0) is True AND (n >= 8) is False.
    assert is_equal_to_sum_even(0) is False
    assert is_equal_to_sum_even(2) is False
    assert is_equal_to_sum_even(6) is False
    assert is_equal_to_sum_even(-4) is False


def test_odd_short_circuits_to_false():
    # Covers branch: (n % 2 == 0) is False, so (n >= 8) is never evaluated.
    assert is_equal_to_sum_even(1) is False
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(9) is False
    assert is_equal_to_sum_even(-3) is False
