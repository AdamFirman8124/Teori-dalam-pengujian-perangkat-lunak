# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers lines 3-4 and 7 with an empty list (loop body never runs)."""
    assert sum_squares([]) == 0


def test_sum_squares_positive_values():
    """Covers lines 3-7 with positive values requiring math.ceil."""
    result = sum_squares([1.2, 2.7, 3.0])
    assert result == math.ceil(1.2) ** 2 + math.ceil(2.7) ** 2 + math.ceil(3.0) ** 2
    assert result == 4 + 9 + 9
    assert result == 22


def test_sum_squares_negative_values():
    """Covers lines 3-7 with negative values, verifying ceil rounds toward zero."""
    result = sum_squares([-1.5, -2.1])
    assert result == math.ceil(-1.5) ** 2 + math.ceil(-2.1) ** 2
    assert result == 1 + 4
    assert result == 5


def test_sum_squares_uses_math_module(monkeypatch):
    """Verifies line 3 (import math) executes and math.ceil is actually used."""
    calls = []
    original_ceil = math.ceil

    def fake_ceil(x):
        calls.append(x)
        return original_ceil(x)

    monkeypatch.setattr(math, "ceil", fake_ceil)
    result = sum_squares([1.5, 2.5])
    assert calls == [1.5, 2.5]
    assert result == 4 + 9
    assert result == 13
