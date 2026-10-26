# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_returns_yes_when_enough_evens():
    lst1 = [1, 3]
    lst2 = [2, 4]
    result = exchange(lst1, lst2)
    assert result == "YES"
    # postconditions: inputs untouched, result is one of the two allowed values
    assert lst1 == [1, 3]
    assert lst2 == [2, 4]
    assert result in ("YES", "NO")


def test_exchange_returns_no_when_not_enough_evens():
    lst1 = [1, 3, 5]
    lst2 = [2]
    result = exchange(lst1, lst2)
    assert result == "NO"
    assert lst1 == [1, 3, 5]
    assert lst2 == [2]
    assert result in ("YES", "NO")


def test_exchange_with_no_odds_in_lst1_and_no_evens_in_lst2():
    # covers the "even element in lst1" and "odd element in lst2" branches
    lst1 = [2, 4]
    lst2 = [1, 3]
    result = exchange(lst1, lst2)
    assert result == "YES"
    assert lst1 == [2, 4]
    assert lst2 == [1, 3]


def test_exchange_with_empty_lists():
    assert exchange([], []) == "YES"


def test_exchange_boundary_equal_counts():
    # odd == even exactly -> "YES" (>= branch)
    assert exchange([1], [2]) == "YES"
    # odd == even + 1 -> "NO"
    assert exchange([1, 3], [2]) == "NO"
