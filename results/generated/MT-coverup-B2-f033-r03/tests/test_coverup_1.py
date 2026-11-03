# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


def test_sort_third_sorts_every_third_element():
    original = [5, 6, 3, 4, 1, 2, 9, 8, 7]
    result = sort_third(original)
    # Elements at indices 0, 3, 6 are [5, 4, 9]; sorted they become [4, 5, 9].
    # All other elements keep their original positions.
    assert result == [4, 6, 3, 5, 1, 2, 9, 8, 7]


def test_sort_third_does_not_mutate_input():
    original = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    snapshot = list(original)
    result = sort_third(original)
    # The input list must remain untouched because of the copy on line 3.
    assert original == snapshot
    # Indices 0, 3, 6 hold [9, 2, 6] -> sorted [2, 6, 9].
    assert result == [2, 1, 8, 6, 7, 3, 9, 4, 5]
    assert result is not original


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_single_element():
    assert sort_third([2]) == [2]


def test_sort_third_already_sorted_thirds():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = sort_third(original)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
