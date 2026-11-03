# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import math

import pytest

from f025 import factorize


def test_factorize_of_one_returns_empty_list():
    """n == 1: the loop body runs once via the else branch (i += 1),
    the loop then exits, and the final `n > 1` check is False."""
    assert factorize(1) == []


def test_factorize_of_two():
    """Smallest input that takes the `n % i == 0` branch exactly once."""
    assert factorize(2) == [2]


def test_factorize_prime_returns_single_trailing_factor():
    """Prime input: every candidate fails (else branch taken repeatedly),
    the loop exits, and `n > 1` is True so n itself is appended."""
    assert factorize(97) == [97]


def test_factorize_prime_power_repeats_same_factor():
    """8 == 2**3: the dividing branch is taken three times in a row."""
    assert factorize(8) == [2, 2, 2]


def test_factorize_composite_fully_factored():
    """210 == 2*3*5*7: mixes both branches of the if/else; the loop ends
    with n == 1 so the final `n > 1` check is False."""
    assert factorize(210) == [2, 3, 5, 7]


def test_factorize_composite_with_large_prime_leftover():
    """194 == 2*97: divides by 2, then no candidate divides 97 within the
    loop bound, so `n > 1` is True and 97 is appended at the end."""
    assert factorize(194) == [2, 97]


def test_factorize_mixed_exponents():
    """360 == 2**3 * 3**2 * 5: repeated factors of several different primes."""
    result = factorize(360)
    assert result == [2, 2, 2, 3, 3, 5]
    assert isinstance(result, list)
    assert all(isinstance(f, int) for f in result)


@pytest.mark.parametrize(
    "n", [2, 3, 4, 8, 97, 210, 194, 360, 2 * 3 * 5 * 7 * 11 * 13]
)
def test_factorize_product_of_factors_equals_n(n):
    """Postcondition: the returned factors multiply back to n and each
    factor evenly divides n."""
    factors = factorize(n)
    assert math.prod(factors) == n
    assert all(n % f == 0 for f in factors)

# Note: factorize is a pure function (its `import math` only binds a local
# name and it mutates no module/global state), so no monkeypatching or
# teardown is required to avoid state pollution between tests.
