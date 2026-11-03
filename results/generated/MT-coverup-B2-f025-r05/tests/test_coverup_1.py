# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

"""Tests for f025.factorize covering lines 6-18 (previously uncovered).

factorize is a pure function (its only import, `math`, is function-local, so no
module state is created or mutated); therefore no monkeypatching/teardown is
required and no state can leak between tests.
"""

import pytest

from f025 import factorize


def test_factorize_composite_with_repeated_factors():
    """Covers import (6), init (7-8), loop (9), divisible branch (10-12),
    leftover-prime branch (16-17) and return (18)."""
    assert factorize(12) == [2, 2, 3]


def test_factorize_prime():
    """Covers the non-divisible/increment branch (14) and leftover prime (16-17)."""
    assert factorize(7) == [7]


def test_factorize_two():
    """Smallest prime: loop body runs once, then n == 1 so line 17 is skipped
    (False branch of the `if n > 1` check)."""
    assert factorize(2) == [2]


def test_factorize_perfect_square():
    """Same prime divides repeatedly until n is fully reduced."""
    assert factorize(4) == [2, 2]


def test_factorize_one():
    """n = 1: loop condition (9) is evaluated True then False, no factor is
    appended, and `n > 1` is False."""
    assert factorize(1) == []


def test_factorize_large_prime():
    """Exercises many increments of i (line 14) before the loop terminates."""
    assert factorize(13) == [13]


def test_factorize_multiple_distinct_primes():
    """Mixes the divisible branch (10-12) and increment branch (14) in one run."""
    assert factorize(100) == [2, 2, 5, 5]


@pytest.mark.parametrize("n", [2, 3, 4, 12, 97, 100, 360, 9973])
def test_factorize_product_of_factors_equals_n(n):
    """Postcondition: factors multiply back to n and are all >= 2."""
    factors = factorize(n)
    assert all(f >= 2 for f in factors)
    product = 1
    for f in factors:
        product *= f
    assert product == n


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (12, [2, 2, 3]),
        (97, [97]),
        (360, [2, 2, 2, 3, 3, 5]),
        (9973, [9973]),
    ],
)
def test_factorize_expected_values(n, expected):
    assert factorize(n) == expected
