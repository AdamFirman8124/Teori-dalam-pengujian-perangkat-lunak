# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest
from f032 import find_zero, poly


def test_find_zero_no_expansion_covers_both_bisection_branches():
    xs = [-0.5, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(0.5, abs=1e-7)
    assert abs(poly(xs, result)) < 1e-7
    assert abs(result - 0.5) < 1e-7


def test_find_zero_requires_single_expansion():
    xs = [-2.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(2.0, abs=1e-7)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_requires_multiple_expansions():
    xs = [-10.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(10.0, abs=1e-7)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_negative_side_expansion():
    xs = [2.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(-2.0, abs=1e-7)
    assert abs(poly(xs, result)) < 1e-6
