# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    # Executes line 3: the return statement.
    # 1 + 0 = 1 -> bin(1) = '0b1' -> '1'
    assert solve(10) == "1"
    # 9 + 9 = 18 -> bin(18) = '0b10010' -> '10010'
    assert solve(99) == "10010"
    # 1 + 2 + 3 + 4 + 5 = 15 -> bin(15) = '0b1111' -> '1111'
    assert solve(12345) == "1111"


def test_solve_zero():
    # Edge case: sum of digits of 0 is 0 -> bin(0) = '0b0' -> '0'
    assert solve(0) == "0"


def test_solve_single_digit():
    # Single digit N: binary of the digit itself
    assert solve(7) == "111"
    assert solve(1) == "1"


def test_solve_result_is_binary_string():
    result = solve(8888)  # 8*4 = 32 -> bin(32) = '0b100000'
    assert result == "100000"
    assert set(result) <= {"0", "1"}
