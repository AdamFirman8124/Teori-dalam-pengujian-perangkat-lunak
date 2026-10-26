# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

from f142 import sum_squares


def test_sum_squares_mixed_covers_all_branches():
    lst = [1, 2, 3, 4, 5]
    # i=0 square: 1**2=1, i=1 else: 2, i=2 else: 3, i=3 square: 4**2=16, i=4 cube: 5**3=125
    assert sum_squares(lst) == 147


def test_sum_squares_range_ten_covers_all_branches():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 0 + 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81
    assert sum_squares(lst) == 717


def test_sum_squares_negative_and_zero_covers_all_branches():
    lst = [-2, -1, 0, 2, 3]
    # i=0 square: 4, i=1 else: -1, i=2 else: 0, i=3 square: 4, i=4 cube: 27
    assert sum_squares(lst) == 34
