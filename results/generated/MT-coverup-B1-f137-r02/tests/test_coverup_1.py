# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

from f137 import compare_one


def test_both_strings_with_comma_equal_returns_none():
    assert compare_one("1,5", "1.5") is None


def test_both_strings_with_comma_a_greater_returns_a():
    assert compare_one("2,5", "1,5") == "2,5"


def test_both_strings_with_dot_b_greater_returns_b():
    assert compare_one("1.0", "2.0") == "2.0"


def test_a_string_b_number_a_greater_returns_original_a():
    assert compare_one("2,0", 1) == "2,0"


def test_a_number_b_string_b_greater_returns_original_b():
    assert compare_one(1, "2,0") == "2,0"


def test_both_numbers_equal_returns_none():
    assert compare_one(2, 2.0) is None


def test_both_numbers_a_greater_returns_a():
    assert compare_one(5, 3) == 5


def test_both_numbers_b_greater_returns_b():
    assert compare_one(1, 2) == 2
