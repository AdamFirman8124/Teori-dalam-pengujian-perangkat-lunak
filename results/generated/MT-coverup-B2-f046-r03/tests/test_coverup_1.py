# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

from f046 import fib4


def test_fib4_base_cases():
    """Covers lines 3-5: list initialization and the n < 4 early-return branch."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_loop_branch():
    """Covers lines 3, 4, 7-9, 11: the loop branch for n >= 4.

    Each new value is the sum of the previous four values, starting
    from the seed sequence [0, 0, 2, 0].
    """
    assert fib4(4) == 2    # 0 + 0 + 2 + 0
    assert fib4(5) == 4    # 0 + 2 + 0 + 2
    assert fib4(6) == 8    # 2 + 0 + 2 + 4
    assert fib4(7) == 14   # 0 + 2 + 4 + 8
    assert fib4(8) == 28   # 2 + 4 + 8 + 14
