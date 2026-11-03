# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest

from f110 import exchange


def test_exchange_yes_when_even_count_geq_odd_count():
    """Covers lines 3-12: both loops, both if-branches taken, and 'YES' return."""
    # lst1 has 2 odd numbers (odd=2), lst2 has 2 even numbers (even=2)
    # even (2) >= odd (2) -> "YES"
    assert exchange([1, 3], [2, 4]) == "YES"


def test_exchange_no_when_even_count_lt_odd_count():
    """Covers line 13: the 'NO' return path."""
    # lst1 has 2 odd numbers (odd=2), lst2 has 1 even number (even=1)
    # even (1) < odd (2) -> "NO"
    assert exchange([1, 3], [2]) == "NO"


def test_exchange_empty_lists_returns_yes():
    """Covers loop bodies never executing (empty iterables) and 'YES' path (0 >= 0)."""
    assert exchange([], []) == "YES"


def test_exchange_conditions_false_in_both_loops():
    """Covers lines 6 and 9 evaluating to False (no odd in lst1, no even in lst2)."""
    # lst1 all even (odd stays 0), lst2 all odd (even stays 0) -> 0 >= 0 -> "YES"
    assert exchange([2, 4], [1, 3]) == "YES"


def test_exchange_negative_and_zero_values():
    """Covers negative numbers and zero exercising both parity branches."""
    # lst1: -1 is odd (odd=1), -2 is even; lst2: 0 is even (even=1), -3 is odd
    # even (1) >= odd (1) -> "YES"
    assert exchange([-1, -2], [0, -3]) == "YES"
    # lst1: -1 and -3 are odd (odd=2); lst2: 0 is even (even=1)
    # even (1) < odd (2) -> "NO"
    assert exchange([-1, -3], [0]) == "NO"


def test_exchange_is_pure_no_state_pollution():
    """Verifies the function has no side effects on its inputs (no cleanup needed)."""
    lst1 = [1, 2]
    lst2 = [3, 4]
    result = exchange(lst1, lst2)
    # lst1 has one odd number (1) -> odd=1
    # lst2 has one even number (4) -> even=1
    # even (1) >= odd (1) -> "YES"
    assert result == "YES"
    # Inputs are unmodified, so no state pollution occurs
    assert lst1 == [1, 2]
    assert lst2 == [3, 4]
