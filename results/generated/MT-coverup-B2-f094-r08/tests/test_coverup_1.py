# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

from f094 import skjkasdkd


def test_largest_prime_digit_sum_basic():
    """4 is composite (isPrime returns False on its first divisor), 7 is prime
    and becomes maxx, 9 is composite after two loop iterations, and 2 is
    skipped by short-circuit evaluation (2 > 7 is False)."""
    assert skjkasdkd([4, 7, 9, 2]) == 7


def test_is_prime_loop_multiple_iterations():
    """25 makes the isPrime loop iterate over 2, 3, 4 before finding divisor 5
    (covers the False branch of n % i == 0 several times); 29 iterates over the
    same range and returns True (covers the True branch after iterations)."""
    assert skjkasdkd([25, 29]) == 11  # digit sum of 29 -> 2 + 9


def test_small_prime_empty_range():
    """isPrime(2) gets an empty range(2, int(2**0.5)+1), so the for loop body
    never runs and True is returned directly."""
    assert skjkasdkd([2]) == 2


def test_no_prime_maxx_stays_zero():
    """No element is prime, so maxx stays 0 and the digit sum of '0' is 0.
    Note: 1 is deliberately excluded, because this implementation's isPrime(1)
    returns True (empty range) and would make maxx = 1. The elements 0 and -5
    still cover the short-circuit False branch (lst[i] <= maxx)."""
    assert skjkasdkd([4, 6, 8, 9, 0, -5]) == 0


def test_empty_list_while_loop_never_runs():
    """Empty list: the while condition is immediately False, maxx stays 0 and
    the digit sum of '0' (0) is returned."""
    assert skjkasdkd([]) == 0


def test_multi_digit_prime_digit_sum():
    """13 is the largest prime; the result is the sum of its digits, 1 + 3."""
    assert skjkasdkd([10, 13, 15]) == 4
