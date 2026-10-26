# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_ascending_when_endpoint_sum_is_odd():
    assert sort_array([2, 3, 1]) == [1, 2, 3]


def test_sort_array_descending_when_endpoint_sum_is_even():
    assert sort_array([3, 1, 5, 2, 7]) == [7, 5, 3, 2, 1]
