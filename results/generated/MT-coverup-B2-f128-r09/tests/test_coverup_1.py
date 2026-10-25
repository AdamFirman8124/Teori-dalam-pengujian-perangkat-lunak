# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_prod_signs_empty_returns_none():
    assert prod_signs([]) is None


def test_prod_signs_zero_in_arr_returns_zero():
    assert prod_signs([1, 0, -2]) == 0
    assert prod_signs([0, 1, 2]) == 0 * (0 + 1 + 2)


def test_prod_signs_all_positive():
    assert prod_signs([1, 2, 3]) == 6


def test_prod_signs_odd_negatives():
    assert prod_signs([-1, 2, 3]) == -6


def test_prod_signs_even_negatives():
    assert prod_signs([-1, -2, 3]) == 6
