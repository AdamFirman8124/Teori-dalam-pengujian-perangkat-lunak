# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest():
    # Covers line 3 (sorted(set(...))) and the len >= 2 branch of line 4
    assert next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_unsorted_input():
    # Ensures sorting happens before indexing
    assert next_smallest([5, 1, 4, 3, 2]) == 2


def test_next_smallest_deduplicates_before_sorting():
    # Duplicates collapse via set(); second smallest of unique values
    assert next_smallest([1, 1, 2, 2, 3]) == 2


def test_next_smallest_negative_numbers():
    assert next_smallest([-1, -5, 0, -5]) == -1


def test_next_smallest_empty_list_returns_none():
    # Covers the len(lst) < 2 branch of line 4
    assert next_smallest([]) is None


def test_next_smallest_single_element_returns_none():
    assert next_smallest([7]) is None


def test_next_smallest_all_duplicates_returns_none():
    # set() collapses to a single element, so len < 2
    assert next_smallest([2, 2, 2]) is None
