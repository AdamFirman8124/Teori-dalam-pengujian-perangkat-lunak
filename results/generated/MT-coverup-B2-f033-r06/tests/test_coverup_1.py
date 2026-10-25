# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


def test_sort_third_sorts_indices_0_3_6():
    result = sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sort_third_unsorted_thirds():
    result = sort_third([5, 6, 3, 4, 8, 9, 2])
    # positions 0, 3, 6 hold [5, 4, 2] -> sorted [2, 4, 5]
    assert result == [2, 6, 3, 4, 8, 9, 5]
    # other positions untouched
    assert result[1] == 6 and result[2] == 3 and result[4] == 8 and result[5] == 9


def test_sort_third_does_not_mutate_input():
    original = [3, 1, 2, 0]
    snapshot = list(original)
    result = sort_third(original)
    assert original == snapshot  # input list unchanged
    assert result == [0, 1, 2, 3]
    assert result is not original  # a new list is returned


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_single_element():
    assert sort_third([9]) == [9]
