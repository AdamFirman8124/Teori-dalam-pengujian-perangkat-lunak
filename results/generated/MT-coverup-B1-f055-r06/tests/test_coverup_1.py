# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

from f055 import fib


def test_fib_zero():
    assert fib(0) == 0


def test_fib_one():
    assert fib(1) == 1


def test_fib_recursive():
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(10) == 55
