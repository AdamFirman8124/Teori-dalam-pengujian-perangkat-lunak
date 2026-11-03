# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_prod_signs_empty_returns_none():
    """Covers lines 3-4: empty array short-circuits to None."""
    assert prod_signs([]) is None


def test_prod_signs_contains_zero():
    """Covers line 5 (true branch of the conditional expression): prod = 0."""
    # prod = 0 because 0 is in arr, regardless of the negative count
    assert prod_signs([1, 0, -3, 2]) == 0
    assert prod_signs([0]) == 0


def test_prod_signs_even_number_of_negatives():
    """Covers line 5 (false branch) with an even count of negatives: prod = 1."""
    # two negatives -> (-1) ** 2 == 1; sum of abs values = 1 + 2 + 3 = 6
    assert prod_signs([-1, -2, 3]) == 6


def test_prod_signs_odd_number_of_negatives():
    """Covers line 5 (false branch) with an odd count of negatives: prod = -1."""
    # one negative -> (-1) ** 1 == -1; sum of abs values = 1 + 2 + 3 = 6
    assert prod_signs([-1, 2, 3]) == -6


def test_prod_signs_all_positive():
    """Covers line 5 (false branch, zero negatives) and line 6."""
    # zero negatives -> (-1) ** 0 == 1; sum of abs values = 4
    assert prod_signs([1, 3]) == 4


def test_prod_signs_does_not_mutate_input():
    """Verifies the function is side-effect free on its argument."""
    arr = [-1, 0, 2]
    snapshot = list(arr)
    prod_signs(arr)
    assert arr == snapshot
