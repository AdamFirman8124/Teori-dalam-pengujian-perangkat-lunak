# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_zero():
    assert solve(0) == "0"


def test_solve_single_digit():
    assert solve(5) == bin(5)[2:]


def test_solve_multi_digit():
    # 1 + 2 + 3 = 6 -> bin(6) = '0b110' -> '110'
    assert solve(123) == "110"


def test_solve_sum_needs_multi_bit():
    # 1 + 9 = 10 -> bin(10) = '0b1010' -> '1010'
    assert solve(19) == "1010"


def test_solve_large_number():
    # 9 + 9 + 9 = 27 -> bin(27) = '0b11011' -> '11011'
    assert solve(999) == "11011"
