# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest
from f032 import find_zero, poly


def test_find_zero_no_expansion_brackets_immediately():
    # poly(x) = x, root at 0: poly(-1)*poly(1) = -1 <= 0, so no expansion
    xs = [0.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(0.0, abs=1e-6)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expansion_negative_root():
    # poly(x) = 10 + x, root at -10: needs several doublings of [-1,1]
    # covers begin *= 2.0 and end *= 2.0 loop body
    xs = [10.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(-10.0, abs=1e-6)
    assert abs(poly(xs, result)) < 1e-6


def test_find_zero_expansion_positive_root():
    # poly(x) = -10 + x, root at 10: needs expansion the other way
    # bisection exercises both begin=center and end=center branches
    xs = [-10.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(10.0, abs=1e-6)
    assert abs(poly(xs, result)) < 1e-6
