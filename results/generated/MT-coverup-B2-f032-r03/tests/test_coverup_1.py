# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

from f032 import find_zero, poly


def test_find_zero_no_expansion_interior_covers_both_branches():
    # xs = x -> zero at 0, poly(-1)*poly(1) < 0 so no expansion
    xs = [0.0, 1.0]
    result = find_zero(xs)
    assert abs(result - 0.0) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expansion_positive_root():
    # xs = x - 5 -> zero at 5, poly(-1)*poly(1) > 0 so expansion loop runs
    xs = [-5.0, 1.0]
    assert poly(xs, -1.0) * poly(xs, 1.0) > 0
    result = find_zero(xs)
    assert abs(result - 5.0) < 1e-6
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expansion_negative_root():
    # xs = x + 5 -> zero at -5, poly(-1)*poly(1) > 0 so expansion loop runs
    xs = [5.0, 1.0]
    assert poly(xs, -1.0) * poly(xs, 1.0) > 0
    result = find_zero(xs)
    assert abs(result - (-5.0)) < 1e-6
    assert abs(poly(xs, result)) < 1e-6
