# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_basic():
    """Covers line 3 (sorted(set(...))) and the len >= 2 branch of line 4."""
    assert next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_unsorted_with_duplicates():
    """Deduplication and sorting: second-smallest among unsorted duplicates."""
    assert next_smallest([5, 1, 4, 3, 2, 1, 2]) == 2


def test_next_smallest_two_elements():
    """Exactly two unique elements: returns the larger of the two."""
    assert next_smallest([3, 1]) == 3


def test_next_smallest_negative_numbers():
    """Works with negative values."""
    assert next_smallest([-1, -2, -3]) == -2


def test_next_smallest_empty_list_returns_none():
    """Covers the len < 2 branch of line 4 (empty list)."""
    assert next_smallest([]) is None


def test_next_smallest_single_element_returns_none():
    """Covers the len < 2 branch of line 4 (one element)."""
    assert next_smallest([42]) is None


def test_next_smallest_all_duplicates_returns_none():
    """set() collapses duplicates to a single element -> None."""
    assert next_smallest([7, 7, 7, 7]) is None


def test_next_smallest_does_not_mutate_input():
    """The function must not modify the caller's list (no state pollution)."""
    original = [3, 1, 2]
    snapshot = list(original)
    result = next_smallest(original)
    assert result == 2
    assert original == snapshot
