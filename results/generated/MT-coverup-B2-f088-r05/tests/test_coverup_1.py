# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f088 import sort_array


def test_sort_array_returns_empty_list_for_empty_input():
    array = []

    result = sort_array(array)

    assert result == []
    assert array == []


def test_sort_array_sorts_descending_when_first_and_last_sum_is_even():
    array = [1, 4, 3]

    result = sort_array(array)

    assert result == [4, 3, 1]
    assert array == [1, 4, 3]


def test_sort_array_sorts_ascending_when_first_and_last_sum_is_odd():
    array = [3, 1, 2]

    result = sort_array(array)

    assert result == [1, 2, 3]
    assert array == [3, 1, 2]
