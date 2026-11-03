# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_even_composite():
    # Covers line 3 (loop), line 4 false branch (i=9,8,7,6), line 4 true
    # branch (i=5) and line 5 (return).
    assert largest_divisor(10) == 5


def test_largest_divisor_odd_composite():
    # Exercises several false-branch iterations (i=14..6) before the
    # true branch at i=5 returns.
    assert largest_divisor(15) == 5


def test_largest_divisor_prime():
    # For a prime, every candidate except 1 fails the modulo check,
    # so the false branch is taken many times before returning 1.
    assert largest_divisor(7) == 1


def test_largest_divisor_smallest_valid_input():
    # n=2 hits the true branch on the very first iteration (i=1).
    assert largest_divisor(2) == 1


def test_largest_divisor_perfect_square():
    # The largest proper divisor of 9 is 3 (its square root).
    assert largest_divisor(9) == 3
