# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_squares_positive_odd_integers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25


def test_double_the_difference_ignores_non_positive_values():
    assert double_the_difference([-1, -3, 0, 1]) == 1


def test_double_the_difference_ignores_even_values():
    assert double_the_difference([2, 4, 6, 3]) == 9


def test_double_the_difference_ignores_floats():
    assert double_the_difference([1.5, 3.0, 5.0, 7]) == 49


def test_double_the_difference_empty_list_returns_zero():
    result = double_the_difference([])
    assert result == 0
    assert isinstance(result, int)


def test_double_the_difference_all_filtered_returns_zero():
    assert double_the_difference([-2, 0, 2, 4, 1.1]) == 0


def test_double_the_difference_mixed_input():
    assert double_the_difference([-5, 0, 2, 3, 4.5, 7, 9.0]) == 9 + 49


def test_double_the_difference_does_not_mutate_input():
    lst = [1, 2, 3, -4, 5.5]
    snapshot = list(lst)
    double_the_difference(lst)
    assert lst == snapshot
