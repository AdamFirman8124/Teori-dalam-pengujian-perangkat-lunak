# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f133 import sum_squares


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_rounds_up_and_sums_squares():
    assert sum_squares([1.2, -1.2, 2]) == 9
