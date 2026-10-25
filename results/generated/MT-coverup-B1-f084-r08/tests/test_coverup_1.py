# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    assert solve(123) == "110"  # 1+2+3 = 6 -> 0b110


def test_solve_single_digit():
    assert solve(7) == "111"  # 7 -> 0b111


def test_solve_zero():
    assert solve(0) == "0"  # 0 -> 0b0


def test_solve_trailing_zero_digit():
    assert solve(10) == "1"  # 1+0 = 1 -> 0b1


def test_solve_large_number():
    assert solve(9999) == "100100"  # 36 -> 0b100100
