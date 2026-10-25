# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_with_even_length_preserves_odd_positions():
    values = [5, 3, 1, 2]
    original = values.copy()

    assert sort_even(values) == [1, 3, 5, 2]
    assert values == original


def test_sort_even_with_odd_length_appends_last_even_position():
    values = [5, 3, 1]
    original = values.copy()

    assert sort_even(values) == [1, 3, 5]
    assert values == original
