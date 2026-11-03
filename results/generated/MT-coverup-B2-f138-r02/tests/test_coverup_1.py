# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


def test_even_and_at_least_eight_returns_true():
    # n % 2 == 0 is True and n >= 8 is True -> True
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True


def test_even_but_below_eight_returns_false():
    # Covers the False branch of the second condition (n >= 8)
    assert is_equal_to_sum_even(6) is False
    assert is_equal_to_sum_even(0) is False


def test_odd_number_returns_false():
    # Covers the False branch of the first condition (n % 2 == 0)
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(9) is False


def test_negative_even_number_returns_false():
    # Even but below 8 -> False
    assert is_equal_to_sum_even(-2) is False
