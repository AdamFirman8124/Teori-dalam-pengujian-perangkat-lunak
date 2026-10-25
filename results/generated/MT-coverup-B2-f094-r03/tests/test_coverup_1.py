# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

import pytest

from f094 import skjkasdkd


def test_largest_prime_digit_sum():
    # 13 is the largest prime; 1 + 3 == 4
    assert skjkasdkd([4, 2, 13, 3]) == 4


def test_prime_larger_than_maxx_wins_over_smaller_prime():
    # 7 is prime and larger than 3, so maxx becomes 7; digit sum == 7
    assert skjkasdkd([3, 7]) == 7


def test_composite_greater_than_maxx_is_skipped():
    # 9 > 3 but isPrime(9) is False (9 % 3 == 0), so maxx stays 3; digit sum == 3
    assert skjkasdkd([9, 3]) == 3


def test_smallest_prime_two_hits_empty_loop_branch():
    # isPrime(2): range(2, int(2**0.5)+1) is empty, so returns True; digit sum == 2
    assert skjkasdkd([2]) == 2


def test_no_primes_returns_zero():
    # No primes at all: maxx stays 0, sum of digits of "0" is 0
    assert skjkasdkd([4, 6, 8, 9, 10]) == 0


def test_empty_list_returns_zero():
    # While loop never runs; result is digit sum of 0
    assert skjkasdkd([]) == 0


def test_prime_equal_to_maxx_not_replaced():
    # 11 appears twice; second 11 is not > maxx, so no replacement; digit sum == 2
    assert skjkasdkd([11, 11]) == 2
