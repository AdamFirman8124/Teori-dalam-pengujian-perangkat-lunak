# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_empty_returns_empty_list():
    result = sort_array([])
    assert result == []


def test_sort_array_odd_sum_sorts_ascending():
    # first + last = 1 + 4 = 5 (odd) -> reverse=False -> ascending
    data = [1, 3, 2, 4]
    result = sort_array(data)
    assert result == [1, 2, 3, 4]
    assert data == [1, 3, 2, 4]


def test_sort_array_even_sum_sorts_descending():
    # first + last = 4 + 2 = 6 (even) -> reverse=True -> descending
    data = [4, 1, 3, 2]
    result = sort_array(data)
    assert result == [4, 3, 2, 1]
    assert data == [4, 1, 3, 2]


def test_sort_array_single_element():
    # first + last = 5 + 5 = 10 (even) -> reverse=True, unchanged
    assert sort_array([5]) == [5]
