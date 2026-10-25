# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

from f142 import sum_squares


def test_sum_squares_exercises_all_index_branches():
    values = [1, 2, 3, 4, 5]
    original = values.copy()

    assert sum_squares(values) == 147
    assert values == original


def test_sum_squares_with_empty_list():
    values = []

    assert sum_squares(values) == 0
    assert values == []
