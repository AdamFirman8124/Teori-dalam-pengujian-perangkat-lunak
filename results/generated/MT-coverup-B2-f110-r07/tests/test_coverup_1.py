# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_returns_yes_when_even_count_geq_odd_count():
    # lst1: 1, 3 are odd -> odd = 2; 2, 4 are even (skip)
    # lst2: 2, 4 are even -> even = 2; 1, 3 are odd (skip)
    # even (2) >= odd (2) -> "YES"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"


def test_exchange_returns_no_when_even_count_lt_odd_count():
    # lst1: 1, 3 are odd -> odd = 2; 2 is even (skip)
    # lst2: 4 is even -> even = 1; 1, 5, 3 are odd (skip)
    # even (1) < odd (2) -> "NO"
    assert exchange([1, 2, 3], [1, 5, 3, 4]) == "NO"


def test_exchange_empty_lists_returns_yes():
    # No iterations at all: odd = 0, even = 0 -> even >= odd -> "YES"
    assert exchange([], []) == "YES"


def test_exchange_all_even_lst1_all_odd_lst2_returns_no():
    # lst1: no odds -> odd = 0; lst2: no evens -> even = 0
    # even (0) >= odd (0) -> "YES" (boundary of the >= branch)
    assert exchange([2, 4], [1, 3]) == "YES"
