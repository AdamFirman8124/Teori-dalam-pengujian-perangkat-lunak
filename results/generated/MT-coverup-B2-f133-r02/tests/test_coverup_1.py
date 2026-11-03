# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Empty list: lines 3, 4 and 7 execute; loop body (lines 5-6) is skipped."""
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    """Non-empty list of ints: all lines 3-7 execute."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9
    assert sum_squares([0]) == 0


def test_sum_squares_floats_are_ceiled():
    """Floats are rounded up by math.ceil before squaring (exercises line 6)."""
    # math.ceil(1.2) == 2 and math.ceil(2.7) == 3, so 4 + 9 == 13.
    assert sum_squares([1.2, 2.7]) == 2 ** 2 + 3 ** 2  # 4 + 9 == 13


def test_sum_squares_negative_numbers():
    """math.ceil rounds toward positive infinity for negatives."""
    assert sum_squares([-1.5, -2.0]) == (-1) ** 2 + (-2) ** 2  # 1 + 4 == 5


def test_sum_squares_mixed_values():
    """Mixed positive/negative/zero values accumulate correctly."""
    assert sum_squares([0.5, -0.5, 2]) == 1 + 0 + 4  # 5
