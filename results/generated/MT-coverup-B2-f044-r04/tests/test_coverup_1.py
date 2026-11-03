# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_positive_multi_iteration():
    """Covers lines 3-7 with the while-loop body executing multiple times."""
    # 8 in base 2 is 1000
    assert change_base(8, 2) == "1000"
    # 10 in base 10 is "10"
    assert change_base(10, 10) == "10"


def test_change_base_multi_digit_remainders():
    """Verifies digit ordering when remainders are multi-digit strings."""
    # 255 in base 16: 255 % 16 = 15 -> "15", then 15 % 16 = 15 -> "15"
    assert change_base(255, 16) == "1515"


def test_change_base_zero():
    """Covers the False branch of 'while x > 0' when x starts at 0."""
    assert change_base(0, 2) == ""


def test_change_base_negative():
    """Covers the False branch of 'while x > 0' when x is negative."""
    assert change_base(-7, 10) == ""
    assert change_base(-1, 2) == ""


def test_change_base_single_digit():
    """Covers exactly one loop iteration."""
    assert change_base(1, 2) == "1"
    assert change_base(5, 10) == "5"
