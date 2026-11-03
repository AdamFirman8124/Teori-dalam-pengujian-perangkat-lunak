# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


def test_factorize_one_returns_empty_list():
    """n=1: loop body runs once (else branch), n is not > 1 -> empty list."""
    assert factorize(1) == []


def test_factorize_small_prime():
    """n=3: loop runs once (else branch), remaining n > 1 is appended."""
    assert factorize(3) == [3]


def test_factorize_large_prime():
    """n=97: no divisor found up to sqrt, remaining n > 1 is appended."""
    assert factorize(97) == [97]


def test_factorize_composite_with_repeated_factors():
    """n=12: exercises the divisible branch (append + integer division)."""
    assert factorize(12) == [2, 2, 3]


def test_factorize_prime_power():
    """n=8: same prime factor appended multiple times, n reduced to 1."""
    assert factorize(8) == [2, 2, 2]


def test_factorize_mixed_factors():
    """n=360: mixed prime factors, product of factors reconstructs n."""
    assert factorize(360) == [2, 2, 2, 3, 3, 5]


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (97, [97]),
        (100, [2, 2, 5, 5]),
        (999983, [999983]),
    ],
)
def test_factorize_parametrized(n, expected):
    assert factorize(n) == expected


@pytest.mark.parametrize(
    "n",
    [2, 3, 12, 97, 360, 999983, 2 * 3 * 5 * 7 * 11 * 13],
)
def test_factorize_product_of_factors_equals_input(n):
    factors = factorize(n)
    product = 1
    for f in factors:
        product *= f
    assert product == n
    assert all(
        factors[i] <= factors[i + 1] for i in range(len(factors) - 1)
    ), "factors must be non-decreasing"
