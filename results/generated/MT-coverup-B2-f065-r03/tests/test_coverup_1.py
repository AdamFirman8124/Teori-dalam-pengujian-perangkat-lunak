# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f065 import circular_shift


def test_circular_shift_reverses_when_shift_exceeds_length():
    """When shift > len(str(x)), the digits are reversed (lines 3-5)."""
    assert circular_shift(12345, 6) == "54321"
    assert circular_shift(12345, 100) == "54321"
    # Works for non-int values too, since str() is applied
    assert circular_shift(12.5, 10) == "5.21"


def test_circular_shift_rotates_when_shift_within_length():
    """When shift <= len(str(x)), the string is rotated right (lines 3-4, 7)."""
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 1) == "51234"
    assert circular_shift(12345, 3) == "34512"


def test_circular_shift_boundary_shift_equals_length():
    """Edge case: shift == len(str(x)) takes the else branch and is a no-op."""
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(0, 1) == "0"
