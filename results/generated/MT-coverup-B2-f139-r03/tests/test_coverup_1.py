# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

"""Tests for f139.special_factorial.

The function is pure (no I/O, no global state, no randomness), so no
monkeypatching or teardown is required; each test is self-contained and
leaves no state behind.
"""

from f139 import special_factorial


def test_special_factorial_executes_loop_body():
    # n=4 forces lines 3-8 to run, including the loop body (lines 6-7).
    # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
    assert special_factorial(4) == 288


def test_special_factorial_single_iteration():
    # n=1 executes the loop exactly once: fact_i = 1, special_fact = 1.
    assert special_factorial(1) == 1


def test_special_factorial_zero_skips_loop():
    # n=0 makes range(1, 1) empty, so the loop body is skipped and the
    # initial value is returned (covers the zero-iteration branch).
    assert special_factorial(0) == 1


def test_special_factorial_matches_factorial_product():
    # Cross-check against an independent computation of 1! * 2! * ... * n!.
    import math

    for n in range(1, 8):
        expected = math.prod(math.factorial(i) for i in range(1, n + 1))
        assert special_factorial(n) == expected
