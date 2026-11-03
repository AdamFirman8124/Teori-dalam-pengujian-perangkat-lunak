# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

"""Tests for f039.prime_fib.

prime_fib(n) returns the n-th Fibonacci number that is also prime.
Calling it drives every line/branch of the implementation:

  * is_prime(1)          -> hits the ``p < 2`` early-return branch (lines 6-7)
  * is_prime(2)          -> empty ``range`` in the for-loop, falls to ``return True``
                            (line 11) and exercises ``min(..., p - 1)`` picking ``p - 1``
  * is_prime(5)          -> loop body runs, no divisor found, falls to ``return True``
                            (lines 8-11) and exercises ``min(...)`` picking ``sqrt + 1``
  * is_prime(8)/is_prime(21) -> loop body runs and returns False via ``p % k == 0``
                            (lines 9-10)
  * the outer while-loop, ``n -= 1`` and ``return f[-1]`` (lines 13-18)

The function is pure (no I/O, no module state), so no monkeypatching/cleanup
is required.
"""

import pytest

from f039 import prime_fib

# The first ten Fibonacci numbers that are prime, in order.
PRIME_FIBS = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437]


def test_prime_fib_first_five_covers_all_branches():
    # n=1: is_prime(1) -> p < 2 branch; is_prime(2) -> empty range -> True.
    # n=3: is_prime(5) -> loop runs, no divisor -> True.
    # n=4: is_prime(8) -> loop finds divisor 2 -> False.
    # n=5: is_prime(21) -> loop finds divisor 3 -> False; is_prime(89) -> True.
    for n, expected in enumerate(PRIME_FIBS[:5], start=1):
        assert prime_fib(n) == expected


def test_prime_fib_larger_values():
    for n, expected in enumerate(PRIME_FIBS[5:], start=6):
        assert prime_fib(n) == expected


def test_prime_fib_results_are_prime_fibonacci_numbers():
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(p ** 0.5) + 1):
            if p % k == 0:
                return False
        return True

    fibs = [0, 1]
    while fibs[-1] <= PRIME_FIBS[-1]:
        fibs.append(fibs[-1] + fibs[-2])
    fib_set = set(fibs)

    for n in range(1, len(PRIME_FIBS) + 1):
        result = prime_fib(n)
        assert is_prime(result), f"prime_fib({n}) = {result} is not prime"
        assert result in fib_set, f"prime_fib({n}) = {result} is not a Fibonacci number"
        assert result == PRIME_FIBS[n - 1]


def test_prime_fib_is_monotonic():
    results = [prime_fib(n) for n in range(1, 8)]
    assert results == sorted(results)
    assert len(set(results)) == len(results)
