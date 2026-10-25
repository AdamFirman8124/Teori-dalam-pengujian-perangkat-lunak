# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_returns_empty_list_for_empty_input():
    assert sort_array([]) == []


def test_sort_array_sorts_descending_when_first_and_last_sum_is_even():
    values = [3, 1, 4, 1]

    result = sort_array(values)

    assert result == [4, 3, 1, 1]
    assert values == [3, 1, 4, 1]


def test_sort_array_sorts_ascending_when_first_and_last_sum_is_odd():
    values = [4, 1, 3, 1]

    result = sort_array(values)

    assert result == [1, 1, 3, 4]
    assert values == [4, 1, 3, 1]
