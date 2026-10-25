# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

from f046 import fib4


def test_fib4_n0():
    assert fib4(0) == 0


def test_fib4_n1():
    assert fib4(1) == 0


def test_fib4_n2():
    assert fib4(2) == 2


def test_fib4_n3():
    assert fib4(3) == 0


def test_fib4_n4_single_iteration():
    assert fib4(4) == 2


def test_fib4_n5_multiple_iterations():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
