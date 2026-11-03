# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

"""Tests for f039.prime_fib.

The function is pure (no I/O, no module-level mutable state), so no
monkeypatching/teardown is required; each call is fully self-contained.
These tests drive every line and branch of prime_fib, including:

  * line 3 (import math) and the nested is_prime definition (line 5)
  * the `p < 2` early-return branch (p == 1 on the first Fibonacci append)
  * the trial-division loop with an empty range (p == 2, p == 3)
  * the `p % k == 0` -> return False branch (composite Fibonacci numbers
    such as 8, 21, 34, 144, 377, ...)
  * the loop-exhaustion -> return True branch (primes such as 5, 13, 89)
  * both outcomes of `if is_prime(f[-1])` and of `if n == 0`
"""

import pytest

from f039 import prime_fib


def test_prime_fib_first_prime_is_two():
    # Drives: import math, is_prime(1) -> p < 2 branch, is_prime(2) with an
    # empty trial-division range, n reaching 0 -> return f[-1].
    assert prime_fib(1) == 2


def test_prime_fib_second_prime_is_three():
    # is_prime(3) also exercises the empty-range path of the for loop.
    assert prime_fib(2) == 3


def test_prime_fib_third_prime_is_five():
    # is_prime(5) exercises the for loop running to completion (no divisor
    # found) before returning True.
    assert prime_fib(3) == 5


def test_prime_fib_fourth_prime_is_thirteen():
    # is_prime(8) exercises the `p % k == 0` -> return False branch.
    assert prime_fib(4) == 13


def test_prime_fib_fifth_prime_is_eighty_nine():
    # Composites 8, 21, 34 hit the divisor branch; 89 exercises a longer
    # successful trial-division loop.
    assert prime_fib(5) == 89


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
    ],
)
def test_prime_fib_known_values(n, expected):
    # Larger n values force many loop iterations, covering both the
    # prime (n -= 1) and composite (continue) outcomes of is_prime,
    # plus repeated False evaluations of `if n == 0` before the final True.
    assert prime_fib(n) == expected


def test_prime_fib_results_are_prime():
    # Postcondition: every returned value must actually be prime.
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(p ** 0.5) + 1):
            if p % k == 0:
                return False
        return True

    for n in range(1, 7):
        result = prime_fib(n)
        assert is_prime(result), f"prime_fib({n}) = {result} is not prime"
