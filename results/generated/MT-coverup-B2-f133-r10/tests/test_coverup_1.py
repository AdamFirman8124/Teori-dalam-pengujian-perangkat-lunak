# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f133 import sum_squares


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    assert sum_squares([0.1]) == 1
    assert sum_squares([2.0]) == 4
    assert sum_squares([0]) == 0


def test_sum_squares_multiple_positive_floats():
    # ceil(1.1)=2, ceil(2.3)=3, ceil(3.0)=3 -> 4 + 9 + 9
    assert sum_squares([1.1, 2.3, 3.0]) == 22


def test_sum_squares_integers():
    assert sum_squares([1, 2, 3]) == 14


def test_sum_squares_negative_numbers():
    # ceil(-1.5)=-1, ceil(-2.1)=-2 -> 1 + 4
    assert sum_squares([-1.5, -2.1]) == 5
    # ceil(-0.5)=0
    assert sum_squares([-0.5]) == 0


def test_sum_squares_mixed_and_zero():
    # ceil(0)=0, ceil(0.5)=1, ceil(-1.2)=-1 -> 0 + 1 + 1
    assert sum_squares([0, 0.5, -1.2]) == 2
