# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_sum_product_empty_list():
    """Covers lines 6-7 (initialization) and 12 (return) with an empty iterable."""
    result = sum_product([])
    assert result == (0, 1)


def test_sum_product_single_element():
    """Covers the loop body (lines 10-11) with one element."""
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_multiple_elements():
    """Covers all lines 6-12 with multiple elements."""
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)


def test_sum_product_with_negatives_and_zero():
    """Covers loop body with negative numbers and zero."""
    result = sum_product([-1, 0, 7])
    assert result == (6, 0)
