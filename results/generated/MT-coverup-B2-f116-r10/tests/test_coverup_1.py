# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f116 import sort_array


def test_sort_array_basic():
    """1 has one '1' bit, 2 has one, 4 has one, 3 has two, 5 has two."""
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_single_element():
    assert sort_array([7]) == [7]


def test_sort_array_negatives():
    """bin(-n)[2:] still counts the '1' bits of the magnitude."""
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]


def test_sort_array_duplicates_and_stability():
    """Equal key counts keep the order from the initial sorted() pass."""
    assert sort_array([2, 4, 1, 3, 2]) == [1, 2, 2, 4, 3]


def test_sort_array_does_not_mutate_input():
    original = [3, 1, 2]
    result = sort_array(original)
    assert original == [3, 1, 2]
    assert result == [1, 2, 3]


def test_sort_array_result_is_sorted_by_bit_count():
    result = sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    counts = [bin(x)[2:].count('1') for x in result]
    assert counts == sorted(counts)
    assert sorted(result) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
