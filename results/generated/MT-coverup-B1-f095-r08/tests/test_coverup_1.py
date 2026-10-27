# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

from f095 import check_dict_case


def test_empty_dict_returns_false():
    assert check_dict_case({}) is False


def test_single_upper_returns_true():
    assert check_dict_case({"ABC": 1}) is True


def test_single_lower_returns_true():
    assert check_dict_case({"abc": 1}) is True


def test_multiple_upper_returns_true():
    assert check_dict_case({"ABC": 1, "DEF": 2, "GHI": 3}) is True


def test_multiple_lower_returns_true():
    assert check_dict_case({"abc": 1, "def": 2, "ghi": 3}) is True


def test_upper_then_lower_returns_false():
    assert check_dict_case({"ABC": 1, "def": 2}) is False


def test_lower_then_upper_returns_false():
    assert check_dict_case({"abc": 1, "DEF": 2}) is False


def test_non_string_key_first_returns_false():
    assert check_dict_case({1: "a", 2: "b"}) is False


def test_non_string_key_second_returns_false():
    assert check_dict_case({"ABC": 1, 1: 2}) is False


def test_neither_upper_nor_lower_first_key_returns_false():
    assert check_dict_case({"123": 1}) is False


def test_mixed_case_first_key_returns_false():
    assert check_dict_case({"AbC": 1}) is False
