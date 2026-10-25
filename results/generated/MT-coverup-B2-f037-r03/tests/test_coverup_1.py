# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import f037


def test_sort_even_even_length_list():
    data = [5, 3, 2, 8, 1, 4]
    original = list(data)

    result = f037.sort_even(data)

    assert result == [1, 3, 2, 8, 5, 4]
    assert len(result) == len(data)
    assert data == original  # input must not be mutated


def test_sort_even_odd_length_list_appends_trailing_even():
    data = [5, 3, 2, 8, 1]
    original = list(data)

    result = f037.sort_even(data)

    assert result == [1, 3, 2, 8, 5]
    assert len(result) == len(data)
    assert data == original


def test_sort_even_single_element():
    assert f037.sort_even([7]) == [7]


def test_sort_even_empty_list():
    assert f037.sort_even([]) == []


def test_sort_even_two_elements():
    assert f037.sort_even([9, 1]) == [9, 1]


def test_sort_even_already_sorted_evens():
    assert f037.sort_even([1, 10, 3, 20, 5, 30]) == [1, 10, 3, 20, 5, 30]
