# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

from f137 import compare_one


def test_compare_one_returns_none_for_equal_values():
    assert compare_one("1,5", 1.5) is None


def test_compare_one_returns_first_original_value_when_greater():
    assert compare_one(2, "1,5") == 2


def test_compare_one_returns_second_original_value_when_greater():
    assert compare_one("1,5", "2,0") == "2,0"
