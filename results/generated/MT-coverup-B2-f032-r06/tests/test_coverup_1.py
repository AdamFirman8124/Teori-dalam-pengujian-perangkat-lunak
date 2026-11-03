# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

"""Tests for f032.find_zero, covering the previously unexecuted lines 11-21.

poly(xs, x) evaluates the polynomial whose coefficients are xs, i.e.
xs[0] + xs[1]*x + xs[2]*x**2 + ...

find_zero is a pure function (no I/O, no module state is touched), so no
monkeypatching/teardown is required; the tests below are side-effect free.
"""

import math

from f032 import find_zero, poly


def test_find_zero_root_inside_initial_interval_covers_both_branches():
    # p(x) = -0.5 + x has its only root at x = 0.5, strictly inside [-1, 1],
    # so the sign check on line 12 is immediately false (expansion skipped).
    # First bisection step: center=0.0, p(0)*p(-1) > 0  -> begin = center (line 18).
    # Second step:        center=0.5, p(0.5)*p(0) == 0  -> end = center   (line 20).
    # Hence both branches of the if on lines 17-20 are exercised.
    xs = [-0.5, 1]
    result = find_zero(xs)
    assert abs(result - 0.5) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expands_search_interval_once():
    # p(x) = 2 + x has its only root at x = -2, outside [-1, 1].
    # p(-1) = 1 and p(1) = 3 are both positive, so the while on line 12 is
    # true and lines 13-14 execute (interval doubles to [-2, 2], where
    # p(-2) == 0 stops the loop). Bisection then converges to -2.
    xs = [2, 1]
    result = find_zero(xs)
    assert abs(result - (-2.0)) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expands_search_interval_repeatedly():
    # p(x) = 4 + x has its only root at x = -4. Both signs agree on [-1, 1]
    # and again on [-2, 2], so lines 13-14 execute twice before
    # p(-4) == 0 ends the expansion loop.
    xs = [4, 1]
    result = find_zero(xs)
    assert abs(result - (-4.0)) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_cubic_root_at_interval_boundary():
    # p(x) = (x - 1)(x - 2)(x - 3): p(-1) = -24 and p(1) = 0, so the
    # expansion loop is skipped and the bisection loop (lines 15-21) runs,
    # taking the begin = center branch until begin converges to the root 1.
    xs = [-6, 11, -6, 1]
    result = find_zero(xs)
    assert abs(result - 1.0) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_returns_float_within_bracket():
    # Postcondition check: the returned value is a float lying in the final
    # (tiny) bracketing interval, i.e. poly is (near) zero there.
    xs = [-0.5, 1]
    result = find_zero(xs)
    assert isinstance(result, float)
    assert math.isfinite(result)
    assert abs(poly(xs, result)) < 1e-6
