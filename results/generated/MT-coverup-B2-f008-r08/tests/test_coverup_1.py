# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_sum_product_empty_list():
    """Covers lines 6-7 (initialization) and line 12 (return) with an empty loop."""
    result = sum_product([])
    assert result == (0, 1)


def test_sum_product_single_element():
    """Covers lines 9-11 (loop body) with a single element."""
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_multiple_elements():
    """Covers lines 9-11 with multiple elements, verifying both sum and product."""
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)


def test_sum_product_negative_numbers():
    """Covers lines 9-11 with negative numbers to verify accumulation logic."""
    result = sum_product([-1, -2, 3])
    assert result == (0, 6)


def test_sum_product_with_zero():
    """Covers lines 9-11 ensuring zero affects sum but nullifies product."""
    result = sum_product([0, 7, 3])
    assert result == (10, 0)
