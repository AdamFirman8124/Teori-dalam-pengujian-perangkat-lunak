# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f059 import largest_prime_factor


def test_composite_number_returns_largest_prime_factor():
    # 13195 = 5 * 7 * 13 * 29
    assert largest_prime_factor(13195) == 29


def test_prime_power():
    # 16 = 2^4, exercises is_prime returning False for composite j=4
    assert largest_prime_factor(16) == 2


def test_prime_input():
    # n itself is prime; is_prime returns True via the loop-exit path
    assert largest_prime_factor(13) == 13


def test_small_even():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(4) == 2


def test_no_divisors_in_range_returns_one():
    # n <= 1: loop body never runs, largest stays 1
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-7) == 1
