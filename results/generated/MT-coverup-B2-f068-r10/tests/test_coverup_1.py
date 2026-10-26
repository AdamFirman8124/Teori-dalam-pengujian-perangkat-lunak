# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_returns_empty_list_for_empty_input():
    arr = []

    result = pluck(arr)

    assert result == []
    assert arr == []


def test_pluck_returns_empty_list_when_input_has_no_even_numbers():
    arr = [1, 3, 5, 7]

    result = pluck(arr)

    assert result == []
    assert arr == [1, 3, 5, 7]


def test_pluck_returns_smallest_even_number_and_its_index():
    arr = [9, 6, 4, 8, 2, 7]

    result = pluck(arr)

    assert result == [2, 4]
    assert arr == [9, 6, 4, 8, 2, 7]
