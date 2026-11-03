# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

"""Tests for f039.prime_fib — the n-th Fibonacci number that is also prime.

These tests execute every line and branch of prime_fib (lines 3-18):

- n=1 drives the loop through f[-1] == 1, exercising the ``p < 2`` early
  return of the inner ``is_prime`` helper, then hits p == 2 where the
  trial-division ``for`` loop range is empty and ``is_prime`` returns True,
  and finally returns via the ``n == 0`` branch.
- n=2..4 exercise the non-empty trial-division loop for primes (5, 13)
  where ``p % k != 0`` for every candidate k.
- n=5 exercises the composite branch of ``is_prime`` (the Fibonacci numbers
  8, 21, 34 and 55 are generated and rejected before 89 is returned).
- Larger n values exercise additional loop iterations of the outer loop.

prime_fib is a pure function (no module state, no I/O, no monkeypatching
targets), so no cleanup/teardown is required and none of the tests leak
state.
"""

import pytest

from f039 import prime_fib


def test_prime_fib_first_prime_fibonacci_is_two():
    # Covers: import math, is_prime's p < 2 branch (p == 1), the empty
    # trial-division loop for p == 2, and the n == 0 return.
    assert prime_fib(1) == 2


def test_prime_fib_second_prime_fibonacci_is_three():
    assert prime_fib(2) == 3


def test_prime_fib_third_prime_fibonacci_is_five():
    # p == 5 runs the trial-division loop with k == 2 (5 % 2 != 0).
    assert prime_fib(3) == 5


def test_prime_fib_fourth_prime_fibonacci_is_thirteen():
    # p == 13 runs the trial-division loop with k in {2, 3}.
    assert prime_fib(4) == 13


def test_prime_fib_fifth_prime_fibonacci_is_eighty_nine():
    # Covers the composite branch of is_prime: 8, 21, 34 and 55 are all
    # rejected via ``p % k == 0`` before 89 is returned.
    assert prime_fib(5) == 89


@pytest.mark.parametrize(
    "n, expected",
    [
        (6, 233),
        (7, 1597),
        (8, 28657),
        (9, 514229),
        (10, 433494437),
    ],
)
def test_prime_fib_larger_known_values(n, expected):
    # Exercises many more iterations of the outer while loop, mixing prime
    # and composite Fibonacci candidates.
    assert prime_fib(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 13),
        (5, 89),
        (6, 233),
        (7, 1597),
        (8, 28657),
        (9, 514229),
        (10, 433494437),
    ],
)
def test_prime_fib_result_is_prime_and_fibonacci(n, expected):
    # Postcondition checks: the returned value must be prime and must
    # appear in the Fibonacci sequence, in addition to matching the
    # known expected value.
    result = prime_fib(n)

    assert result == expected
    assert result >= 2
    assert all(result % k for k in range(2, int(result ** 0.5) + 1))

    a, b = 0, 1
    while a < result:
        a, b = b, a + b
    assert a == result
