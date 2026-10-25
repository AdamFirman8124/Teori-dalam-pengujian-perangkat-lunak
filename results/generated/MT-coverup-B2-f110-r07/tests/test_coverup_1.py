# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_yes_when_even_geq_odd():
    # lst1 has 2 odds, lst2 has 2 evens -> even >= odd -> "YES"
    assert exchange([1, 3, 2], [2, 4, 5]) == "YES"


def test_exchange_no_when_even_lt_odd():
    # lst1 has 3 odds, lst2 has 1 even -> even < odd -> "NO"
    assert exchange([1, 3, 5], [2, 7]) == "NO"


def test_exchange_equal_counts_returns_yes():
    # odd == even -> branch even >= odd still taken via equality
    assert exchange([1, 3], [2, 4]) == "YES"


def test_exchange_empty_lists():
    # odd = 0, even = 0 -> even >= odd -> "YES"
    assert exchange([], []) == "YES"


def test_exchange_no_odds_no_evens():
    # all evens in lst1 (odd stays 0), all odds in lst2 (even stays 0)
    assert exchange([2, 4], [1, 3]) == "YES"


def test_exchange_negative_numbers():
    # -3 % 2 == 1 in Python, so negatives count as odd correctly
    assert exchange([-3, -1], [-2, -4]) == "YES"
    assert exchange([-3, -1, -5], [-1]) == "NO"
