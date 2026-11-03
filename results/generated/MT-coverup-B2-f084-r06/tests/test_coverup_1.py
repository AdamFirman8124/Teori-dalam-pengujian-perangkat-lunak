# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    # Digit sum of 10 is 1 -> binary '1'
    assert solve(10) == "1"
    # Digit sum of 123 is 6 -> binary '110'
    assert solve(123) == "110"
    # Digit sum of 99 is 18 -> binary '10010'
    assert solve(99) == "10010"
    # Digit sum of 0 is 0 -> binary '0'
    assert solve(0) == "0"
