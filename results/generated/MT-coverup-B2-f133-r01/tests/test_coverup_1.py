# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Empty list: loop body is skipped, function returns 0.

    Covers lines 3, 4 and 7 (import, initialization, return) and the
    branch where the for-loop does not execute.
    """
    assert sum_squares([]) == 0


def test_sum_squares_positive_floats():
    """Positive floats: math.ceil rounds up before squaring.

    Covers lines 5 and 6 (loop body) with the loop executing.
    """
    result = sum_squares([1.2, 2.3])
    assert result == math.ceil(1.2) ** 2 + math.ceil(2.3) ** 2
    assert result == 2 ** 2 + 3 ** 2
    assert result == 13


def test_sum_squares_negative_floats():
    """Negative floats: math.ceil rounds toward positive infinity."""
    result = sum_squares([-1.5, -2.5])
    assert result == math.ceil(-1.5) ** 2 + math.ceil(-2.5) ** 2
    assert result == (-1) ** 2 + (-2) ** 2
    assert result == 5


def test_sum_squares_integers():
    """Integers pass through math.ceil unchanged."""
    result = sum_squares([1, 2, 3])
    assert result == 1 + 4 + 9
    assert result == 14


def test_sum_squares_single_element():
    """Single-element list exercises the loop exactly once."""
    assert sum_squares([2.1]) == math.ceil(2.1) ** 2 == 9


def test_sum_squares_mixed_values():
    """Mixed positive, negative and zero values accumulate correctly."""
    result = sum_squares([0.5, -0.5, 0])
    assert result == math.ceil(0.5) ** 2 + math.ceil(-0.5) ** 2 + math.ceil(0) ** 2
    assert result == 1 + 0 + 0
    assert result == 1
