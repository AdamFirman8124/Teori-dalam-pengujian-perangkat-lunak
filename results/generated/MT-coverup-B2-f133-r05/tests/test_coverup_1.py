# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Calling with an empty list executes lines 3-5 and 7 (loop body skipped)."""
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    """Executing line 6 with integer elements (ceil is identity on ints)."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9


def test_sum_squares_floats_ceil_applied():
    """Executing line 6 and verifying math.ceil is applied to each element."""
    # ceil(1.5) == 2 -> 4 ; ceil(2.3) == 3 -> 9 ; ceil(-1.5) == -1 -> 1
    assert sum_squares([1.5, 2.3, -1.5]) == 4 + 9 + 1


def test_sum_squares_zero_and_negative_floats():
    """Edge cases: zero and negative floats (ceil(-2.5) == -2)."""
    assert sum_squares([0, -2.5]) == 0 + 4


def test_sum_squares_accepts_any_iterable():
    """Line 6 must run for each item of any iterable, not just lists."""
    assert sum_squares(iter([0.5, 1.5])) == 1 + 4
