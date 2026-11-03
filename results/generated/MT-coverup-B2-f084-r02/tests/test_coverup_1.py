# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f084 import solve


def test_solve():
    # solve(N) sums the digits of N and returns the binary representation
    # (without the '0b' prefix) of that sum.
    assert solve(10) == '1'        # 1 + 0 = 1  -> bin(1)  = '0b1'   -> '1'
    assert solve(99) == '10010'    # 9 + 9 = 18 -> bin(18) = '0b10010' -> '10010'
    assert solve(0) == '0'         # 0          -> bin(0)  = '0b0'    -> '0'
    assert solve(12345) == '1111'  # 1+2+3+4+5 = 15 -> bin(15) = '0b1111' -> '1111'
