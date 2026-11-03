# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    # Digit sum of 123 is 6 -> binary '110'
    assert solve(123) == "110"
    # Digit sum of 999 is 27 -> binary '11011'
    assert solve(999) == "11011"
    # Digit sum of 1000000 is 1 -> binary '1'
    assert solve(1000000) == "1"


def test_solve_zero():
    # Edge case: digit sum of 0 is 0, bin(0)[2:] is '0'
    assert solve(0) == "0"
