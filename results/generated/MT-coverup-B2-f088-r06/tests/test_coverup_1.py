# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_empty():
    array = []
    assert sort_array(array) == []
    assert array == []


def test_sort_array_ascending_when_endpoint_sum_is_odd():
    array = [3, 1, 4, 2]
    assert sort_array(array) == [1, 2, 3, 4]
    assert array == [3, 1, 4, 2]


def test_sort_array_descending_when_endpoint_sum_is_even():
    array = [1, 3, 2, 1]
    assert sort_array(array) == [3, 2, 1, 1]
    assert array == [1, 3, 2, 1]
