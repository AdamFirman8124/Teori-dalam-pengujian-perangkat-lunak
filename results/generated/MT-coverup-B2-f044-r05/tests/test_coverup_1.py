# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_zero_returns_empty():
    assert change_base(0, 2) == ""


def test_change_base_negative_returns_empty():
    assert change_base(-5, 2) == ""


def test_change_base_single_iteration():
    assert change_base(1, 2) == "1"
    assert change_base(5, 10) == "5"


def test_change_base_multiple_iterations_binary():
    assert change_base(5, 2) == "101"
    assert change_base(10, 2) == "1010"


def test_change_base_other_bases():
    assert change_base(8, 8) == "10"
    assert change_base(10, 10) == "10"
    assert change_base(7, 3) == "21"
