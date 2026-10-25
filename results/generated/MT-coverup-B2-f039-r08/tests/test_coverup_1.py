# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

import pytest

from f039 import prime_fib


def test_prime_fib_first():
    """Covers the full happy path: import, is_prime, loop, decrement, return."""
    assert prime_fib(1) == 2


def test_prime_fib_small_values():
    """Each call exercises is_prime's True branch and the n == 0 return."""
    expected = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437]
    for i, value in enumerate(expected, start=1):
        assert prime_fib(i) == value


def test_prime_fib_is_prime_composite_branch():
    """
    Covers the composite branch of is_prime (line 10: return False).
    Fibonacci numbers 4, 6, 8, 9, 12, ... are composite and get rejected
    before the next prime is counted.
    """
    # prime_fib(4) == 13 means composites 4, 6, 8, 9, 12 were skipped.
    assert prime_fib(4) == 13


def test_prime_fib_is_prime_small_p_branch():
    """
    Covers the p < 2 branch of is_prime (line 7: return False).
    The first appended Fibonacci number is 1, which is < 2, so is_prime(1)
    returns False on the very first loop iteration for every call.
    """
    assert prime_fib(1) == 2


def test_prime_fib_result_is_prime():
    """Postcondition: every returned value is a prime Fibonacci number."""
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(p ** 0.5) + 1):
            if p % k == 0:
                return False
        return True

    fibs = [0, 1]
    for _ in range(30):
        fibs.append(fibs[-1] + fibs[-2])

    prime_fibs = [x for x in fibs if is_prime(x)]
    for i in range(1, 8):
        result = prime_fib(i)
        assert result in prime_fibs
        assert is_prime(result)
