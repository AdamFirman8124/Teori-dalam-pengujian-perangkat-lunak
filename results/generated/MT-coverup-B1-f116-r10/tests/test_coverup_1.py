# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_empty_executes_line_and_returns_empty():
    arr = []
    result = sort_array(arr)
    assert result == []
    assert result is not arr
    assert arr == []


def test_sort_array_single_element_executes_lambda():
    arr = [7]
    result = sort_array(arr)
    assert result == [7]
    assert arr == [7]


def test_sort_array_sorts_by_popcount_then_value():
    arr = [1, 5, 2, 3, 4]
    result = sort_array(arr)
    assert result == [1, 2, 4, 3, 5]
    assert arr == [1, 5, 2, 3, 4]


def test_sort_array_with_zero_and_duplicates():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    assert sort_array([3, 3, 1]) == [1, 3, 3]
    assert sort_array([0, 0]) == [0, 0]


def test_sort_array_postconditions_on_varied_input():
    arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result = sort_array(arr)
    assert result == [0, 1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 7, 11, 13, 14, 15]
    assert sorted(result) == sorted(arr)
    assert all(
        (bin(a)[2:].count("1"), a) <= (bin(b)[2:].count("1"), b) or bin(a)[2:].count("1") < bin(b)[2:].count("1")
        for a, b in zip(result, result[1:])
    )
    keys = [(bin(x)[2:].count("1"), x) for x in result]
    assert keys == sorted(keys)
    assert arr == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
