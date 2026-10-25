# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_basic():
    # "5 apples and 6 oranges" -> digits [5, 6], n=19 -> 19 - 11 = 8
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    # No digits in string -> lis stays empty -> returns n
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_single_digit():
    # Single digit -> lis = [1] -> 21 - 1 = 20
    assert fruit_distribution("1 apple", 21) == 20


def test_fruit_distribution_multi_digit_numbers():
    # Multi-digit tokens are parsed as full numbers
    assert fruit_distribution("100 apples and 25 oranges", 150) == 25


def test_fruit_distribution_zero_total():
    # All fruit accounted for -> result is zero
    assert fruit_distribution("0 apples 0 oranges 0 mangoes", 0) == 0


def test_fruit_distribution_mixed_tokens():
    # Mixed alphanumeric tokens: only purely-numeric tokens count
    assert fruit_distribution("3 apples 4 oranges 5apples", 12) == 5
