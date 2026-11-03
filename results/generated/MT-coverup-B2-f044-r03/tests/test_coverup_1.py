# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_multiple_iterations():
    # Exercises lines 3-7: loop body runs several times (true branch of while)
    assert change_base(8, 2) == "1000"


def test_change_base_base10():
    # Multi-digit conversion in base 10
    assert change_base(123, 10) == "123"


def test_change_base_base16():
    # Digits >= 10 are concatenated as their decimal string representations
    assert change_base(255, 16) == "1515"


def test_change_base_zero():
    # Covers the false branch of the while condition (loop never entered)
    assert change_base(0, 2) == ""


def test_change_base_negative():
    # Negative x also skips the loop body entirely
    assert change_base(-7, 3) == ""
