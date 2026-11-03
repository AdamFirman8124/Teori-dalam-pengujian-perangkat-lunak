# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

# Tests for f039.prime_fib.
#
# prime_fib is a pure function (no I/O, no globals, no side effects), so no
# monkeypatching/teardown is required; each call leaves no state behind.
#
# Coverage notes:
#   * line 3 (import math) and the nested is_prime definition: executed on
#     every call.
#   * lines 6-7 (p < 2 -> False): exercised because the first appended
#     Fibonacci value is 1, which is rejected by is_prime.
#   * line 10 (composite -> False): exercised because composite Fibonacci
#     numbers such as 8, 21, 34, 55 are tested by is_prime before the n-th
#     prime is reached.
#   * line 11 (loop finishes with no divisor -> True): exercised for primes
#     such as 2, 3, 5, 13, 89.
#   * lines 13-18 (main loop and return): exercised by every call below.

from f039 import prime_fib


def test_prime_fib_first_is_two():
    # Walks: 1 (rejected, p < 2 branch), 2 (prime) -> returns 2.
    assert prime_fib(1) == 2


def test_prime_fib_second_is_three():
    assert prime_fib(2) == 3


def test_prime_fib_third_is_five():
    # 5 is prime and its trial-division loop (range(2, 3)) completes without
    # finding a divisor, covering the "return True" fall-through branch.
    assert prime_fib(3) == 5


def test_prime_fib_skips_composite_fibonacci_numbers():
    # 8 is Fibonacci but composite (8 % 2 == 0), so is_prime returns False
    # via the early-exit branch at line 10; the 4th prime fib is 13.
    assert prime_fib(4) == 13


def test_prime_fib_fifth_is_eighty_nine():
    # Also exercises the composite branch for 21 (21 % 3 == 0) and 34.
    assert prime_fib(5) == 89


def test_prime_fib_tenth_is_433494437():
    # Longer run: many loop iterations of the while loop and of is_prime,
    # including several composite rejections (144, 377, 610, ...).
    assert prime_fib(10) == 433494437
