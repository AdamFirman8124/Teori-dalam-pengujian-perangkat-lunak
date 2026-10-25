# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_ascending_odd_sum():
    # (3 + 2) % 2 == 1 -> reverse=False -> ascending
    assert sort_array([3, 1, 2]) == [1, 2, 3]


def test_sort_array_descending_even_sum():
    # (1 + 3) % 2 == 0 -> reverse=True -> descending
    assert sort_array([1, 2, 3]) == [3, 2, 1]


def test_sort_array_single_element_even_sum():
    # (5 + 5) % 2 == 0 -> reverse=True, single element unchanged
    assert sort_array([5]) == [5]
