# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_with_even_length():
    values = [4, 9, 2, 7]
    original = values.copy()

    assert sort_even(values) == [2, 9, 4, 7]
    assert values == original


def test_sort_even_with_odd_length():
    values = [6, 9, 2, 7, 4]
    original = values.copy()

    assert sort_even(values) == [2, 9, 4, 7, 6]
    assert values == original
