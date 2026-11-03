# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

"""Tests for f126.is_sorted covering all lines and branches (lines 3-11)."""

from f126 import is_sorted


def test_is_sorted_sorted_list_returns_true():
    """Lines 3-5 (counting) and 8-9 (all() branch True)."""
    assert is_sorted([1, 2, 2, 3]) is True


def test_is_sorted_strictly_increasing_returns_true():
    """Lines 3-5 and 8-9 with no duplicates at all."""
    assert is_sorted([1, 2, 3, 4, 5]) is True


def test_is_sorted_exactly_two_duplicates_allowed():
    """Boundary of line 6: count == 2 must NOT trigger the False branch."""
    assert is_sorted([1, 1, 2, 3]) is True


def test_is_sorted_three_duplicates_returns_false():
    """Lines 6-7: any(count_digit[i] > 2) branch taken -> False."""
    assert is_sorted([1, 2, 2, 2, 3]) is False


def test_is_sorted_unsorted_returns_false():
    """Line 11: all() branch False -> else branch returns False."""
    assert is_sorted([2, 1]) is False


def test_is_sorted_unsorted_with_duplicates_returns_false():
    """Exercises both the counting loop and the else branch (line 11)."""
    assert is_sorted([1, 3, 2, 2]) is False


def test_is_sorted_empty_list_returns_true():
    """Lines 3-5 with empty iterable; all() over empty range is True (line 9)."""
    assert is_sorted([]) is True


def test_is_sorted_single_element_returns_true():
    """Single element: counting loop runs once, all() over empty range True."""
    assert is_sorted([7]) is True


def test_is_sorted_descending_duplicates_returns_false():
    """Duplicates counted (lines 4-5) but unsorted -> line 11 False."""
    assert is_sorted([5, 5, 4, 4]) is False


def test_is_sorted_non_adjacent_triple_returns_false():
    """Three occurrences of a value, non-adjacent, still exceeds the limit."""
    assert is_sorted([1, 2, 1, 3, 1]) is False
