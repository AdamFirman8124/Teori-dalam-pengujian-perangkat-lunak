# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f116 import sort_array


def test_sort_array_executes_return_line():
    arr = [5, 2, 3, 1, 4]
    result = sort_array(arr)
    # Postcondition: result is sorted primarily by number of set bits in
    # binary representation, secondarily by numeric value.
    expected = sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
    assert result == expected
    assert result == [1, 2, 4, 3, 5]
    # Original list must not be mutated.
    assert arr == [5, 2, 3, 1, 4]


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_single_element():
    assert sort_array([7]) == [7]


def test_sort_array_tie_broken_by_value():
    # 2 (0b10) and 4 (0b100) both have one set bit; numeric order breaks the tie.
    result = sort_array([4, 2])
    assert result == [2, 4]
