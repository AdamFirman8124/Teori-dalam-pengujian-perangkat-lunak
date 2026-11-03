# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_returns_false_when_object_too_heavy():
    """Covers lines 3-4: sum(q) > w triggers the early False return."""
    # sum([3, 2, 3]) == 8 > 1
    assert will_it_fly([3, 2, 3], 1) is False


def test_returns_false_when_not_palindromic():
    """Covers lines 6-9: loop entered, elements mismatch -> False."""
    # sum([1, 2]) == 3 <= 100, but q[0] != q[1]
    assert will_it_fly([1, 2], 100) is False


def test_returns_true_for_palindromic_object_within_weight():
    """Covers lines 6-7, 10-12: multiple loop iterations then True."""
    # sum([1, 2, 3, 2, 1]) == 9 <= 9 (boundary), palindrome -> True
    assert will_it_fly([1, 2, 3, 2, 1], 9) is True


def test_single_element_skips_loop_but_returns_true():
    """Covers line 12 via the i == j path (loop body never runs)."""
    assert will_it_fly([5], 5) is True


def test_empty_list_is_balanced_and_within_weight():
    """Covers line 12 via the empty-list path (i=0, j=-1, loop skipped)."""
    assert will_it_fly([], 0) is True
