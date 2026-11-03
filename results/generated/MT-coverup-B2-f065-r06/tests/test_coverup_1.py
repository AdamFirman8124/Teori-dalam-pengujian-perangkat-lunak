# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f065 import circular_shift


def test_circular_shift_reverses_when_shift_exceeds_length():
    """shift > len(s) must take the if-branch and return the reversed string
    (covers lines 3, 4 and 5)."""
    assert circular_shift(12, 3) == "21"
    assert circular_shift(123, 10) == "321"
    # negative x still goes through str(x) and the reversal branch
    assert circular_shift(-12, 5) == "21-"


def test_circular_shift_partial_rotation():
    """0 < shift < len(s) must take the else-branch and rotate the digits
    (covers lines 3, 4 and 7)."""
    assert circular_shift(12, 1) == "21"
    assert circular_shift(1234, 2) == "3412"


def test_circular_shift_boundary_shift_equals_length():
    """shift == len(s) is not greater than len(s), so it must take the
    else-branch and yield the original string unchanged."""
    assert circular_shift(12, 2) == "12"


def test_circular_shift_zero_shift():
    """shift == 0 also takes the else-branch and yields the original string."""
    assert circular_shift(123, 0) == "123"
