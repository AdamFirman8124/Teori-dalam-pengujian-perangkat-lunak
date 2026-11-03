# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_basic():
    # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert special_factorial(4) == 288


def test_special_factorial_one():
    # Executes lines 3-8 with a single loop iteration: 1! = 1
    assert special_factorial(1) == 1


def test_special_factorial_two():
    # 1! * 2! = 1 * 2 = 2
    assert special_factorial(2) == 2


def test_special_factorial_zero():
    # Covers the branch where the loop body never executes (range(1, 1) is empty)
    assert special_factorial(0) == 1


def test_special_factorial_matches_bruteforce():
    # Cross-check against a straightforward brute-force computation
    import math

    for n in range(0, 8):
        expected = math.prod(math.factorial(i) for i in range(1, n + 1))
        assert special_factorial(n) == expected
