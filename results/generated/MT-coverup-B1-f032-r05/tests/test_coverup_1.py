# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

from f032 import find_zero, poly


def test_find_zero_no_expansion_if_true_branch():
    # poly(x) = x - 1, root at x = 1 (endpoint, no bracket expansion)
    xs = [-1.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(1.0, abs=1e-9)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-9)


def test_find_zero_no_expansion_else_and_true_branches():
    # poly(x) = x + 0.5, root at x = -0.5 inside [-1, 1]
    xs = [0.5, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(-0.5, abs=1e-9)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-9)


def test_find_zero_with_expansion_positive_root():
    # poly(x) = x - 10, root at x = 10; forces the first while loop
    # to double the bracket several times, then exercises both
    # bisection branches.
    xs = [-10.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(10.0, abs=1e-8)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-8)


def test_find_zero_with_expansion_negative_root():
    # poly(x) = x + 10, root at x = -10; forces bracket expansion
    # in the negative direction.
    xs = [10.0, 1.0]
    result = find_zero(xs)
    assert result == pytest.approx(-10.0, abs=1e-8)
    assert poly(xs, result) == pytest.approx(0.0, abs=1e-8)


def test_find_zero_root_at_begin_endpoint():
    # poly(x) = x + 1, root exactly at begin = -1, so
    # poly(begin) == 0 and the else branch is taken repeatedly.
    xs = [1.0, 1.0]
    result = find_zero(xs)
    assert result == -1.0
    assert poly(xs, result) == 0.0
