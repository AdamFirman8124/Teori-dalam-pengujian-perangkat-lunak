# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_prod_signs_empty_returns_none():
    """Covers lines 3-4: empty array short-circuits to None."""
    assert prod_signs([]) is None


def test_prod_signs_with_zero_returns_zero():
    """Covers line 5 (true branch of the conditional expression) and line 6."""
    # 0 in arr -> prod = 0, so result must be 0 regardless of other elements.
    assert prod_signs([1, 0, -3, 2]) == 0


def test_prod_signs_even_number_of_negatives():
    """Covers line 5 (false branch, even count of negatives -> prod = 1) and line 6."""
    # Two negatives -> (-1) ** 2 == 1; sum of abs values = 1 + 2 + 3 + 4 = 10.
    assert prod_signs([-1, 2, -3, 4]) == 10


def test_prod_signs_odd_number_of_negatives():
    """Covers line 5 (false branch, odd count of negatives -> prod = -1) and line 6."""
    # One negative -> (-1) ** 1 == -1; sum of abs values = 1 + 2 + 3 = 6.
    assert prod_signs([-1, 2, 3]) == -6


def test_prod_signs_all_negative():
    """Covers line 5 (false branch, odd count) and line 6 with all-negative input."""
    # Three negatives -> prod = -1; sum of abs values = 1 + 2 + 3 = 6.
    assert prod_signs([-1, -2, -3]) == -6


def test_prod_signs_all_positive():
    """Covers line 5 (false branch, zero negatives -> prod = 1) and line 6."""
    # No negatives -> (-1) ** 0 == 1; sum of abs values = 1 + 2 + 3 = 6.
    assert prod_signs([1, 2, 3]) == 6
