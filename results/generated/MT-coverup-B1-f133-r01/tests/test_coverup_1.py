# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f133 import sum_squares


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    assert sum_squares([1, 2, 3]) == 14


def test_sum_squares_floats_with_ceil():
    # math.ceil(1.2) == 2, math.ceil(2.5) == 3, math.ceil(-1.1) == -1
    # 2**2 + 3**2 + (-1)**2 == 14
    assert sum_squares([1.2, 2.5, -1.1]) == 14
