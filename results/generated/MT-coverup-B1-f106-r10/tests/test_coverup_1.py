# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

from f106 import f


def test_f_zero_returns_empty_list():
    assert f(0) == []


def test_f_one_odd_branch():
    assert f(1) == [1]


def test_f_two_covers_even_and_odd_branches():
    assert f(2) == [1, 2]


def test_f_five_covers_repeated_loops():
    assert f(5) == [1, 2, 6, 24, 15]


def test_f_four_factorial_and_sum_values():
    result = f(4)
    assert result == [1, 2, 6, 24]
    assert len(result) == 4
