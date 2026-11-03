# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_with_digits_and_words():
    # Covers: lis creation, loop, isdigit() True branch, append, and return.
    result = fruit_distribution("5 apples and 6 oranges", 19)
    assert result == 8  # 19 - (5 + 6)


def test_fruit_distribution_with_no_digits():
    # Covers the isdigit() False branch (no numbers in the string).
    result = fruit_distribution("apples and oranges", 10)
    assert result == 10  # 10 - sum([])


def test_fruit_distribution_with_only_digits():
    result = fruit_distribution("0 0", 7)
    assert result == 7  # 7 - (0 + 0)


def test_fruit_distribution_empty_string():
    # Covers split on an empty string (loop body runs once with "").
    result = fruit_distribution("", 3)
    assert result == 3  # "" is not a digit, so sum([]) == 0
