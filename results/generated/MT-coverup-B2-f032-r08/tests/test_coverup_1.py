# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

"""Tests for f032.find_zero, covering the previously unexecuted lines 11-21.

find_zero and poly are pure functions (they touch no module state, files or
globals), so no monkeypatching/teardown is needed to avoid state pollution.
"""

from f032 import find_zero, poly


def test_find_zero_widens_interval_then_bisects_else_branch():
    """poly(x) = 2 + x has its root at x = -2, outside [-1, 1].

    poly(-1) = 1 and poly(1) = 3 share a sign, so the widening loop
    (lines 13-14) executes once before bisection starts. During bisection
    poly(begin) == poly(-2) == 0, so every step takes the else-branch
    (line 20) and `begin` remains at the exact root -2.
    """
    xs = [2.0, 1.0]
    result = find_zero(xs)
    assert abs(result - (-2.0)) < 1e-9
    assert abs(poly(xs, result)) < 1e-9


def test_find_zero_bisection_if_branch_moves_begin():
    """poly(x) = x - 1 has its root at x = 1, an endpoint of [-1, 1].

    poly(-1) = -2 and poly(1) = 0 already bracket the root, so the widening
    loop is skipped, and every bisection step takes the if-branch (line 18),
    moving `begin` up towards the root while `end` stays at 1.
    """
    xs = [-1.0, 1.0]
    result = find_zero(xs)
    assert abs(result - 1.0) <= 1e-9
    assert abs(poly(xs, result)) < 1e-9


def test_find_zero_widens_interval_twice_and_uses_both_branches():
    """poly(x) = x + 3 has its root at x = -3.

    Both [-1, 1] and [-2, 2] have same-sign endpoints, so the widening loop
    runs twice (lines 13-14 twice); the subsequent bisection exercises both
    the if- and the else-branch before converging onto -3.
    """
    xs = [3.0, 1.0]
    result = find_zero(xs)
    assert abs(result - (-3.0)) < 1e-9
    assert abs(poly(xs, result)) < 1e-9
