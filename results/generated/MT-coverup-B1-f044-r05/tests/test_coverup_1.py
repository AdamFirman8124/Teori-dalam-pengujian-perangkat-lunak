# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f044 import change_base


def test_change_base_zero_returns_empty():
    assert change_base(0, 10) == ""


def test_change_base_negative_returns_empty():
    assert change_base(-5, 10) == ""


def test_change_base_single_iteration():
    assert change_base(5, 10) == "5"


def test_change_base_decimal_identity():
    assert change_base(123, 10) == "123"


def test_change_base_binary_multi_iteration():
    assert change_base(8, 2) == "1000"
    assert change_base(10, 2) == "1010"
    assert change_base(9, 2) == "1001"


def test_change_base_octal():
    assert change_base(8, 8) == "10"
