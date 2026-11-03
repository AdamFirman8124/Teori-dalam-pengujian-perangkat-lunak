# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

from f094 import skjkasdkd


def test_skjkasdkd_mixed_list_returns_digit_sum_of_largest_prime():
    # Largest prime in the list is 181; its digit sum is 1 + 8 + 1 = 10.
    # This exercises: the while loop, primes smaller than current max (3, 2, 5, 7),
    # a composite larger than max (324 -> isPrime returns False via line 6),
    # and a large prime whose isPrime loop finishes without finding a divisor
    # (line 8: return True).
    assert skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10


def test_skjkasdkd_composite_larger_than_current_max_is_ignored():
    # 10 > 2 but isPrime(10) is False (line 6: return False), so maxx stays 2.
    assert skjkasdkd([2, 10]) == 2


def test_skjkasdkd_single_large_prime():
    # isPrime(97) iterates its loop fully (no divisor found) and returns True;
    # the digit sum of 97 is 9 + 7 = 16.
    assert skjkasdkd([97]) == 16


def test_skjkasdkd_no_primes_returns_zero():
    # No primes at all: maxx remains 0 and the digit sum of "0" is 0.
    # Every candidate > 0 here is composite, so the False branch of line 12's
    # condition is taken each time.
    assert skjkasdkd([0, 4, 6, 8, 9]) == 0


def test_skjkasdkd_empty_list_returns_zero():
    # The while-loop condition is False immediately; maxx stays 0.
    assert skjkasdkd([]) == 0
