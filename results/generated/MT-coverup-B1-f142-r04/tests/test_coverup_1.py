# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

from f142 import sum_squares


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_executes_all_transformation_branches():
    values = [2, 3, 4, 5, 6]
    assert sum_squares(values) == 252
    assert values == [2, 3, 4, 5, 6]
