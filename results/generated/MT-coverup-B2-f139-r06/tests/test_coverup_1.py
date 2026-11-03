# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_basic():
    """Covers lines 3-8: initialization, loop body, and return.

    special_factorial(n) = 1! * 2! * ... * n!
    For n=4: 1 * 2 * 6 * 24 = 288
    """
    assert special_factorial(4) == 288


def test_special_factorial_single_element():
    """Loop body executes exactly once (n=1): result is 1! = 1."""
    assert special_factorial(1) == 1


def test_special_factorial_zero():
    """n=0: loop body never runs, returns initial value 1."""
    assert special_factorial(0) == 1


def test_special_factorial_matches_factorial_product():
    """Verify against an independent computation of the product of factorials."""
    import math

    for n in range(1, 8):
        expected = math.prod(math.factorial(i) for i in range(1, n + 1))
        assert special_factorial(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 12),
        (4, 288),
        (5, 34560),
    ],
)
def test_special_factorial_known_values(n, expected):
    assert special_factorial(n) == expected
