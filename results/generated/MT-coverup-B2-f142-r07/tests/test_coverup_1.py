# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

from f142 import sum_squares


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_square_branch():
    # indices 0 and 3 are divisible by 3 -> squared
    assert sum_squares([2]) == 4
    assert sum_squares([10, 20, 30]) == 100 + 20 + 30
    assert sum_squares([4, 5, 6, 7]) == 16 + 5 + 6 + 49


def test_sum_squares_cube_branch():
    # index 4: i % 4 == 0 and i % 3 != 0 -> cubed
    # i0=1**2=1, i1=1, i2=1, i3=1**2=1, i4=2**3=8
    assert sum_squares([1, 1, 1, 1, 2]) == 12
    # index 8: i % 4 == 0 and i % 3 != 0 -> cubed
    lst = [1, 1, 1, 1, 1, 1, 1, 1, 2]
    # 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 8 = 16
    assert sum_squares(lst) == 16


def test_sum_squares_else_branch():
    # indices 1, 2, 5, 7, 10, 11 -> appended as-is
    assert sum_squares([0, 5, 6]) == 0 + 5 + 6
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 0 + 1 + 2 + 9 + 64 + 5


def test_sum_squares_full_coverage():
    # covers i%3==0, i%4==0 cube, and else in one call, including i=12
    lst = list(range(13))
    # 0,1,2,9,64,5,36,7,512,81,10,11,144
    assert sum_squares(lst) == 882
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 1,2,3,16,125,6,49,8,729
    assert sum_squares(lst2) == 939
