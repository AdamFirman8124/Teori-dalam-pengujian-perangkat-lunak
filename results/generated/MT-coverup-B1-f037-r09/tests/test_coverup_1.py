# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_even_length():
    inp = [5, 6, 3, 4]
    result = sort_even(inp)
    assert result == [3, 6, 5, 4]
    # original list unchanged (no state pollution)
    assert inp == [5, 6, 3, 4]


def test_sort_even_odd_length_appends_last():
    inp = [5, 6, 3, 4, 1]
    result = sort_even(inp)
    assert result == [1, 6, 3, 4, 5]
    assert inp == [5, 6, 3, 4, 1]


def test_sort_even_empty():
    assert sort_even([]) == []


def test_sort_even_single_element():
    assert sort_even([4]) == [4]
