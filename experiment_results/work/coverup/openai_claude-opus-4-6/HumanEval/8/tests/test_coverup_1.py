# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

from typing import List, Tuple

import pytest

from script_8 import sum_product


def test_sum_product_empty_list():
    # Covers lines 12, 13, 15 (loop not entered), 18
    result = sum_product([])
    assert result == (0, 1)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_sum_product_single_element():
    # Covers lines 12-18 with exactly one iteration
    result = sum_product([5])
    assert result == (5, 5)


def test_sum_product_multiple_elements():
    # Covers lines 12-18 with several iterations
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)


def test_sum_product_negative_and_zero():
    # Branch/edge coverage with negatives and zero
    assert sum_product([-1, -2, -3]) == (-6, -6)
    assert sum_product([0, 7, 3]) == (10, 0)


def test_sum_product_does_not_mutate_input():
    # Postcondition: input list is unchanged
    numbers: List[int] = [2, 4, 6]
    original = list(numbers)
    result: Tuple[int, int] = sum_product(numbers)
    assert result == (12, 48)
    assert numbers == original
