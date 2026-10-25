# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

from f137 import compare_one


def test_equal_ints_returns_none():
    assert compare_one(1, 1) is None


def test_a_greater_ints_returns_a():
    assert compare_one(5, 3) == 5


def test_b_greater_ints_returns_b():
    assert compare_one(2, 3) == 3


def test_comma_strings_equal_returns_none():
    assert compare_one("1,5", "1.5") is None


def test_both_comma_strings_a_greater_returns_a():
    assert compare_one("2,5", "1,5") == "2,5"


def test_both_comma_strings_b_greater_returns_b():
    assert compare_one("1,5", "2,5") == "2,5"


def test_mixed_str_a_and_int_b_equal_returns_none():
    assert compare_one("1,0", 1) is None


def test_mixed_int_a_and_str_b_b_greater_returns_b():
    assert compare_one(1, "2,0") == "2,0"


def test_mixed_str_a_greater_returns_original_a():
    assert compare_one("3,0", 2) == "3,0"


def test_mixed_str_b_greater_returns_original_b():
    assert compare_one(2, "3,0") == "3,0"
