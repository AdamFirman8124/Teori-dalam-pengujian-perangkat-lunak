# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_zero():
    # sum of digits of 0 is 0 -> bin(0)[2:] == '0'
    assert solve(0) == '0'


def test_solve_single_digit():
    # sum of digits of 5 is 5 -> bin(5)[2:] == '101'
    assert solve(5) == '101'


def test_solve_multi_digit():
    # sum of digits of 10 is 1 -> bin(1)[2:] == '1'
    assert solve(10) == '1'
    # sum of digits of 123 is 6 -> bin(6)[2:] == '110'
    assert solve(123) == '110'


def test_solve_large_number():
    # sum of digits of 999 is 27 -> bin(27)[2:] == '11011'
    assert solve(999) == '11011'
