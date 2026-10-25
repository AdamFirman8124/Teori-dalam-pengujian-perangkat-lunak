# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

import pytest

from f133 import sum_squares


def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3]) == 14


def test_sum_squares_rounds_floats_up():
    # ceil(1.2) == 2, ceil(2.1) == 3 -> 4 + 9
    assert sum_squares([1.2, 2.1]) == 13


def test_sum_squares_negative_values():
    # ceil(-1.5) == -1 -> 1 ; ceil(-0.5) == 0 -> 0
    assert sum_squares([-1.5, -0.5]) == 1


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_does_not_mutate_input():
    lst = [1.1, 2.9, -3.2]
    original = list(lst)
    result = sum_squares(lst)
    assert lst == original
    assert result == 4 + 9 + 9


def test_sum_squares_uses_math_ceil(monkeypatch):
    calls = []

    def fake_ceil(value):
        calls.append(value)
        return math.floor(value) + 1

    monkeypatch.setattr(math, "ceil", fake_ceil)
    assert sum_squares([0.5, 1.5]) == 1 + 4
    assert calls == [0.5, 1.5]
