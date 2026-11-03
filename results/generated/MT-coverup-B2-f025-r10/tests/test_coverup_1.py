# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import math

import pytest

from f025 import factorize


def test_factorize_composite_with_repeated_factors():
    # Covers: import, loop entry, divisible branch (append + //=), else branch,
    # loop exit, and the final n > 1 append.
    assert factorize(12) == [2, 2, 3]


def test_factorize_prime():
    # Covers: else branch (i += 1) taken repeatedly, loop exit, n > 1 append.
    assert factorize(7) == [7]


def test_factorize_large_prime():
    # Exercises many iterations of the else branch before loop exit.
    assert factorize(97) == [97]


def test_factorize_two():
    # Smallest prime: loop body runs, n becomes 1, loop re-enters with n == 1,
    # then exits; final n > 1 is False.
    assert factorize(2) == [2]


def test_factorize_one():
    # n == 1: while condition (2 <= int(sqrt(1) + 1) == 2) is True once,
    # else branch taken, then loop exits; n > 1 is False -> empty list.
    assert factorize(1) == []


def test_factorize_perfect_square():
    # n becomes 1 inside the loop; while condition re-evaluated with n == 1.
    assert factorize(4) == [2, 2]


def test_factorize_square_of_odd_prime():
    # sqrt boundary: while 3 <= int(sqrt(9) + 1) == 4 is True, then after
    # dividing, 3 <= int(sqrt(3) + 1) == 2 is False.
    assert factorize(9) == [3, 3]


def test_factorize_product_and_sorted_property():
    # Property-based check: factors multiply back to n, are >= 2 and sorted.
    for n in range(1, 300):
        factors = factorize(n)
        assert all(f >= 2 for f in factors)
        assert factors == sorted(factors)
        product = 1
        for f in factors:
            product *= f
        assert product == n
        # Cross-check against an independent reference implementation.
        assert factors == _reference_factorize(n)


def _reference_factorize(n: int) -> list:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
