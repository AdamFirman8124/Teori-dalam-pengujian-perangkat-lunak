# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_yes_when_even_geq_odd():
    # lst1 has 2 odds, lst2 has 2 evens -> even >= odd -> "YES"
    assert exchange([1, 3], [2, 4]) == "YES"


def test_exchange_no_when_even_lt_odd():
    # lst1 has 3 odds, lst2 has 1 even -> even < odd -> "NO"
    assert exchange([1, 3, 5], [2]) == "NO"


def test_exchange_empty_lists():
    # Both loops execute zero times; even (0) >= odd (0) -> "YES"
    assert exchange([], []) == "YES"


def test_exchange_even_numbers_in_lst1():
    # lst1 contains evens (not counted as odd), lst2 has evens -> "YES"
    assert exchange([2, 4, 6], [2, 4]) == "YES"


def test_exchange_odd_numbers_in_lst2():
    # lst2 contains odds (not counted as even); odd count exceeds -> "NO"
    assert exchange([1], [1, 3]) == "NO"


def test_exchange_boundary_equal_counts():
    # odd == even -> "YES" (covers the >= branch boundary)
    assert exchange([1], [2]) == "YES"


def test_exchange_negative_numbers():
    # Negative odds/evens still classified correctly by i % 2
    assert exchange([-1, -3], [-2, -4]) == "YES"
    assert exchange([-1, -3, -5], [-2]) == "NO"
