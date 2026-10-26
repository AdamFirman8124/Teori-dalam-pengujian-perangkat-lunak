# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

from f070 import strange_sort_list


def test_empty_list():
    lst = []
    result = strange_sort_list(lst)
    assert result == []
    assert lst == []


def test_single_element():
    lst = [42]
    result = strange_sort_list(lst)
    assert result == [42]
    assert lst == []


def test_odd_length_alternation():
    lst = [5, 3, 1, 4, 2]
    input_copy = list(lst)
    result = strange_sort_list(lst)
    assert result == [1, 5, 2, 4, 3]
    assert lst == []
    assert sorted(result) == sorted(input_copy)


def test_even_length_alternation():
    lst = [3, 1, 2, 4]
    input_copy = list(lst)
    result = strange_sort_list(lst)
    # min, max, min, max
    assert result == [1, 4, 2, 3]
    assert lst == []
    assert sorted(result) == sorted(input_copy)


def test_duplicates_and_negatives():
    lst = [2, 2, -1, 0, -1]
    input_copy = list(lst)
    result = strange_sort_list(lst)
    # min(-1), max(2), min(-1), max(2), min(0)
    assert result == [-1, 2, -1, 2, 0]
    assert lst == []
    assert sorted(result) == sorted(input_copy)
