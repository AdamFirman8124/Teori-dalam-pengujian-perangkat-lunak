# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f065 import circular_shift


def test_circular_shift_reverses_when_shift_exceeds_length():
    # shift > len(s) -> reversed string branch (lines 3-5)
    assert circular_shift(12, 3) == "21"
    assert circular_shift(12345, 100) == "54321"


def test_circular_shift_rotates_when_shift_within_length():
    # shift <= len(s) -> rotation branch (lines 6-7)
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(1234, 4) == "1234"  # shift == len(s) -> unchanged
    assert circular_shift(12, 1) == "21"


def test_circular_shift_zero_shift_returns_original():
    assert circular_shift(987, 0) == "987"
