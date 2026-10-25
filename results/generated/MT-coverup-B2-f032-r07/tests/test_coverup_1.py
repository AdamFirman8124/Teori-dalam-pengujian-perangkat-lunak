# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import math

import pytest

from f032 import find_zero, poly


def test_find_zero_expands_interval_and_positive_branch():
    # xs represents 2 - x^2? No: [-2, 1] represents -2 + x, root at x = 2.
    # poly(-1) = -3, poly(1) = -1 -> product > 0, so the while loop on
    # lines 12-14 must double the interval (lines 13-14 execute).
    # After doubling: poly(-2) = -4, poly(2) = 0 -> product == 0, loop exits.
    # During bisection poly(center) * poly(begin) > 0, so line 18
    # (begin = center) executes.
    xs = [-2.0, 1.0]
    result = find_zero(xs)
    # Postcondition: returned value is (numerically) the root of -2 + x = 0.
    assert math.isclose(result, 2.0, abs_tol=1e-8)
    assert math.isclose(poly(xs, result), 0.0, abs_tol=1e-6)
    # The interval invariant held: root lies within the final bracket.
    assert -4.0 <= result <= 4.0


def test_find_zero_negative_branch():
    # xs represents 2 + x, root at x = -2.
    # poly(-1) = 1, poly(1) = 3 -> product > 0, so lines 13-14 execute
    # (interval doubles to [-2, 2], where poly(-2) = 0 stops the loop).
    # In bisection, poly(begin) == 0 makes every product <= 0, so the
    # else branch on line 20 (end = center) executes.
    xs = [2.0, 1.0]
    result = find_zero(xs)
    # Postcondition: returned value is (numerically) the root of 2 + x = 0.
    assert math.isclose(result, -2.0, abs_tol=1e-8)
    assert math.isclose(poly(xs, result), 0.0, abs_tol=1e-6)
    assert -4.0 <= result <= 4.0


def test_find_zero_root_inside_initial_interval():
    # xs represents x^2 - 1? No: [-1, 0, 1] represents -1 + x^2, roots at
    # +/-1. Use [-1, 0, 1] with a sign change inside [-1, 1] instead:
    # [0, -1] represents -x, root at 0, poly(-1) = 1, poly(1) = -1,
    # product < 0 so the doubling loop body (lines 13-14) is skipped and
    # bisection runs directly, exercising both branches.
    xs = [0.0, -1.0]
    result = find_zero(xs)
    assert math.isclose(result, 0.0, abs_tol=1e-8)
    assert math.isclose(poly(xs, result), 0.0, abs_tol=1e-8)
