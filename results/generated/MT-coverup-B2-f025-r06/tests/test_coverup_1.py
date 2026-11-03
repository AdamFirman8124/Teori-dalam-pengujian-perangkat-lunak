# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


def test_factorize_one_returns_empty_list():
    """n = 1: loop body runs once (else branch), leftover n is not > 1."""
    assert factorize(1) == []


def test_factorize_smallest_prime():
    """n = 2: division branch taken, leftover n == 1 so nothing appended."""
    assert factorize(2) == [2]


def test_factorize_prime_power():
    """n = 4: repeated division of the same factor, final n == 1."""
    assert factorize(4) == [2, 2]


def test_factorize_composite_with_multiple_primes():
    """n = 12: exercises both the division branch and the increment branch,
    and the final 'if n > 1' True branch (leftover prime 3)."""
    assert factorize(12) == [2, 2, 3]


def test_factorize_prime_larger_than_sqrt_bound():
    """n = 97: only the else branch runs until the loop exits,
    then the leftover prime is appended."""
    assert factorize(97) == [97]


def test_factorize_mixed_factors():
    """n = 735 = 3 * 5 * 7 * 7: mixes division and increment branches,
    ends with a leftover prime factor."""
    assert factorize(735) == [3, 5, 7, 7]


def test_factorize_result_multiplies_back():
    """Postcondition: product of factors equals the original n."""
    for n in (1, 2, 4, 12, 97, 735, 2 * 2 * 3 * 3 * 5 * 13):
        factors = factorize(n)
        product = 1
        for f in factors:
            product *= f
        assert product == n
        assert all(f >= 2 for f in factors)
        assert factors == sorted(factors)
