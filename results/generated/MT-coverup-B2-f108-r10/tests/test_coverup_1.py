# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

from f108 import count_nums


def test_count_nums_positive_and_zero():
    # 12 -> 1+2=3 >0 counted, 7 -> 7 >0 counted, 0 -> 0 not counted, 100 -> 1+0+0=1 counted
    assert count_nums([12, 7, 0, 100]) == 3


def test_count_nums_negative_branch():
    # -5 -> -5 not counted, -22 -> -2+2=0 not counted, -12 -> -1+2=1 counted, -35 -> -3+5=2 counted
    assert count_nums([-5, -22, -12, -35]) == 2


def test_count_nums_mixed_covers_both_branches():
    # 123 -> 6 counted (n>=0, x>0 True), -123 -> -1+2+3=4 counted (n<0, x>0 True)
    # 0 -> 0 not counted (x>0 False), -10 -> -1+0=-1 not counted (n<0, x>0 False)
    assert count_nums([123, -123, 0, -10]) == 2


def test_count_nums_empty_and_all_non_positive():
    assert count_nums([]) == 0
    # 0 -> 0, -5 -> -5, -22 -> 0, -100 -> -1+0+0=-1 : none > 0
    assert count_nums([0, -5, -22, -100]) == 0
