# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers lines 3-7 with the loop body never executing (empty list)."""
    assert sum_squares([]) == 0


def test_sum_squares_positive_floats():
    """Covers lines 3-7 with the loop body executing (ceil applied)."""
    assert sum_squares([1.2, 2.7]) == 2**2 + 3**2  # 4 + 9 = 13


def test_sum_squares_negative_and_zero():
    """Covers lines 3-7 with negative values and zero (math.ceil of negatives)."""
    assert sum_squares([-1.5, 0.0]) == (-1)**2 + 0**2  # 1 + 0 = 1
