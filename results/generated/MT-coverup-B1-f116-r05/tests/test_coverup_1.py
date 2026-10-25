# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f116 import sort_array


def test_sort_array_sorts_by_binary_ones_count():
    arr = [1, 5, 2, 3, 4]
    result = sort_array(arr)
    # 1 -> 0b1 (one 1), 2 -> 0b10 (one 1), 3 -> 0b11 (two 1s),
    # 4 -> 0b100 (one 1), 5 -> 0b101 (two 1s)
    # Ties broken by numeric order: [1, 2, 4, 3, 5]
    assert result == [1, 2, 4, 3, 5]
    # Input list must not be mutated
    assert arr == [1, 5, 2, 3, 4]


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_single_element():
    assert sort_array([7]) == [7]
