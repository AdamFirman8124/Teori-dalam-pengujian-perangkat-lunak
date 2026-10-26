# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_sum_product_basic():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_single_element():
    assert sum_product([5]) == (5, 5)


def test_sum_product_empty():
    assert sum_product([]) == (0, 1)


def test_sum_product_with_zero():
    assert sum_product([0, 7, 3]) == (10, 0)


def test_sum_product_negative_numbers():
    assert sum_product([-1, 2, -3]) == (-2, 6)
