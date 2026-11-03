# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


def test_sort_third_sorts_every_third_element():
    result = sort_third([5, 6, 3, 4, 8, 9, 1])
    # Elements at indices 0, 3, 6 are [5, 4, 1] -> sorted [1, 4, 5]
    assert result == [1, 6, 3, 4, 8, 9, 5]


def test_sort_third_longer_list():
    result = sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1])
    # Elements at indices 0, 3, 6 are [9, 6, 3] -> sorted [3, 6, 9]
    assert result == [3, 8, 7, 6, 5, 4, 9, 2, 1]


def test_sort_third_with_duplicates():
    result = sort_third([5, 6, 3, 4, 8, 9, 2, 2])
    # Elements at indices 0, 3, 6 are [5, 4, 2] -> sorted [2, 4, 5]
    assert result == [2, 6, 3, 4, 8, 9, 5, 2]


def test_sort_third_already_sorted_thirds():
    result = sort_third([1, 2, 3])
    assert result == [1, 2, 3]


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_single_element():
    assert sort_third([42]) == [42]


def test_sort_third_does_not_mutate_input():
    original = [5, 6, 3, 4, 8, 9, 1]
    snapshot = list(original)
    result = sort_third(original)
    # The input list must remain unchanged (function works on a copy)
    assert original == snapshot
    # The returned list must be a new object, not the same one
    assert result is not original
