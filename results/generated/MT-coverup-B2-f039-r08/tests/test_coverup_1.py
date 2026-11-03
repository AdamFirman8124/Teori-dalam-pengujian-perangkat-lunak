# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

"""Tests for f039.prime_fib.

The function under test is pure: it imports ``math`` locally, keeps all of
its state in local variables, performs no I/O and touches no module-level
or global state.  Therefore no monkeypatching or teardown/cleanup is
required -- each test leaves the environment exactly as it found it.

Coverage notes (lines 3-18 of f039/__init__.py):
  * line 3        : ``import math``            -> executed by every call
  * lines 5-11    : ``is_prime`` definition    -> executed by every call
  * line 6-7      : ``p < 2`` early return     -> hit via the Fibonacci value 1
  * lines 8-10    : composite detection        -> hit via 8, 21, 34, 55
  * line 11       : ``return True``            -> hit via 2, 3, 5, 13, 89
  * lines 12-14   : Fibonacci loop             -> executed by every call
  * lines 15-16   : prime counter decrement    -> hit by every n >= 1
  * lines 17-18   : loop-continue and return   -> both branches exercised
"""

import pytest

from f039 import prime_fib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),    # first prime Fibonacci number
        (2, 3),    # second prime Fibonacci number
        (3, 5),    # third prime Fibonacci number
        (4, 13),   # fourth prime Fibonacci number
        (5, 89),   # fifth prime Fibonacci number
    ],
)
def test_prime_fib_returns_nth_prime_fibonacci(n, expected):
    """prime_fib(n) must return the n-th prime in the Fibonacci sequence."""
    result = prime_fib(n)
    assert result == expected
    # Postcondition: the result itself must be a prime number.
    assert all(result % k for k in range(2, int(result ** 0.5) + 1))


def test_prime_fib_results_are_strictly_increasing():
    """Successive prime Fibonacci numbers must grow strictly monotonically."""
    results = [prime_fib(i) for i in range(1, 6)]
    assert results == sorted(results)
    assert len(set(results)) == len(results)


def test_prime_fib_is_deterministic():
    """Repeated calls with the same argument must yield the same value."""
    assert prime_fib(5) == prime_fib(5) == 89
