# file: project/f032/__init__.py:9-21
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 18, 20, 21], "branches": [[12, 13], [12, 15], [15, 16], [15, 21], [17, 18], [17, 20]]}

import pytest

import f032


def test_find_zero_exercises_both_bisection_branches():
    root = f032.find_zero([-0.25, 1.0])

    assert root == pytest.approx(0.25, abs=1e-10)
    assert f032.poly([-0.25, 1.0], root) == pytest.approx(0.0, abs=1e-10)


def test_find_zero_expands_initial_interval(monkeypatch):
    calls = []
    original_poly = f032.poly

    def tracking_poly(xs, x):
        calls.append(x)
        return original_poly(xs, x)

    monkeypatch.setattr(f032, "poly", tracking_poly)

    root = f032.find_zero([-3.0, 1.0])

    assert root == pytest.approx(3.0, abs=1e-10)
    assert -2.0 in calls
    assert 2.0 in calls
    assert -4.0 in calls
    assert 4.0 in calls
