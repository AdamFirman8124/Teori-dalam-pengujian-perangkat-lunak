# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers lines 3-4 and 7: import, initialization, and return with no loop iterations."""
    result = sum_squares([])
    assert result == 0


def test_sum_squares_positive_integers():
    """Covers lines 5-6: loop body with integer values (ceil is identity)."""
    result = sum_squares([1, 2, 3])
    assert result == 1**2 + 2**2 + 3**2
    assert result == 14


def test_sum_squares_negative_and_floats():
    """Covers line 6 branch: math.ceil applied to negative and fractional values."""
    result = sum_squares([-1.5, 2.3])
    assert result == math.ceil(-1.5) ** 2 + math.ceil(2.3) ** 2
    assert result == (-1) ** 2 + 3 ** 2
    assert result == 10
