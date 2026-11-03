# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly


def test_find_zero_doubles_bounds_then_bisects():
    """Root at x=3 lies outside [-1, 1] and poly has the same sign at both
    initial bounds, so the doubling loop (lines 13-14) must run before
    bisection starts.  During bisection both the 'begin = center' branch
    (line 18) and the 'end = center' branch (line 20) are taken."""
    # poly(x) = -3 + x - 3x^2 + x^3 = (x - 3)(x^2 + 1); single real root at 3.
    xs = [-3, 1, -3, 1]

    # Precondition driving the doubling loop: same sign at -1 and 1.
    assert poly(xs, -1.0) * poly(xs, 1.0) > 0

    result = find_zero(xs)

    # Postconditions: the returned point is (within bisection tolerance) the root.
    assert abs(result - 3.0) < 1e-8
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_bisects_within_initial_bounds():
    """Root at x=0.5 lies inside [-1, 1] with opposite signs at the bounds,
    so the doubling loop is skipped (false branch of line 12) and bisection
    exercises both update branches before returning."""
    # poly(x) = -0.5 + x - 0.5x^2 + x^3 = (x - 0.5)(x^2 + 1); root at 0.5.
    xs = [-0.5, 1, -0.5, 1]

    # Precondition: opposite signs at the initial bounds -> no doubling.
    assert poly(xs, -1.0) * poly(xs, 1.0) <= 0

    result = find_zero(xs)

    # Postconditions: the returned point is (within bisection tolerance) the root.
    assert abs(result - 0.5) < 1e-8
    assert abs(poly(xs, result)) < 1e-6
