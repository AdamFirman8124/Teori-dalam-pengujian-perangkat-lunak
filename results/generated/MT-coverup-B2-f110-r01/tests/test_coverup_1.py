# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_returns_yes_when_even_count_at_least_odd_count():
    """Covers lines 3-12: counting odds in lst1 (both branches of i%2==1),
    counting evens in lst2 (both branches of i%2==0), and the 'YES' return."""
    # lst1 = [1, 2]: 1 is odd (odd=1), 2 is even (branch false)
    # lst2 = [2, 3]: 2 is even (even=1), 3 is odd (branch false)
    # odd=1, even=1 -> even >= odd -> "YES"
    assert exchange([1, 2], [2, 3]) == "YES"


def test_exchange_returns_no_when_even_count_less_than_odd_count():
    """Covers line 13: the 'NO' return when even < odd."""
    # lst1 = [1, 3]: both odd -> odd=2
    # lst2 = [3, 5]: both odd -> even=0
    # even=0 < odd=2 -> "NO"
    assert exchange([1, 3], [3, 5]) == "NO"


def test_exchange_empty_lists_returns_yes():
    """Covers loops with empty iterables: odd=0, even=0 -> even >= odd -> 'YES'."""
    assert exchange([], []) == "YES"


def test_exchange_all_even_lst1_all_odd_lst2_returns_yes():
    """Covers the case where neither counter is incremented:
    lst1 all even (odd stays 0), lst2 all odd (even stays 0) -> 'YES'."""
    assert exchange([2, 4, 6], [1, 3, 5]) == "YES"


def test_exchange_tie_returns_yes():
    """Boundary case: even == odd exactly -> 'YES' (>= comparison)."""
    # lst1 = [1, 3, 5]: odd=3; lst2 = [2, 4, 6]: even=3 -> tie -> "YES"
    assert exchange([1, 3, 5], [2, 4, 6]) == "YES"


def test_exchange_negative_numbers():
    """Negative integers: Python's % keeps sign, so -3 % 2 == 1 (odd) and
    -4 % 2 == 0 (even). Verifies counting works for negatives too."""
    # lst1 = [-3, -4]: -3 is odd (odd=1), -4 is even
    # lst2 = [-4, -3]: -4 is even (even=1), -3 is odd
    # even=1 >= odd=1 -> "YES"
    assert exchange([-3, -4], [-4, -3]) == "YES"
