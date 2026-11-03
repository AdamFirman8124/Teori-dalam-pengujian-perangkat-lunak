# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_prod_signs_empty_returns_none():
    """Covers lines 3-4: empty array short-circuits to None."""
    assert prod_signs([]) is None


def test_prod_signs_with_zero_returns_zero():
    """Covers line 5 (true branch of '0 in arr'): prod is 0."""
    assert prod_signs([1, 0, -2, 3]) == 0


def test_prod_signs_even_number_of_negatives():
    """Covers line 5 (false branch, even negative count): prod = (-1)**2 = 1."""
    # negatives: -1, -3 -> prod = 1; sum of abs = 1+2+3+4 = 10
    assert prod_signs([-1, 2, -3, 4]) == 10


def test_prod_signs_odd_number_of_negatives():
    """Covers line 5 (false branch, odd negative count): prod = (-1)**1 = -1."""
    # negatives: -1 -> prod = -1; sum of abs = 1+2+3 = 6
    assert prod_signs([-1, 2, 3]) == -6


def test_prod_signs_no_negatives():
    """Covers line 5 (false branch, zero negatives): prod = (-1)**0 = 1."""
    assert prod_signs([1, 2, 3]) == 6
