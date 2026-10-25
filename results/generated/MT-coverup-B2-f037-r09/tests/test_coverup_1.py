# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_even_length():
    inp = [5, 6, 3, 4]
    original = list(inp)
    result = sort_even(inp)
    assert result == [3, 6, 5, 4]
    assert inp == original


def test_sort_even_odd_length():
    inp = [5, 6, 3, 4, 1]
    original = list(inp)
    result = sort_even(inp)
    assert result == [1, 6, 3, 4, 5]
    assert inp == original


def test_sort_even_empty():
    inp = []
    result = sort_even(inp)
    assert result == []
    assert inp == []


def test_sort_even_single_element():
    inp = [4]
    original = list(inp)
    result = sort_even(inp)
    assert result == [4]
    assert inp == original
