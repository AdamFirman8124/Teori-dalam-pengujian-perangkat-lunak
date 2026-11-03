# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_sum_product_basic():
    """Exercises lines 6-12 with a non-empty list (loop body executes)."""
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)


def test_sum_product_empty():
    """Covers the branch where the loop body never executes."""
    result = sum_product([])
    assert result == (0, 1)


def test_sum_product_single_element():
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_negatives():
    result = sum_product([-1, 2, -3])
    assert result == (-2, 6)


def test_sum_product_with_zero():
    result = sum_product([0, 5, 7])
    assert result == (12, 0)


def test_sum_product_returns_tuple():
    result = sum_product([2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == 5
    assert result[1] == 6
