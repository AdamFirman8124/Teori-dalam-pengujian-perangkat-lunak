# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f151 import double_the_difference


def test_empty_list():
    assert double_the_difference([]) == 0


def test_positive_odd_ints_included():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25
    assert double_the_difference([1]) == 1
    assert double_the_difference([7]) == 49


def test_non_positive_filtered():
    # i > 0 is False
    assert double_the_difference([-1, -3, -5]) == 0
    assert double_the_difference([0]) == 0
    assert double_the_difference([-2, -4, 0]) == 0


def test_even_ints_filtered():
    # i > 0 True, i % 2 != 0 False
    assert double_the_difference([2, 4, 6, 8]) == 0
    assert double_the_difference([1, 2, 3, 4]) == 1 + 9


def test_floats_filtered_by_dot_check():
    # i > 0 True, i % 2 != 0 True, "." not in str(i) False
    assert double_the_difference([3.0, 5.0]) == 0
    assert double_the_difference([1.5, 2.5, 3.5]) == 0
    assert double_the_difference([1, 3.0, 3, 5.0]) == 1 + 9


def test_mixed_list():
    assert double_the_difference([1, 2, 3, -1, -3, 0, 3.0, 4.5, 5]) == 1 + 9 + 25
    assert double_the_difference([-7, 0, 2, 4, 1.0, 7]) == 49
