# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

from f137 import compare_one


def test_compare_one_returns_none_for_equal_mixed_values():
    assert compare_one("1,0", 1) is None


def test_compare_one_returns_original_first_value_when_greater():
    first = 3
    assert compare_one(first, "2,5") is first


def test_compare_one_returns_original_second_value_when_less():
    second = "3,0"
    assert compare_one("2,5", second) is second
