# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

import pytest

from f039 import prime_fib


def test_prime_fib_first():
    """Covers the full happy path: import, is_prime, loop, decrement, return."""
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89


def test_prime_fib_larger():
    """Exercises more loop iterations and the composite-skip branch of is_prime."""
    assert prime_fib(6) == 233
    assert prime_fib(7) == 1597
    assert prime_fib(8) == 28657
    assert prime_fib(9) == 514229
    assert prime_fib(10) == 433494437


def test_prime_fib_results_are_prime():
    """Postcondition: every returned value is a prime number."""
    def _is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(p ** 0.5) + 1):
            if p % k == 0:
                return False
        return True

    for n in range(1, 11):
        result = prime_fib(n)
        assert _is_prime(result), f"prime_fib({n}) = {result} is not prime"


def test_prime_fib_strictly_increasing():
    """Postcondition: the sequence of prime Fibonacci numbers is strictly increasing."""
    values = [prime_fib(n) for n in range(1, 11)]
    assert all(a < b for a, b in zip(values, values[1:]))
