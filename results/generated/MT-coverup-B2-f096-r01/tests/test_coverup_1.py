# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import pytest

from f096 import count_up_to


def test_count_up_to_no_candidates():
    """Covers lines 3, 4 and 12: the list is created, the outer loop body
    never runs (n <= 2), and the empty list is returned."""
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(2) == []


def test_count_up_to_first_prime_only():
    """Covers lines 5, 10 and 11: is_prime is set, stays True, and the
    prime is appended; the inner loop (line 6) never runs for i == 2."""
    assert count_up_to(3) == [2]


def test_count_up_to_prime_with_inner_loop():
    """Covers lines 6 and 7 (False branch): for i == 3 the inner loop runs
    but no divisor is found, so the prime is still appended."""
    assert count_up_to(5) == [2, 3]


def test_count_up_to_composite_break():
    """Covers lines 7 (True branch), 8, 9 and 10 (False branch): for i == 4
    a divisor is found, is_prime is set to False, the loop breaks, and the
    composite is not appended."""
    assert count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_larger_range():
    """Full correctness check over a larger range; exercises every line and
    both branches of the divisibility test repeatedly."""
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
