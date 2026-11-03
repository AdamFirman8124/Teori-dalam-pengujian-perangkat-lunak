# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly

# Both find_zero and poly are pure functions (no I/O, no globals mutated),
# so no monkeypatching/cleanup is required; each test is self-contained.


def test_find_zero_expands_interval_then_bisects_to_root():
    # xs represents x**3 - 2, whose positive root is 2**(1/3) ~ 1.2599.
    # poly(-1) * poly(1) == (-3) * (-1) == 3 > 0, so the doubling loop
    # (lines 12-14) must run until [-2**k, 2**k] brackets the root; the
    # bisection loop (lines 15-18, 20-21) then converges onto it.
    xs = [-2, 0, 0, 1]
    result = find_zero(xs)
    # The bisection never moves an endpoint outside the current bracket, so
    # a result beyond the initial [-1, 1] proves the doubling loop executed.
    assert result > 1.0
    assert result == pytest.approx(2 ** (1 / 3), abs=1e-6)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_skips_expansion_and_takes_else_branch():
    # xs represents x**2 - 1.  poly(-1) == poly(1) == 0, so their product is
    # 0 and the doubling loop is skipped immediately (line 12 false branch).
    # Since poly(begin) == 0 throughout, every bisection step takes the else
    # branch (line 20): `end` converges onto the root at -1 while `begin`
    # never moves, so the returned value is exactly -1.0 (line 21).
    xs = [-1, 0, 1]
    result = find_zero(xs)
    assert result == pytest.approx(-1.0, abs=1e-9)
    assert abs(poly(xs, result)) < 1e-8


def test_find_zero_bracketed_at_start_converges_to_zero():
    # xs represents x.  poly(-1) * poly(1) == -1 <= 0, so no expansion is
    # needed (line 12 false branch).  The first bisection step hits the else
    # branch (end = 0) and subsequent steps hit the true branch of line 17
    # (begin = center), converging to the root at 0 from below.
    xs = [0, 1]
    result = find_zero(xs)
    assert -1.1e-10 <= result <= 0.0
    assert abs(poly(xs, result)) < 1e-9
