# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_returns_true_for_sorted_list_within_duplicate_limit():
    """A sorted list where no element occurs more than twice -> True.

    Covers lines 3-5 (counting loop), line 6, line 8, and line 9 (return True).
    """
    assert is_sorted([1, 2, 2, 3, 4]) is True
    # Edge case: empty list is trivially sorted, all() over empty range is True.
    assert is_sorted([]) is True


def test_is_sorted_returns_false_when_element_occurs_more_than_twice():
    """An element occurring 3+ times forces an early False return.

    Covers line 7 (return False from the any() guard).
    """
    assert is_sorted([1, 1, 1, 2]) is False
    # Even a sorted list must fail if a value appears 3 times.
    assert is_sorted([1, 2, 2, 2, 3]) is False


def test_is_sorted_returns_false_for_unsorted_list_within_duplicate_limit():
    """An unsorted list (with all counts <= 2) reaches the else branch.

    Covers line 8 (all() evaluating to False) and line 11 (return False).
    """
    assert is_sorted([2, 1]) is False
    assert is_sorted([1, 3, 2, 4]) is False
    # Equal adjacent elements are allowed (non-strictly sorted), so use a real drop.
    assert is_sorted([1, 2, 2, 1]) is False
