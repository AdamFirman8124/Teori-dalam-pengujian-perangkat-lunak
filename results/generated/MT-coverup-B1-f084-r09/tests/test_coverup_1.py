# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_returns_binary_digit_sum():
    assert solve(123) == "110"
