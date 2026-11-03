# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

import pytest

from f123 import get_odd_collatz


def test_even_starting_n():
    """Covers lines 3-4 (even branch), 7-9 (even step in loop),
    11 (odd step in loop), 13-14 (append of odd values) and 16 (return).

    Collatz sequence for 6: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    Odd values encountered: 3, 5, 1
    """
    assert get_odd_collatz(6) == [1, 3, 5]


def test_odd_starting_n():
    """Covers line 6 (odd branch initializing odd_collatz with [n]).

    Collatz sequence for 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1
    Odd values encountered: 5, 1
    """
    assert get_odd_collatz(5) == [1, 5]


def test_n_equals_one_skips_loop():
    """Covers the False branch of the while condition on line 7 (loop body
    never runs for n == 1)."""
    assert get_odd_collatz(1) == [1]


def test_even_n_reaching_one_immediately():
    """Covers the even branch (lines 3-4) with a minimal sequence:
    2 -> 1, appending only 1."""
    assert get_odd_collatz(2) == [1]


def test_result_is_sorted_and_contains_only_odds():
    """Postcondition checks: output is sorted and contains only odd ints."""
    for n in range(1, 30):
        result = get_odd_collatz(n)
        assert result == sorted(result)
        assert all(isinstance(x, int) and x % 2 == 1 for x in result)
        assert result[0] == 1  # every Collatz sequence ends at 1
