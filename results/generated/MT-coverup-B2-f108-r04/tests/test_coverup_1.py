# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty_list():
    """Empty input: line 10 executes, digits_sum never called."""
    assert count_nums([]) == 0


def test_count_nums_all_positive():
    """Positive numbers exercise the 'n < 0' False branch of digits_sum."""
    assert count_nums([1, 1, 2]) == 3


def test_count_nums_mixed_signs():
    """Negative numbers exercise the 'n < 0' True branch (line 6).

    digits_sum(-1)  -> -1  (not counted)
    digits_sum(11)  ->  2  (counted)
    digits_sum(-11) ->  0  (not counted)
    """
    assert count_nums([-1, 11, -11]) == 1


def test_count_nums_zero_not_counted():
    """Zero has digit sum 0, which fails the 'x > 0' filter branch."""
    assert count_nums([0, 0, 0]) == 0


def test_count_nums_multi_digit_negative():
    """Negative multi-digit number: first digit negated, rest positive."""
    # digits_sum(-123) -> -1 + 2 + 3 = 4 (counted)
    # digits_sum(-12)  -> -1 + 2     = 1 (counted)
    # digits_sum(-10)  -> -1 + 0     = -1 (not counted)
    assert count_nums([-123, -12, -10]) == 2
