# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers the loop-not-taken branch: no iterations, result must be 0."""
    original = []
    result = sum_squares(original)
    assert result == 0
    # Postcondition: input list is not mutated.
    assert original == []


def test_sum_squares_positive_floats():
    """Covers lines 3-7 with a non-empty list (loop taken at least once)."""
    original = [1.2, 2.5]
    result = sum_squares(original)
    # ceil(1.2) == 2, ceil(2.5) == 3
    assert result == 2 ** 2 + 3 ** 2
    assert result == 13
    # Postcondition: input list is not mutated.
    assert original == [1.2, 2.5]


def test_sum_squares_negative_zero_and_int():
    """Covers ceil behaviour for negatives, zero and exact integers."""
    original = [-1.5, 0, 3]
    result = sum_squares(original)
    # ceil(-1.5) == -1, ceil(0) == 0, ceil(3) == 3
    assert result == (-1) ** 2 + 0 ** 2 + 3 ** 2
    assert result == 10
    assert original == [-1.5, 0, 3]


def test_sum_squares_uses_math_ceil(monkeypatch):
    """Verifies the function really calls math.ceil on every element."""
    calls = []
    real_ceil = math.ceil

    def fake_ceil(x):
        calls.append(x)
        return real_ceil(x)

    # monkeypatch restores math.ceil automatically after the test.
    monkeypatch.setattr(math, "ceil", fake_ceil)

    result = sum_squares([1.1, 2.9, -0.5])

    assert calls == [1.1, 2.9, -0.5]
    # ceil(1.1) == 2, ceil(2.9) == 3, ceil(-0.5) == 0
    assert result == 2 ** 2 + 3 ** 2 + 0 ** 2
    assert result == 13


def test_sum_squares_single_element():
    """Single-element list: loop body executes exactly once."""
    assert sum_squares([2.0]) == 4
    assert sum_squares([0.9]) == 1
