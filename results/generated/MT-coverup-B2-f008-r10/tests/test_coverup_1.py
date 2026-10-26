# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

from f008 import sum_product


def test_sum_product_empty():
    assert sum_product([]) == (0, 1)


def test_sum_product_single():
    assert sum_product([5]) == (5, 5)


def test_sum_product_multiple():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_with_zero_and_negatives():
    assert sum_product([0, -1, 2, -3]) == (-2, 0)
    assert sum_product([-1, -2, -3]) == (-6, -6)
