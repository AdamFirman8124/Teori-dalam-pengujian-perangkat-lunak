# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_too_heavy_returns_false():
    # sum(q) > w -> line 3 branch taken, returns False at line 4
    assert will_it_fly([3, 2, 3], 1) is False
    assert will_it_fly([1, 2], 2) is False


def test_unbalanced_returns_false():
    # sum <= w but q[i] != q[j] -> returns False at line 9
    assert will_it_fly([1, 2], 5) is False
    assert will_it_fly([3, 2, 3, 1], 100) is False


def test_balanced_and_light_returns_true():
    # palindrome with sum <= w -> loop runs, exits, returns True at line 12
    assert will_it_fly([3, 2, 3], 9) is True
    assert will_it_fly([1, 2, 1], 5) is True


def test_single_element_within_weight_returns_true():
    # len(q) == 1 -> i == j, while loop body never runs, returns True
    assert will_it_fly([2], 5) is True


def test_empty_list_returns_true():
    # len(q) == 0 -> i=0, j=-1, while loop never runs, returns True
    assert will_it_fly([], 5) is True


def test_exact_weight_boundary_returns_true():
    # sum(q) == w -> not greater, so proceeds to palindrome check
    assert will_it_fly([1, 2, 1], 4) is True
