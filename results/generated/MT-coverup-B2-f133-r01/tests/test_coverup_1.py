# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f133 import sum_squares


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([0]) == 0
    assert sum_squares([-1, -2]) == 5


def test_sum_squares_floats_require_ceil():
    # ceil(1.4)=2, ceil(2.2)=3 -> 4 + 9 = 13
    assert sum_squares([1.4, 2.2]) == 13
    # ceil(-1.5)=-1, ceil(-2.1)=-2 -> 1 + 4 = 5
    assert sum_squares([-1.5, -2.1]) == 5
    # ceil(1.0)=1, ceil(0.0)=0
    assert sum_squares([1.0, 0.0]) == 1
