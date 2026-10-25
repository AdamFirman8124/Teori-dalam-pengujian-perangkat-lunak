# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

from f137 import compare_one


def test_compare_one_equal_comma_decimal_strings():
    assert compare_one("1,5", "1.5") is None


def test_compare_one_returns_first_larger_value():
    first = "2,5"
    assert compare_one(first, 2) is first


def test_compare_one_returns_second_larger_value():
    second = "2,5"
    assert compare_one(1, second) is second
