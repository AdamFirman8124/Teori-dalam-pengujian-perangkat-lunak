# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

from script_2 import truncate_number


def test_truncate_number_returns_decimal_part():
    assert truncate_number(3.5) == 0.5


def test_truncate_number_returns_zero_for_integer():
    assert truncate_number(7.0) == 0.0
