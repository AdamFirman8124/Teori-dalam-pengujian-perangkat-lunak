# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f088


def test_sort_array_returns_empty_list_for_empty_input():
    assert f088.sort_array([]) == []


def test_sort_array_sorts_ascending_when_endpoint_sum_is_odd():
    values = [3, 1, 2]

    result = f088.sort_array(values)

    assert result == [1, 2, 3]
    assert values == [3, 1, 2]


def test_sort_array_sorts_descending_when_endpoint_sum_is_even():
    values = [1, 4, 3]

    result = f088.sort_array(values)

    assert result == [4, 3, 1]
    assert values == [1, 4, 3]
