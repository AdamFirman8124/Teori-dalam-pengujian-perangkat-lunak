# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f044 import change_base


def test_change_base_multi_digit():
    """Covers lines 3-7: loop body executes multiple times."""
    # 8 in base 3 is 22 (2*3 + 2 = 8)
    assert change_base(8, 3) == "22"


def test_change_base_binary():
    """Covers the loop with base 2."""
    # 10 in base 2 is 1010
    assert change_base(10, 2) == "1010"


def test_change_base_base_larger_than_ten():
    """Digits above 9 are rendered as decimal numbers, not letters."""
    # 255 in base 16 -> digits 15, 15 -> "1515"
    assert change_base(255, 16) == "1515"


def test_change_base_zero_returns_empty_string():
    """Covers the False branch of 'while x > 0' on first check (x == 0)."""
    assert change_base(0, 2) == ""


def test_change_base_negative_returns_empty_string():
    """Covers the False branch of 'while x > 0' for negative x."""
    assert change_base(-5, 2) == ""


def test_change_base_single_digit():
    """Loop body executes exactly once."""
    # 5 in base 10 is "5"
    assert change_base(5, 10) == "5"
