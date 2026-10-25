# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_empty_list_returns_none():
    assert prod_signs([]) is None


def test_zero_in_arr_returns_zero():
    assert prod_signs([0, 1, 2]) == 0
    assert prod_signs([0]) == 0


def test_zero_with_negatives_returns_zero():
    assert prod_signs([0, -1, 2]) == 0 * (0 + 1 + 2)


def test_all_positive_prod_one():
    assert prod_signs([1, 2, 3]) == 1 * (1 + 2 + 3)


def test_odd_negatives_prod_minus_one():
    # covers lambda x: x < 0 -> True and False, and (-1) ** odd == -1
    assert prod_signs([-1, 2, 3]) == -1 * (1 + 2 + 3)
    assert prod_signs([-5]) == -5


def test_even_negatives_prod_one():
    # covers lambda x: x < 0 -> True and False, and (-1) ** even == 1
    assert prod_signs([-1, -2, 3]) == 1 * (1 + 2 + 3)
    assert prod_signs([-1, -1]) == 1 * (1 + 1)
