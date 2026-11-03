# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

"""Tests for f032.find_zero — covering lines 11-21 and both branches of line 17.

poly(xs, x) evaluates the polynomial sum(coeff * x**i), so:
  - [1.0, 2.0]        -> 1 + 2x,   zero at -0.5 (inside [-1, 1])
  - [-2.0, 1.0]       -> -2 + x,   zero at 2.0  (outside [-1, 1], doubling loop runs once)
  - [-10.0, 1.0]      -> -10 + x,  zero at 10.0 (doubling loop runs several times)
"""

import math

import pytest

from f032 import find_zero, poly


def test_find_zero_linear_inside_interval():
    """Zero inside the initial [-1, 1] bracket: doubling loop is skipped,
    and both the if-branch (line 18) and else-branch (line 20) of the
    bisection loop are exercised."""
    xs = [1.0, 2.0]  # 1 + 2x = 0  =>  x = -0.5
    result = find_zero(xs)
    assert isinstance(result, float)
    assert abs(result - (-0.5)) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_zero_outside_interval():
    """Zero outside [-1, 1]: the doubling loop (lines 13-14) runs once to
    re-bracket, then bisection converges to the root."""
    xs = [-2.0, 1.0]  # -2 + x = 0  =>  x = 2.0
    result = find_zero(xs)
    assert abs(result - 2.0) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_zero_far_outside_interval():
    """Zero far outside [-1, 1]: the doubling loop (lines 13-14) runs several
    times, and the else-branch (line 20) of the bisection loop is exercised."""
    xs = [-10.0, 1.0]  # -10 + x = 0  =>  x = 10.0
    result = find_zero(xs)
    assert abs(result - 10.0) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_quadratic_root_at_zero():
    """Quadratic with a root at 0 inside the bracket: doubling loop skipped,
    bisection converges to the root in [begin, end]."""
    xs = [0.0, -1.0, 1.0]  # x^2 - x = x(x - 1), root at x = 0
    result = find_zero(xs)
    assert abs(result) < 1e-6
    assert abs(poly(xs, result)) < 1e-6
