# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

import pytest

from f094 import skjkasdkd


def test_returns_digit_sum_of_largest_prime():
    # 10 is composite (hits the n % i == 0 branch), 97 is the largest prime
    assert skjkasdkd([10, 97, 4, 89]) == 16
    assert skjkasdkd([1, 2, 3, 5, 7]) == 7


def test_composite_numbers_are_rejected():
    # 9, 25 and 49 all hit the early-return branch; no prime found -> maxx stays 0
    assert skjkasdkd([9, 25, 49]) == 0


def test_empty_list_returns_zero():
    assert skjkasdkd([]) == 0


def test_smaller_primes_after_max_do_not_replace_it():
    # exercises the short-circuit where lst[i] > maxx is False
    assert skjkasdkd([7, 3, 2]) == 7


def test_negative_and_zero_values_are_ignored():
    assert skjkasdkd([-5, 0, 11]) == 2


def test_smallest_prime_uses_empty_range():
    # isPrime(2) -> range(2, 2) is empty, so the loop body never runs
    assert skjkasdkd([2]) == 2
