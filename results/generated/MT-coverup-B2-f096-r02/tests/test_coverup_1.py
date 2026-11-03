# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import pytest

from f096 import count_up_to


def test_count_up_to_basic_covers_all_lines():
    """Exercises every line: prime appends, composite detection with break."""
    assert count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_empty_range():
    """n <= 2: outer loop body never executes."""
    assert count_up_to(2) == []
    assert count_up_to(0) == []
    assert count_up_to(-3) == []


def test_count_up_to_inner_loop_skipped():
    """n = 3: for i=2 the inner range(2, 2) is empty, is_prime stays True."""
    assert count_up_to(3) == [2]


def test_count_up_to_composite_branch():
    """Ensures i % j == 0 branch, is_prime = False, and break all execute."""
    assert count_up_to(5) == [2, 3]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_count_up_to_upper_bound_exclusive():
    """n itself is excluded even when prime; both branches of 'if is_prime' hit."""
    assert count_up_to(7) == [2, 3, 5]
    assert count_up_to(8) == [2, 3, 5, 7]


def test_count_up_to_returns_new_list_each_call():
    """Verifies no shared state leaks between calls (function is pure)."""
    first = count_up_to(6)
    second = count_up_to(6)
    assert first == [2, 3, 5]
    assert second == [2, 3, 5]
    assert first is not second
