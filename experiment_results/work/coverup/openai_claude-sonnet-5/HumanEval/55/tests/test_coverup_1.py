# file: script_55.py:1-14
# asked: {"lines": [10, 11, 12, 13, 14], "branches": [[10, 11], [10, 12], [12, 13], [12, 14]]}
# gained: {"lines": [10, 11, 12, 13, 14], "branches": [[10, 11], [10, 12], [12, 13], [12, 14]]}

import pytest
from script_55 import fib


def test_fib_zero():
    """Test Fibonacci of 0."""
    assert fib(0) == 0


def test_fib_one():
    """Test Fibonacci of 1."""
    assert fib(1) == 1


def test_fib_two():
    """Test Fibonacci of 2."""
    assert fib(2) == 1


def test_fib_ten():
    """Test Fibonacci of 10."""
    assert fib(10) == 55


def test_fib_eight():
    """Test Fibonacci of 8."""
    assert fib(8) == 21
