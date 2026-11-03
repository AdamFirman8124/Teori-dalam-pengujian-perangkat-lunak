# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_yes_when_even_count_matches_odd_count():
    """lst1 has odd numbers (odd branch taken), lst2 has enough evens -> 'YES'."""
    result = exchange([1, 3, 5], [2, 4, 6])
    assert result == "YES"


def test_exchange_no_when_odd_count_exceeds_even_count():
    """More odds in lst1 than evens in lst2 -> 'NO'."""
    result = exchange([1, 3, 5], [2])
    assert result == "NO"


def test_exchange_yes_with_even_numbers_in_lst1():
    """Even numbers in lst1 skip the odd-count branch (branch not taken)."""
    result = exchange([2, 4], [2])
    assert result == "YES"


def test_exchange_no_with_odd_numbers_in_lst2():
    """Odd numbers in lst2 skip the even-count branch (branch not taken)."""
    result = exchange([1], [3])
    assert result == "NO"


def test_exchange_empty_lists_returns_yes():
    """Both lists empty: counts are zero, 0 >= 0 -> 'YES'."""
    result = exchange([], [])
    assert result == "YES"


def test_exchange_does_not_mutate_inputs():
    """The function must not modify its arguments (no state pollution)."""
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    exchange(lst1, lst2)
    assert lst1 == [1, 2, 3]
    assert lst2 == [4, 5, 6]


def test_exchange_boundary_equal_counts():
    """Boundary case: even count exactly equals odd count -> 'YES' (>= branch)."""
    result = exchange([1, 3], [2, 4])
    assert result == "YES"
