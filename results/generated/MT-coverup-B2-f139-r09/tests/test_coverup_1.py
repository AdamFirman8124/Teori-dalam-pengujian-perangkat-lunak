# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_zero_iterations():
    """n = 0: the loop body never runs; the initial value 1 is returned."""
    assert special_factorial(0) == 1


def test_special_factorial_single_iteration():
    """n = 1: loop runs exactly once; result is 1! = 1."""
    assert special_factorial(1) == 1


def test_special_factorial_multiple_iterations():
    """n = 4: loop runs several times; result is 1! * 2! * 3! * 4! = 288."""
    assert special_factorial(4) == 288


def test_special_factorial_matches_product_of_factorials():
    """General property: special_factorial(n) == product of k! for k in 1..n."""
    import math

    for n in range(0, 7):
        expected = math.prod(math.factorial(k) for k in range(1, n + 1))
        assert special_factorial(n) == expected
