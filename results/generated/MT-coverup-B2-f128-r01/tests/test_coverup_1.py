# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_empty_array_returns_none():
    """Covers line 3 (True branch of 'if not arr') and line 4."""
    assert prod_signs([]) is None


def test_array_containing_zero_returns_zero():
    """Covers line 5 (True branch of '0 in arr', prod = 0) and line 6."""
    assert prod_signs([0, -3, 4]) == 0


def test_no_negatives_gives_positive_result():
    """Covers line 5 (False branch, zero negatives -> prod = 1) and line 6."""
    assert prod_signs([1, 2, 3]) == 6


def test_odd_number_of_negatives_gives_negative_result():
    """Covers line 5 (False branch, odd negatives -> prod = -1) and line 6."""
    assert prod_signs([-1, 2, 3]) == -6


def test_even_number_of_negatives_gives_positive_result():
    """Covers line 5 (False branch, even negatives -> prod = 1) and line 6."""
    assert prod_signs([-1, -2, 3]) == 6


def test_single_negative_element():
    """Covers line 5 (False branch, one negative -> prod = -1) and line 6."""
    assert prod_signs([-5]) == -5
