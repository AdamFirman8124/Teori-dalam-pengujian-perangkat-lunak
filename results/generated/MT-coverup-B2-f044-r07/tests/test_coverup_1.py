# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_converts_positive_integer():
    assert change_base(10, 2) == "1010"


def test_change_base_returns_empty_string_for_zero():
    assert change_base(0, 2) == ""
