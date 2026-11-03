# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f044 import change_base


def test_change_base_binary_multiple_digits():
    """Covers lines 3-7 with several loop iterations (x stays > 0 across iterations)."""
    assert change_base(10, 2) == "1010"


def test_change_base_base_three():
    """Exercises the loop with a different base and verifies the result."""
    assert change_base(7, 3) == "21"


def test_change_base_single_iteration():
    """Covers the loop with exactly one iteration."""
    assert change_base(4, 2) == "100"


def test_change_base_zero_returns_empty_string():
    """x <= 0 skips the while loop: lines 3 and 7 execute, 4-6 do not."""
    assert change_base(0, 2) == ""
    assert change_base(0, 10) == ""


def test_change_base_negative_returns_empty_string():
    """Negative x also skips the loop body."""
    assert change_base(-5, 2) == ""


def test_change_base_base_ten_identity():
    """Base 10 conversion returns the decimal representation."""
    assert change_base(123, 10) == "123"
