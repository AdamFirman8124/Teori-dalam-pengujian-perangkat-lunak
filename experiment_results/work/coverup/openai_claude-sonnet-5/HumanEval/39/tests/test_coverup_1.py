# file: script_39.py:1-30
# asked: {"lines": [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22], [25, 26], [27, 28], [27, 29], [29, 25], [29, 30]]}
# gained: {"lines": [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22], [25, 26], [27, 28], [27, 29], [29, 25], [29, 30]]}

import pytest
from script_39 import prime_fib


def test_prime_fib_first():
    """Test that the first prime Fibonacci number is 2."""
    assert prime_fib(1) == 2


def test_prime_fib_second():
    """Test that the second prime Fibonacci number is 3."""
    assert prime_fib(2) == 3


def test_prime_fib_third():
    """Test that the third prime Fibonacci number is 5."""
    assert prime_fib(3) == 5


def test_prime_fib_fourth():
    """Test that the fourth prime Fibonacci number is 13."""
    assert prime_fib(4) == 13


def test_prime_fib_fifth():
    """Test that the fifth prime Fibonacci number is 89."""
    assert prime_fib(5) == 89


def test_prime_fib_sixth():
    """Test that the sixth prime Fibonacci number is 233."""
    assert prime_fib(6) == 233


def test_prime_fib_seventh():
    """Test that the seventh prime Fibonacci number is 1597."""
    assert prime_fib(7) == 1597
