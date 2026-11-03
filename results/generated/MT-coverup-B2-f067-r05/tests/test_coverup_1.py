# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_with_digits():
    """Covers lines 3-7 including the True branch of the isdigit check."""
    # "5 apples and 6 oranges" -> digits [5, 6], so 19 - 11 = 8
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    """Covers the False branch of the isdigit check (no numbers in string)."""
    # No digits found, so lis stays empty and sum(lis) == 0
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_multiple_digits():
    """Covers multiple iterations of the loop appending several digits."""
    # digits [0, 1, 2] -> 100 - 3 = 97
    assert fruit_distribution("0 apples 1 oranges 2 mangoes", 100) == 97


def test_fruit_distribution_all_digits():
    """Every token is a digit; loop appends each one."""
    # digits [3, 4] -> 12 - 7 = 5
    assert fruit_distribution("3 4", 12) == 5
