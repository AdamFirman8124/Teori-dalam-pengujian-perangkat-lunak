# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_array_returns_empty_list():
    # covers line 3 (len(arr) == 0 branch)
    result = pluck([])
    assert result == []
    assert isinstance(result, list)


def test_pluck_no_even_numbers_returns_empty_list():
    # covers line 4 (filter) and line 5 (evens == [] branch)
    result = pluck([1, 3, 5, 7])
    assert result == []
    assert isinstance(result, list)


def test_pluck_returns_smallest_even_and_its_index():
    # covers line 6 (return [min(evens), arr.index(...)])
    result = pluck([4, 2, 3])
    assert result == [2, 1]
    assert result[0] == min(x for x in [4, 2, 3] if x % 2 == 0)
    assert [4, 2, 3][result[1]] == result[0]


def test_pluck_duplicate_smallest_even_uses_first_index():
    # line 6 with duplicates: arr.index returns the FIRST occurrence
    arr = [6, 2, 2, 8]
    result = pluck(arr)
    assert result == [2, 1]
    assert arr[result[1]] == result[0]


def test_pluck_single_even_element():
    # line 6 with a one-element array
    result = pluck([10])
    assert result == [10, 0]


def test_pluck_negative_even_numbers():
    # line 6 with negatives: -4 is the smallest even
    arr = [-4, 3, -2, 7]
    result = pluck(arr)
    assert result == [-4, 0]
    assert arr[result[1]] == result[0]


def test_pluck_zero_is_even():
    # line 6: 0 is even and can be the minimum
    arr = [5, 0, 3]
    result = pluck(arr)
    assert result == [0, 1]


def test_pluck_does_not_mutate_input():
    # postcondition: input list unchanged
    arr = [3, 4, 5, 6]
    snapshot = list(arr)
    pluck(arr)
    assert arr == snapshot
