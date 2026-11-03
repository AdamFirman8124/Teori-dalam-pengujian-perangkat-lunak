# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

"""Tests for f067.fruit_distribution.

The function under test is pure (no I/O, no module state, no side effects),
so no monkeypatching or teardown is required to avoid state pollution.
Each test exercises specific lines/branches of the function body:

    lis = list()                      # line 3
    for i in s.split(' '):            # line 4 (loop taken)
        if i.isdigit():               # line 5 (True and False branches)
            lis.append(int(i))        # line 6
    return n - sum(lis)               # line 7
"""

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_typical_mixed_tokens():
    """Mixed words and numbers: loop runs, both if-branches are taken."""
    # "5" and "6" are digits (True branch, line 6); words take the False branch.
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digit_tokens():
    """No digit tokens at all: only the False branch of the if is taken,
    sum() over the empty list is 0, so the result equals n."""
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_multi_digit_numbers():
    """Multi-digit tokens are converted with int() (line 6)."""
    assert fruit_distribution("100 apples and 200 oranges", 350) == 50


def test_fruit_distribution_zero_counts_are_digits():
    """'0'.isdigit() is True, so zero counts are summed."""
    assert fruit_distribution("0 apples and 0 oranges", 7) == 7


def test_fruit_distribution_negative_looking_token_ignored():
    """'-5'.isdigit() is False, so a negative-looking token is skipped."""
    assert fruit_distribution("-5 apples", 5) == 5


def test_fruit_distribution_empty_string():
    """''.split(' ') yields [''], which is not a digit -> returns n."""
    assert fruit_distribution("", 42) == 42


def test_fruit_distribution_all_digit_tokens():
    """Every token is a digit: the True branch is taken on every iteration."""
    assert fruit_distribution("1 2 3", 10) == 4


def test_fruit_distribution_result_is_non_negative_when_counts_match():
    """When the described counts add up to n, zero mangoes remain."""
    assert fruit_distribution("3 apples and 2 oranges", 5) == 0
