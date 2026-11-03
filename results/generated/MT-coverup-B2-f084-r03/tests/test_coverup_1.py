# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve_returns_binary_of_digit_sum_without_prefix():
    # Each call executes line 3 (the return statement).
    # Digit sum of 10 is 1 -> bin(1)[2:] == '1'
    assert solve(10) == "1"
    # Digit sum of 99 is 18 -> bin(18)[2:] == '10010'
    assert solve(99) == "10010"
    # Digit sum of 0 is 0 -> bin(0)[2:] == '0'
    assert solve(0) == "0"
    # Digit sum of 12345 is 15 -> bin(15)[2:] == '1111'
    assert solve(12345) == "1111"
    # Generic consistency check: result equals binary of digit sum, prefix stripped
    for n in (7, 100, 9999, 2024):
        expected = bin(sum(int(d) for d in str(n)))[2:]
        assert solve(n) == expected
        assert not expected.startswith("0b")
