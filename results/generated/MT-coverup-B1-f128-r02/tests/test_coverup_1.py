# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_prod_signs_empty_array_returns_none():
    assert prod_signs([]) is None


def test_prod_signs_with_zero_returns_zero():
    # prod = 0 because 0 in arr, so result must be 0
    assert prod_signs([1, 0, -3, 2]) == 0


def test_prod_signs_even_number_of_negatives():
    # two negatives -> prod = (-1)**2 = 1
    assert prod_signs([-1, -2, 3]) == 1 * (1 + 2 + 3)


def test_prod_signs_odd_number_of_negatives():
    # three negatives -> prod = (-1)**3 = -1
    assert prod_signs([-1, -2, -3, 4]) == -1 * (1 + 2 + 3 + 4)


def test_prod_signs_all_positive():
    # no negatives -> prod = (-1)**0 = 1
    assert prod_signs([2, 5, 7]) == 14
