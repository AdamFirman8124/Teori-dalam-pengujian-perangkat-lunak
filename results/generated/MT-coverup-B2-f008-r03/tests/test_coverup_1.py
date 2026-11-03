# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_sum_product_empty_list():
    """Covers lines 6-7 and 12 (loop body skipped for empty input)."""
    result = sum_product([])
    assert result == (0, 1)


def test_sum_product_single_element():
    """Covers lines 6-12 including one loop iteration."""
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_multiple_elements():
    """Covers lines 6-12 with multiple loop iterations."""
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)


def test_sum_product_with_negatives_and_zero():
    """Covers lines 6-12 with negative values and zero."""
    result = sum_product([-1, 0, 3])
    assert result == (2, 0)
