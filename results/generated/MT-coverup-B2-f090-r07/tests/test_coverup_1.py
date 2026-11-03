# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest():
    """Covers line 3 (sorted(set(...))) and the lst[1] branch of line 4."""
    assert next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_with_duplicates():
    """Duplicates are removed by set(); second smallest of uniques is returned."""
    assert next_smallest([5, 1, 4, 3, 2, 5, 1]) == 2


def test_next_smallest_with_negatives():
    """Works with negative numbers; unsorted input is sorted first."""
    assert next_smallest([-1, -5, 0, 3]) == -1


def test_next_smallest_empty_list():
    """Covers the None branch of line 4 (len < 2) for an empty list."""
    assert next_smallest([]) is None


def test_next_smallest_single_element():
    """Covers the None branch of line 4 for a single-element list."""
    assert next_smallest([42]) is None


def test_next_smallest_all_duplicates():
    """A list whose unique values are fewer than 2 yields None."""
    assert next_smallest([7, 7, 7, 7]) is None
