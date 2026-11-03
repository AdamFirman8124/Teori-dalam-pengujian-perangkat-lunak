# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly

# find_zero/poly are pure functions (no I/O, no module state, no globals),
# so no monkeypatching/cleanup is required; each test only reads them.


def test_find_zero_bracket_doubling_needed():
    """x**3 - 2 has its root (~1.26) outside [-1, 1], so the initial bracket
    must be doubled (lines 12-14) before the bisection loop (lines 15-21)."""
    xs = [-2.0, 0.0, 0.0, 1.0]  # x**3 - 2
    result = find_zero(xs)
    expected = 2.0 ** (1.0 / 3.0)
    assert result == pytest.approx(expected, abs=1e-9)
    # postcondition: returned point is (numerically) a zero of the polynomial
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_bracket_doubling_multiple_times():
    """x**3 - 100 requires three doublings of the bracket before the sign
    change is bracketed, exercising lines 13-14 repeatedly."""
    xs = [-100.0, 0.0, 0.0, 1.0]  # x**3 - 100
    result = find_zero(xs)
    expected = 100.0 ** (1.0 / 3.0)
    assert result == pytest.approx(expected, abs=1e-9)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_negative_root():
    """x**3 + 2 has its root at ~-1.26; the bisection here takes the else
    branch (line 20) as well as the if branch (line 18)."""
    xs = [2.0, 0.0, 0.0, 1.0]  # x**3 + 2
    result = find_zero(xs)
    expected = -(2.0 ** (1.0 / 3.0))
    assert result == pytest.approx(expected, abs=1e-9)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_root_inside_initial_bracket():
    """x - 0.5 already changes sign on [-1, 1], so the doubling loop body
    (lines 13-14) must not run; bisection still converges to 0.5."""
    xs = [-0.5, 1.0]  # x - 0.5
    result = find_zero(xs)
    assert result == pytest.approx(0.5, abs=1e-9)
    assert abs(poly(xs, result)) < 1e-9


def test_find_zero_root_on_bracket_edge():
    """x - 1 gives poly(1) == 0, so the doubling loop condition is false
    immediately; the bisection converges to the bracket edge 1.0."""
    xs = [-1.0, 1.0]  # x - 1
    result = find_zero(xs)
    assert result == pytest.approx(1.0, abs=1e-9)
    assert abs(poly(xs, result)) < 1e-9
