# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f044 import change_base


def test_change_base_positive_multi_digit():
    """Covers lines 3-7: loop body executes multiple times, then exits (both
    branches of the while condition are taken)."""
    assert change_base(8, 2) == "1000"
    assert change_base(8, 3) == "22"
    assert change_base(7, 2) == "111"
    assert change_base(255, 16) == "1515"


def test_change_base_single_digit():
    """Loop body executes exactly once, then the while condition becomes False."""
    assert change_base(5, 10) == "5"
    assert change_base(1, 2) == "1"


def test_change_base_zero():
    """Covers the while condition being False on the very first check:
    the loop body never runs and the initial empty string is returned."""
    assert change_base(0, 2) == ""


def test_change_base_negative():
    """Negative x also makes the while condition False immediately."""
    assert change_base(-7, 2) == ""
