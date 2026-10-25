# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_returns_empty_list_for_empty_input():
    assert sort_array([]) == []


def test_sort_array_sorts_ascending_when_endpoint_sum_is_odd():
    values = [3, 1, 2]
    assert sort_array(values) == [1, 2, 3]


def test_sort_array_sorts_descending_when_endpoint_sum_is_even():
    values = [1, 2, 3]
    assert sort_array(values) == [3, 2, 1]
