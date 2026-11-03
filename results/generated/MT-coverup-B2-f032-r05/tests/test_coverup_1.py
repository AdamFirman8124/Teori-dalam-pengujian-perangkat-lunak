# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

from f032 import find_zero, poly


def test_find_zero_root_inside_initial_interval():
    """Root x = 0.3 lies inside [-1, 1], so poly(xs, -1) * poly(xs, 1) < 0:
    the interval-doubling loop body is skipped, and the bisection loop
    exercises both branches (begin = center and end = center)."""
    xs = [-0.3, 1]  # poly(x) = x - 0.3, poly(-1) = -1.3, poly(1) = 0.7
    result = find_zero(xs)
    assert isinstance(result, float)
    # Bisection terminates when the bracket is narrower than 1e-10 and the
    # root stays inside the bracket, so the result is within 1e-10 of 0.3.
    assert abs(result - 0.3) < 1e-8
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expands_interval_before_bisecting():
    """poly(+-1) are both positive here, so poly(xs, begin) * poly(xs, end) > 0
    initially: the doubling loop body (lines 13-14) runs until the endpoints
    have opposite signs, then bisection (both branches) locates the root -3."""
    xs = [3, 1]  # poly(x) = x + 3; poly(-1) = 2, poly(1) = 4 -> interval doubles
    result = find_zero(xs)
    assert isinstance(result, float)
    assert abs(result + 3.0) < 1e-8
    assert abs(poly(xs, result)) < 1e-6
