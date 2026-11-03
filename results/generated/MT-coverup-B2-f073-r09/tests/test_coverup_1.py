# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_smallest_change_empty():
    """Covers lines 3, 4 (loop body skipped), and 7."""
    assert smallest_change([]) == 0


def test_smallest_change_single_element():
    """Covers lines 3, 4 (loop body skipped), and 7."""
    assert smallest_change([42]) == 0


def test_smallest_change_palindrome():
    """Covers lines 3-5 and 7; line 5 takes the False branch, line 6 skipped."""
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 2, 1]) == 0


def test_smallest_change_non_palindrome():
    """Covers lines 3-7; line 5 takes the True branch, line 6 executes."""
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4


def test_smallest_change_odd_length_partial_mismatch():
    """Mixed branches: some pairs match (False), some differ (True)."""
    assert smallest_change([1, 2, 3, 2, 5]) == 1
    assert smallest_change([1, 2, 3, 4, 5]) == 2


def test_smallest_change_two_elements():
    """Minimal loop: single iteration covering both branches across calls."""
    assert smallest_change([1, 1]) == 0
    assert smallest_change([1, 2]) == 1
