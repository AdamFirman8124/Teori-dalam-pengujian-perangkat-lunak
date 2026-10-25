# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_computes_product_of_factorials():
    # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert special_factorial(4) == 288


def test_special_factorial_single_iteration():
    # 1! = 1
    assert special_factorial(1) == 1


def test_special_factorial_two_iterations():
    # 1! * 2! = 1 * 2 = 2
    assert special_factorial(2) == 2


def test_special_factorial_matches_bruteforce():
    import math

    for n in range(1, 8):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert special_factorial(n) == expected
