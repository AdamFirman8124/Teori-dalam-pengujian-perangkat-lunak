# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f133 import sum_squares


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([0]) == 0
    assert sum_squares([-1, -2]) == 1 + 4


def test_sum_squares_ceil_floats():
    # math.ceil(1.2) == 2 -> 4, math.ceil(2.5) == 3 -> 9, math.ceil(-1.1) == -1 -> 1
    assert sum_squares([1.2, 2.5, -1.1]) == 4 + 9 + 1
    assert sum_squares([1.0, 2.0]) == 1 + 4
    assert sum_squares([0.1]) == 1
