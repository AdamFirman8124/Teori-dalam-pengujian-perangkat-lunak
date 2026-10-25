# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_prod_signs_empty_array_returns_none():
    assert prod_signs([]) is None


def test_prod_signs_nonempty_array_with_even_number_of_negatives_returns_positive_sum():
    assert prod_signs([-2, 3, -4]) == 9


def test_prod_signs_nonempty_array_with_odd_number_of_negatives_returns_negative_sum():
    assert prod_signs([-2, 3, 4]) == -9


def test_prod_signs_array_containing_zero_returns_zero():
    assert prod_signs([-2, 0, 4]) == 0
