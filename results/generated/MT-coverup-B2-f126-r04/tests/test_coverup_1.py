# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

"""Tests for f126.is_sorted, covering all lines and branches (lines 3-11)."""

from f126 import is_sorted


def test_is_sorted_true_when_sorted_and_no_more_than_two_duplicates():
    """A sorted list whose elements occur at most twice -> True.

    Exercises lines 3-5 (counting), line 6 (any(...) is False), and
    lines 8-9 (all(...) is True -> return True).
    """
    assert is_sorted([1, 2, 2, 3]) is True


def test_is_sorted_false_when_element_occurs_more_than_twice():
    """An element occurring more than twice -> False.

    Exercises lines 3-5 (counting) and lines 6-7 (any(...) is True ->
    return False), short-circuiting before the sortedness check.
    """
    assert is_sorted([1, 2, 2, 2, 3]) is False


def test_is_sorted_false_when_not_sorted():
    """A list with no element occurring more than twice but unsorted -> False.

    Exercises lines 3-5 (counting), line 6 (any(...) is False), and
    lines 10-11 (all(...) is False -> else branch -> return False).
    """
    assert is_sorted([1, 3, 2]) is False


def test_is_sorted_single_element():
    """A single-element list is trivially sorted with counts <= 2 -> True."""
    assert is_sorted([5]) is True
