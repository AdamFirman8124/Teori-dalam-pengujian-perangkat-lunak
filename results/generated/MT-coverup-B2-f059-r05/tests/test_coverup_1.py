# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f059 import largest_prime_factor


def test_largest_prime_factor_basic():
    # 13195 = 5 * 7 * 13 * 29
    assert largest_prime_factor(13195) == 29


def test_largest_prime_factor_prime_input():
    # n itself is prime: loop runs, is_prime(n) is True
    assert largest_prime_factor(13) == 13


def test_largest_prime_factor_two():
    # smallest valid input; exercises the loop with a single iteration
    assert largest_prime_factor(2) == 2


def test_largest_prime_factor_power_of_two():
    # 8 = 2^3; only prime factor is 2
    assert largest_prime_factor(8) == 2


def test_largest_prime_factor_composite_with_small_primes():
    # 15 = 3 * 5; exercises is_prime returning False for composite divisors
    assert largest_prime_factor(15) == 5


def test_largest_prime_factor_one():
    # n = 1: loop body never executes, returns initial largest = 1
    assert largest_prime_factor(1) == 1
