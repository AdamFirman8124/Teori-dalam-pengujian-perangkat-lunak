# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


def test_factorize_one_returns_empty_list():
    """n=1: loop body runs once via the else branch (i += 1), then `n > 1` is False."""
    assert factorize(1) == []


def test_factorize_two():
    """n=2: exercises the True branch of `n % i == 0` and the True branch of `n > 1`."""
    assert factorize(2) == [2]


def test_factorize_prime_above_loop_bound():
    """Large primes: many else-branch iterations, then the leftover n is appended."""
    assert factorize(97) == [97]
    assert factorize(999983) == [999983]


def test_factorize_repeated_prime_factors():
    """The same divisor i is consumed several times (True branch taken repeatedly)."""
    assert factorize(4) == [2, 2]
    assert factorize(8) == [2, 2, 2]
    assert factorize(12) == [2, 2, 3]


def test_factorize_distinct_primes():
    """Mixed divisors alternate between the if and else branches."""
    assert factorize(2 * 3 * 5 * 7) == [2, 3, 5, 7]
    assert factorize(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]


@pytest.mark.parametrize("n", list(range(1, 300)) + [999983, 30030, 2 ** 10])
def test_factorize_factors_multiply_back_to_n(n):
    """Postcondition: factors are >= 2 and their product reconstructs n exactly."""
    factors = factorize(n)
    assert all(f >= 2 for f in factors)
    product = 1
    for f in factors:
        product *= f
    assert product == n
