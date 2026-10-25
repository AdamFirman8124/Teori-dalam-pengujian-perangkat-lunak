# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


def test_compare_one_equal_strings_returns_none():
    assert compare_one("1,5", "1.5") is None


def test_compare_one_string_greater_than_string():
    assert compare_one("2,5", "1.5") == "2,5"


def test_compare_one_string_less_than_string():
    assert compare_one("1,5", "2.5") == "2.5"


def test_compare_one_number_greater_than_string():
    assert compare_one(3.0, "1,5") == 3.0


def test_compare_one_string_less_than_number():
    assert compare_one("1,5", 2) == 2


def test_compare_one_numbers_equal_returns_none():
    assert compare_one(5, 5.0) is None


def test_compare_one_number_greater_than_number():
    assert compare_one(10, 3) == 10


def test_compare_one_number_less_than_number():
    assert compare_one(3, 10) == 10
