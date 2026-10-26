# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_mixed_digits_and_words():
    # "5 apples and 6 oranges" -> digits 5 and 6 -> n - 11
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    # No digit tokens -> lis stays empty -> returns n
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_single_digit_token():
    assert fruit_distribution("0 apples", 3) == 3


def test_fruit_distribution_multi_digit_tokens():
    assert fruit_distribution("12 apples 34 oranges", 100) == 54
