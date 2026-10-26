# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_with_digits():
    # "5 apples and 6 oranges" -> digits 5, 6 -> n - 11
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    # No digits in string -> sum is 0 -> returns n
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_single_digit():
    # Single numeric token
    assert fruit_distribution("3 mangoes", 7) == 4


def test_fruit_distribution_multi_digit_numbers():
    # Multi-digit tokens exercise int() conversion on longer strings
    assert fruit_distribution("12 apples 34 oranges", 100) == 54


def test_fruit_distribution_empty_string():
    # Empty string splits to [''] -> no digits -> returns n
    assert fruit_distribution("", 5) == 5
