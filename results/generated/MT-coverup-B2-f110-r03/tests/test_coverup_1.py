# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_returns_yes_when_even_count_at_least_odd_count():
    """Covers lines 3-12: both loops, both if-branches taken, and the 'YES' return.

    lst1 = [1, 2] -> one odd (1), one even (2, skipped by the odd check)
    lst2 = [2, 3] -> one even (2), one odd (3, skipped by the even check)
    even (1) >= odd (1) -> "YES"
    """
    assert exchange([1, 2], [2, 3]) == "YES"


def test_exchange_returns_no_when_even_count_less_than_odd_count():
    """Covers line 13: the 'NO' return path.

    lst1 = [1, 3] -> odd = 2
    lst2 = [1]    -> even = 0 (1 is odd, so the even-branch is not taken)
    even (0) < odd (2) -> "NO"
    """
    assert exchange([1, 3], [1]) == "NO"


def test_exchange_empty_lists_returns_yes():
    """Covers the loops with empty iterables (zero iterations) and 0 >= 0 -> 'YES'."""
    assert exchange([], []) == "YES"


def test_exchange_negative_numbers_branches():
    """Covers both branches of both conditionals using negative integers.

    In Python, -3 % 2 == 1 (odd) and -2 % 2 == 0 (even).
    """
    # odd = 1 (from -3), even = 1 (from -2): 1 >= 1 -> "YES"
    assert exchange([-3, -2], [-2]) == "YES"
    # odd = 2 (from -3, -1), even = 1 (from -2): 1 < 2 -> "NO"
    assert exchange([-3, -1], [-2]) == "NO"
