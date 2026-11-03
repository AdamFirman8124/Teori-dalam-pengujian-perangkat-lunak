# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import f032
from f032 import find_zero


def test_find_zero_expands_interval_then_bisects(monkeypatch):
    """poly(x) = x**3 - 2 has its root at 2**(1/3) ~ 1.26, outside [-1, 1].

    This forces the interval-expansion loop (lines 13-14) to run before the
    bisection loop converges, exercising every line (11-21) and both branches
    of both while loops and of the if/else statement.
    """
    xs = [-2.0, 0.0, 0.0, 1.0]
    original_poly = f032.poly
    calls = []

    def spying_poly(xs_arg, x):
        calls.append(x)
        return original_poly(xs_arg, x)

    # Patch is automatically undone by monkeypatch after the test.
    monkeypatch.setattr(f032, "poly", spying_poly)

    result = find_zero(xs)

    # The first two evaluations probe the initial interval [-1, 1]; the next
    # two prove the expansion loop body ran, widening the interval to [-2, 2]
    # where the endpoint signs finally differ.
    assert calls[:4] == [-1.0, 1.0, -2.0, 2.0]

    root = 2.0 ** (1.0 / 3.0)
    # The expansion was necessary: the answer lies outside the initial [-1, 1].
    assert result > 1.0
    # Bisection keeps the root inside [begin, end], whose width is <= 1e-10
    # when the loop exits, so `begin` must be within 1e-10 of the root.
    assert abs(result - root) <= 1e-9
    assert abs(original_poly(xs, result)) < 1e-8


def test_find_zero_bisects_without_expansion(monkeypatch):
    """poly(x) = x - 1 already has its root at 1.0 on the boundary of [-1, 1]
    (poly(-1) = -2, poly(1) = 0), so the expansion loop body must never run;
    only the bisection loop executes and converges."""
    xs = [-1.0, 1.0]
    original_poly = f032.poly
    calls = []

    def spying_poly(xs_arg, x):
        calls.append(x)
        return original_poly(xs_arg, x)

    # Patch is automatically undone by monkeypatch after the test.
    monkeypatch.setattr(f032, "poly", spying_poly)

    result = find_zero(xs)

    # Every evaluation stayed inside the initial interval: no expansion happened.
    assert calls
    assert min(calls) >= -1.0
    assert max(calls) <= 1.0

    # `begin` approaches the root at 1.0 strictly from below, and the final
    # interval width is at most 1e-10.
    assert result < 1.0
    assert abs(result - 1.0) <= 1e-9
    assert abs(original_poly(xs, result)) < 1e-8
