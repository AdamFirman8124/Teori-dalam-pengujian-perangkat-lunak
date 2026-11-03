# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_mixed_tokens():
    """Covers lines 3-7: list creation, loop, isdigit() True branch,
    append(int(i)), and the return statement."""
    # "5" and "6" are digits -> appended; words are not.
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Postcondition: result equals n minus the sum of all digit tokens.
    assert fruit_distribution("0 apples 1 orange 2 bananas", 10) == 7


def test_fruit_distribution_no_digit_tokens():
    """Covers the isdigit() False branch for every token (line 5 False path)."""
    assert fruit_distribution("apples oranges bananas", 10) == 10


def test_fruit_distribution_empty_string():
    """Covers split(' ') yielding a single non-digit empty token."""
    assert fruit_distribution("", 7) == 7


def test_fruit_distribution_all_digit_tokens():
    """Covers the isdigit() True branch for every token."""
    assert fruit_distribution("3 4", 12) == 5
    assert fruit_distribution("1 2 3 4 5", 15) == 0
