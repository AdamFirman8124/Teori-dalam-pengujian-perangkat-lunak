# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly


def test_find_zero_root_to_the_right_expands_interval_and_bisects():
    # poly(x) = x - 2 has its only root at x = 2, outside the initial [-1, 1]
    # interval. poly(-1) * poly(1) = (-3) * (-1) > 0, so the doubling loop
    # (lines 12-14) executes, and during bisection poly(center) * poly(begin)
    # > 0 holds, exercising the `begin = center` branch (line 18).
    xs = [-2.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(2.0, abs=1e-6)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-6)
    # The returned point must lie in the final (tiny) bracketing interval.
    assert -4.0 <= result <= 4.0


def test_find_zero_root_to_the_left_expands_interval_and_takes_else_branch():
    # poly(x) = x + 2 has its only root at x = -2, outside [-1, 1].
    # poly(-1) * poly(1) = 1 * 3 > 0, so the doubling loop (lines 12-14) runs;
    # afterwards poly(center) * poly(begin) == 0 (poly(begin) == 0), so the
    # `else: end = center` branch (line 20) is exercised.
    xs = [2.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(-2.0, abs=1e-6)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-6)


def test_find_zero_root_inside_initial_interval_skips_expansion():
    # poly(x) = x - 0.5 has its root inside [-1, 1]; poly(-1) * poly(1)
    # = (-1.5) * 0.5 < 0, so the doubling loop is skipped and only the
    # bisection loop (lines 15-20) runs, covering both of its branches.
    xs = [-0.5, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(0.5, abs=1e-6)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-6)
