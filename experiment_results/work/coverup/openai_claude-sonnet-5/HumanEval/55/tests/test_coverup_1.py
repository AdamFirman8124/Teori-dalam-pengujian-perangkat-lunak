# file: script_55.py:1-14
# asked: {"lines": [10, 11, 12, 13, 14], "branches": [[10, 11], [10, 12], [12, 13], [12, 14]]}
# gained: {"lines": [10, 11, 12, 13, 14], "branches": [[10, 11], [10, 12], [12, 13], [12, 14]]}

import pytest
from script_55 import fib


def test_fib_zero():
    assert fib(0) == 0


def test_fib_one():
    assert fib(1) == 1


def test_fib_two():
    assert fib(2) == 1


def test_fib_ten():
    assert fib(10) == 55


def test_fib_eight():
    assert fib(8) == 21
