# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_ascending_odd_sum():
    # first + last = 3 + 2 = 5 (odd) -> reverse=False -> ascending
    assert sort_array([3, 1, 2]) == [1, 2, 3]


def test_sort_array_descending_even_sum():
    # first + last = 4 + 2 = 6 (even) -> reverse=True -> descending
    assert sort_array([4, 1, 3, 2]) == [4, 3, 2, 1]


def test_sort_array_single_element():
    # first + last = 5 + 5 = 10 (even) -> reverse=True, single element unchanged
    assert sort_array([5]) == [5]
