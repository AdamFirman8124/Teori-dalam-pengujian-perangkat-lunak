# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_with_odd_length():
    values = [5, 1, 3, 2, 4]
    original = values.copy()

    result = sort_even(values)

    assert result == [3, 1, 4, 2, 5]
    assert values == original


def test_sort_even_with_even_length():
    values = [4, 1, 2, 3]
    original = values.copy()

    result = sort_even(values)

    assert result == [2, 1, 4, 3]
    assert values == original
