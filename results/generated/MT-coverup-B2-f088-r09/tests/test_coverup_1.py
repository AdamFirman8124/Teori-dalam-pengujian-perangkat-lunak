# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_returns_empty_list_for_empty_input():
    assert sort_array([]) == []


def test_sort_array_sorts_descending_when_endpoints_sum_to_even():
    values = [2, 3, 4]
    original = values.copy()

    assert sort_array(values) == [4, 3, 2]
    assert values == original


def test_sort_array_sorts_ascending_when_endpoints_sum_to_odd():
    values = [1, 3, 2]
    original = values.copy()

    assert sort_array(values) == [1, 2, 3]
    assert values == original
