# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_zero():
    assert solve(0) == "0"


def test_solve_single_digit():
    # 5 -> bin(5) = 0b101 -> "101"
    assert solve(5) == "101"


def test_solve_multi_digit():
    # 1+2+3=6 -> bin(6) = 0b110 -> "110"
    assert solve(123) == "110"


def test_solve_with_zeros():
    # 1+0+0+0=1 -> bin(1) = 0b1 -> "1"
    assert solve(1000) == "1"


def test_solve_large_digit_sum():
    # 9+9+9=27 -> bin(27) = 0b11011 -> "11011"
    result = solve(999)
    assert result == "11011"
    assert result == bin(27)[2:]
    assert set(result) <= {"0", "1"}
