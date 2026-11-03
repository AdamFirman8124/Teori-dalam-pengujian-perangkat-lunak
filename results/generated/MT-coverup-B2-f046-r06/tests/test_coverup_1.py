# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

from f046 import fib4


def test_fib4_base_cases():
    """Covers lines 3-5: list initialization and the 'n < 4' early-return branch."""
    # Each base case exercises the True branch of 'if n < 4'
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_iterative_cases():
    """Covers lines 7-11: the False branch of 'if n < 4', the loop body, and the final return."""
    # n == 4: loop runs exactly once
    assert fib4(4) == 2
    # n > 4: loop runs multiple times, exercising append/pop repeatedly
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 54
    assert fib4(10) == 104
