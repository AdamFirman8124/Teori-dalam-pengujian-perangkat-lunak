# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

"""Tests for f008.sum_product covering lines 6-12 (init, loop, return)
and both branches of the for-loop (non-empty and empty input).

sum_product is a pure function with no side effects or module state,
so no monkeypatching/cleanup is required; each test is self-contained.
"""

from typing import List, Tuple

import pytest

from f008 import sum_product


def test_sum_product_nonempty_list_executes_loop_body():
    """Covers lines 6-7 (init), 9-11 (loop entered and body executed), 12 (return)."""
    numbers: List[int] = [1, 2, 3, 4]
    result: Tuple[int, int] = sum_product(numbers)
    # Postconditions: sum and product of all elements.
    assert result == (10, 24)
    assert result[0] == sum(numbers)
    assert result[1] == 1 * 2 * 3 * 4


def test_sum_product_empty_list_skips_loop_body():
    """Covers the for-loop branch where the body is never entered (empty list)."""
    result: Tuple[int, int] = sum_product([])
    # Postconditions: identity values for sum (0) and product (1).
    assert result == (0, 1)


def test_sum_product_single_element():
    """Loop body executes exactly once."""
    result: Tuple[int, int] = sum_product([7])
    assert result == (7, 7)


def test_sum_product_with_zero_and_negatives():
    """Loop body handles zero (product collapses) and negative values."""
    result: Tuple[int, int] = sum_product([-2, 3, 0])
    assert result == (1, 0)
    assert result[0] == -2 + 3 + 0
    assert result[1] == -2 * 3 * 0
