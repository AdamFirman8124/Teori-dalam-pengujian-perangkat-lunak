# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

import pytest
from script_8 import sum_product


def test_sum_product_non_empty_list():
    """Test sum_product with a non-empty list."""
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)
    assert result[0] == 10
    assert result[1] == 24


def test_sum_product_single_element():
    """Test sum_product with a single element."""
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_with_zero():
    """Test sum_product with list containing zero."""
    result = sum_product([1, 0, 3])
    assert result == (4, 0)


def test_sum_product_negative_numbers():
    """Test sum_product with negative numbers."""
    result = sum_product([-1, -2, -3])
    assert result == (-6, -6)


def test_sum_product_mixed_numbers():
    """Test sum_product with mixed positive and negative numbers."""
    result = sum_product([2, -3, 4])
    assert result == (3, -24)
