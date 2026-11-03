# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

"""Tests for f094.skjkasdkd.

The function scans a list, keeps the largest prime found (isPrime inner
helper), and returns the sum of the decimal digits of that maximum (0 if no
prime is present).  The tests below exercise every line and branch:

* isPrime returning False via the divisibility check (composite inputs)
* isPrime returning True after the loop (primes, incl. n == 2 where the
  range is empty)
* the while loop body: maxx update, short-circuit when lst[i] <= maxx,
  and the case where lst[i] > maxx but the value is composite
* the empty-list / no-prime cases where maxx stays 0

Note: this implementation's isPrime treats 1 as prime (range(2, 2) is
empty, so the loop body never runs and line 8 returns True); a test
documents that actual behavior.  Negative values are avoided because
int((-n) ** 0.5) raises TypeError for complex results.

skjkasdkd is a pure function with no side effects, so no monkeypatching or
fixture-based cleanup is required; each test is fully isolated.
"""

import pytest

from f094 import skjkasdkd


def test_largest_prime_digit_sum_basic():
    """181 is the largest prime; 1 + 8 + 1 == 10 (covers lines 3-16)."""
    result = skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
    assert result == 10


def test_composite_rejected_by_isprime():
    """4 is composite: isPrime hits the `return False` branch (line 6)."""
    # 4 > 0 but not prime -> skipped; largest prime is 3 -> digit sum 3.
    assert skjkasdkd([4, 2, 3]) == 3


def test_prime_after_composite_updates_maxx():
    """9 is composite (line 6), 13 is prime (line 8) and becomes maxx."""
    # 9 > 0 but composite; 13 > 0 and prime -> maxx = 13 -> 1 + 3 == 4.
    assert skjkasdkd([9, 13]) == 4


def test_smallest_prime_two():
    """isPrime(2): range(2, int(2**0.5)+1) is empty, so line 8 returns True."""
    assert skjkasdkd([2]) == 2


def test_larger_prime_replaces_smaller_prime():
    """A later, larger prime replaces an earlier one (line 13 re-executed)."""
    # 3 is prime -> maxx = 3; 11 is prime and larger -> maxx = 11 -> 1 + 1 == 2.
    assert skjkasdkd([3, 11]) == 2


def test_short_circuit_when_not_greater_than_maxx():
    """lst[i] <= maxx short-circuits before isPrime is called."""
    # 7 is prime -> maxx = 7; 3 and 5 are <= 7 so isPrime is never called on them.
    assert skjkasdkd([7, 3, 5]) == 7


def test_greater_but_composite_keeps_maxx():
    """lst[i] > maxx but composite: maxx is unchanged."""
    # 2 is prime -> maxx = 2; 4 and 6 are > 2 but composite -> maxx stays 2.
    assert skjkasdkd([2, 4, 6]) == 2


def test_no_primes_yields_zero():
    """Only composites in the list: maxx stays 0 and digit sum of '0' is 0."""
    # 4, 6, 8, 9 are all composite (isPrime returns False for each).
    assert skjkasdkd([4, 6, 8, 9]) == 0


def test_zero_and_composites_only():
    """0 is never > maxx (0 > 0 is False), so maxx stays 0."""
    assert skjkasdkd([0, 4, 6, 8, 9]) == 0


def test_one_is_treated_as_prime_by_implementation():
    """Documents actual behavior: isPrime(1) returns True (empty range),
    so a list whose only 'prime' is 1 yields digit sum 1."""
    assert skjkasdkd([4, 6, 8, 9, 1]) == 1


def test_empty_list_yields_zero():
    """Empty list: the while loop never runs; result is digit sum of 0."""
    assert skjkasdkd([]) == 0
