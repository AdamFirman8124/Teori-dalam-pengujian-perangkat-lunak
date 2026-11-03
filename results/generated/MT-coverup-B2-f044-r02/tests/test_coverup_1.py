# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_positive_number():
    """Covers lines 3-7: loop body executes (while branch True) and loop exits."""
    # 8 in base 2 -> "1000"
    assert change_base(8, 2) == "1000"
    # 10 in base 10 -> "10"
    assert change_base(10, 10) == "10"
    # 255 in base 16 -> digits 15,15 -> "1515" (str() of each remainder)
    assert change_base(255, 16) == "1515"


def test_change_base_zero():
    """Covers the while branch False on first check: returns empty string."""
    assert change_base(0, 2) == ""


def test_change_base_negative():
    """Covers the while branch False for negative input: returns empty string."""
    assert change_base(-7, 3) == ""
