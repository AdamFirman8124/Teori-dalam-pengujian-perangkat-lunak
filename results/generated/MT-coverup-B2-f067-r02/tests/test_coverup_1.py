# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_with_digits():
    """Digits in the string are summed and subtracted from n (lines 3-7, isdigit True branch)."""
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    """No digits in the string: sum is 0, so result is n (isdigit False branch)."""
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_zero_and_multiple_digits():
    """Zero counts as a digit and multiple digits are all collected."""
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2


def test_fruit_distribution_all_digits():
    """A string made only of digit tokens sums entirely."""
    assert fruit_distribution("3 4", 10) == 3
