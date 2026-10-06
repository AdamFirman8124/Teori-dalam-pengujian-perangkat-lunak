# file: script_39.py:1-30
# asked: {"lines": [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22], [25, 26], [27, 28], [27, 29], [29, 25], [29, 30]]}
# gained: {"lines": [15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22], [25, 26], [27, 28], [27, 29], [29, 25], [29, 30]]}

import pytest
from script_39 import prime_fib


def test_prime_fib_first():
    """Test that the first prime fibonacci number is 2."""
    assert prime_fib(1) == 2


def test_prime_fib_second():
    """Test that the second prime fibonacci number is 3."""
    assert prime_fib(2) == 3


def test_prime_fib_third():
    """Test that the third prime fibonacci number is 5."""
    assert prime_fib(3) == 5


def test_prime_fib_fourth():
    """Test that the fourth prime fibonacci number is 13."""
    assert prime_fib(4) == 13


def test_prime_fib_fifth():
    """Test that the fifth prime fibonacci number is 89."""
    assert prime_fib(5) == 89
