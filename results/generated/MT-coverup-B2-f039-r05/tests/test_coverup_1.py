# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

"""Tests for f039.prime_fib.

The function under test is pure (no I/O, no module-level mutable state), so no
monkeypatching/teardown is required; every test leaves no state behind.

Coverage notes (lines 3-18 of f039/__init__.py):
- line 3  (`import math`)            : executed on every call.
- lines 6-7 (`p < 2 -> False`)       : hit via is_prime(1) (first appended Fib).
- line 8  (range bound)              : both sides of min() exercised
                                       (p == 2 picks p-1, p == 5 picks sqrt term).
- line 9-10 (`p % k == 0 -> False`)  : hit via composite Fibs 8, 21, 34, 55...
- line 11 (`return True`)            : hit via primes 2, 3, 5, 13, 89, ...
- lines 13-14 (loop body)            : hit on every call.
- lines 15-16 (`is_prime` True)      : hit whenever a prime Fib is appended.
- lines 17-18 (`n == 0 -> return`)   : True branch on return, False branch while
                                       the loop keeps searching.
"""

import math

import pytest

from f039 import prime_fib


def _is_prime(p: int) -> bool:
    """Independent, simple primality check used to verify results."""
    if p < 2:
        return False
    for k in range(2, math.isqrt(p) + 1):
        if p % k == 0:
            return False
    return True


def _is_fibonacci(x: int) -> bool:
    """x is a Fibonacci number iff 5*x**2 + 4 or 5*x**2 - 4 is a perfect square."""
    for candidate in (5 * x * x + 4, 5 * x * x - 4):
        root = math.isqrt(candidate)
        if root * root == candidate:
            return True
    return False


# Known n-th prime Fibonacci numbers (1-indexed).
EXPECTED = {
    1: 2,           # empty divisor range (min() picks p - 1)
    2: 3,           # min() picks the sqrt term; range still empty
    3: 5,
    4: 13,          # forces is_prime(8) -> composite -> early `return False`
    5: 89,          # forces a multi-iteration divisor loop ending in True
    6: 233,
    7: 1597,
    8: 28657,
    9: 514229,
    10: 433494437,
}


@pytest.mark.parametrize("n, expected", sorted(EXPECTED.items()))
def test_prime_fib_known_values(n, expected):
    """prime_fib returns the n-th prime Fibonacci number (covers lines 3-18)."""
    result = prime_fib(n)
    assert result == expected
    # Postconditions: the result really is a prime Fibonacci number.
    assert _is_prime(result), f"{result} is not prime"
    assert _is_fibonacci(result), f"{result} is not a Fibonacci number"


def test_prime_fib_returns_nth_prime_in_order():
    """The result is exactly the n-th prime encountered in the Fibonacci sequence."""
    n = 6
    result = prime_fib(n)
    count = 0
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if _is_prime(f[-1]):
            count += 1
            if f[-1] >= result:
                break
    assert f[-1] == result
    assert count == n


def test_prime_fib_skips_composite_fibonacci_numbers():
    """Composite Fibonacci numbers between primes must never be returned."""
    result = prime_fib(4)
    assert result == 13
    for composite in (1, 8, 21, 34, 55):
        assert not _is_prime(composite)
        assert composite != result


def test_prime_fib_zero_returns_first_appended_value():
    """With n == 0 the loop returns the first appended value (1) immediately,
    because 1 is not prime and the `n == 0` check fires on the first pass."""
    assert prime_fib(0) == 1
