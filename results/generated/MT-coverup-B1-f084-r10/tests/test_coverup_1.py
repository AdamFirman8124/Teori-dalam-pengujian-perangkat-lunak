# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_single_digit():
    assert solve(0) == "0"
    assert solve(5) == bin(5)[2:]
    assert solve(8) == "1000"


def test_solve_multi_digit():
    assert solve(10) == "1"
    assert solve(123) == "110"
    assert solve(999) == "11011"


def test_solve_larger_value():
    assert solve(1000) == "1"
    assert solve(123456789) == bin(45)[2:]
    assert solve(15) == bin(6)[2:]
