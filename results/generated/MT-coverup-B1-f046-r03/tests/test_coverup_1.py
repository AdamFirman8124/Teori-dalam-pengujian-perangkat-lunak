# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_first_loop_iteration():
    # n == 4 exercises the loop body exactly once and the final return
    assert fib4(4) == 2


def test_fib4_multiple_loop_iterations():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28


def test_fib4_matches_reference_implementation():
    def reference(n: int) -> int:
        seq = [0, 0, 2, 0]
        if n < 4:
            return seq[n]
        for _ in range(4, n + 1):
            seq.append(sum(seq[-4:]))
        return seq[-1]

    for n in range(0, 20):
        assert fib4(n) == reference(n)


def test_fib4_does_not_leak_state_between_calls():
    first = fib4(10)
    assert fib4(4) == 2
    assert fib4(10) == first
