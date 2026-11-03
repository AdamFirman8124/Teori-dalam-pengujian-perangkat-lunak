# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_sorted_list_returns_true():
    """Covers lines 3-5 (counting) and lines 8-9 (all(...) True -> return True)."""
    assert is_sorted([1, 2, 3, 4]) is True


def test_is_sorted_empty_list_returns_true():
    """Covers lines 3-5 with an empty list; any() and all() are vacuously satisfied."""
    assert is_sorted([]) is True


def test_is_sorted_duplicates_within_limit_returns_true():
    """Elements appearing exactly twice are allowed; covers lines 3-9."""
    assert is_sorted([1, 1, 2, 2, 3]) is True


def test_is_sorted_unsorted_list_returns_false():
    """Covers lines 3-6 and line 11 (all(...) False -> else -> return False)."""
    assert is_sorted([1, 3, 2]) is False


def test_is_sorted_too_many_duplicates_returns_false():
    """Covers lines 3-7 (any(...) True -> return False), even though list is sorted."""
    assert is_sorted([1, 1, 1, 2]) is False


def test_is_sorted_unsorted_and_too_many_duplicates_returns_false():
    """Covers lines 3-7: any(...) short-circuits before the sortedness check."""
    assert is_sorted([2, 2, 2, 1]) is False


def test_is_sorted_single_element_returns_true():
    """Single element: counting executes, both any() and all() vacuously pass."""
    assert is_sorted([42]) is True
