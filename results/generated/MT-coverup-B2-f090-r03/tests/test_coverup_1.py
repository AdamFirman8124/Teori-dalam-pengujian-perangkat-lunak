# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_basic():
    """Second smallest of a sorted list of distinct values."""
    assert next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_unsorted_input():
    """Input need not be sorted; result is second smallest unique value."""
    assert next_smallest([5, 3, 1, 4, 2]) == 2


def test_next_smallest_duplicates_removed():
    """Duplicates are removed before picking the second smallest."""
    assert next_smallest([2, 2, 1, 1, 3]) == 2
    assert next_smallest([7, 7, 7, 5, 7]) == 7


def test_next_smallest_negative_numbers():
    """Works with negative numbers."""
    assert next_smallest([-1, -5, -3, 0]) == -3


def test_next_smallest_empty_list_returns_none():
    """Empty list has no second smallest."""
    assert next_smallest([]) is None


def test_next_smallest_single_element_returns_none():
    """A single element has no second smallest."""
    assert next_smallest([42]) is None


def test_next_smallest_all_duplicates_returns_none():
    """A list whose unique set has fewer than 2 elements returns None."""
    assert next_smallest([3, 3, 3]) is None


def test_next_smallest_two_elements():
    """Boundary case: exactly two unique elements."""
    assert next_smallest([9, 4]) == 9


def test_next_smallest_does_not_mutate_input():
    """The original list must not be modified (sorted/set create new objects)."""
    original = [3, 1, 2]
    snapshot = list(original)
    next_smallest(original)
    assert original == snapshot
