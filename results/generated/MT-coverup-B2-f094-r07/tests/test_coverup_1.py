# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

import pytest

from f094 import skjkasdkd


def test_digit_sum_of_largest_prime():
    # Largest prime in the list is 181 -> 1 + 8 + 1 = 10.
    # Covers: isPrime True path (line 8), loop, maxx update (line 13),
    # digit-sum computation (lines 15-16).
    assert skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10


def test_multi_digit_prime():
    # Largest prime is 4597 -> 4 + 5 + 9 + 7 = 25.
    assert skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25


def test_single_digit_prime_wins():
    # 8 is composite (isPrime returns False), 1 is treated as prime by the
    # empty-range path, then 2 and finally 7 become the max.
    assert skjkasdkd([0, 8, 1, 2, 1, 7]) == 7


def test_composite_larger_than_prime_is_rejected():
    # 4 is composite: isPrime(4) enters the loop body and hits the
    # "return False" branch (lines 5-6). 3 is prime and becomes the max.
    assert skjkasdkd([4, 3]) == 3


def test_composite_rejected_after_non_divisor_trial():
    # isPrime(9): 9 % 2 != 0 (loop condition False), then 9 % 3 == 0 ->
    # return False. Covers the loop-continue path inside isPrime.
    assert skjkasdkd([9, 7]) == 7


def test_smaller_values_short_circuit_first_condition():
    # Once maxx == 5, later values fail "lst[i] > maxx" so isPrime is never
    # called for them (short-circuit branch of the `and` on line 12).
    assert skjkasdkd([5, 3, 2]) == 5


def test_empty_list_returns_zero():
    # While-loop exit branch (loop body never runs); maxx stays 0 and the
    # digit sum of "0" is 0.
    assert skjkasdkd([]) == 0


def test_smallest_prime():
    # isPrime(2): range(2, int(2**0.5)+1) is empty, so the for-loop body
    # never runs and True is returned immediately.
    assert skjkasdkd([2]) == 2
