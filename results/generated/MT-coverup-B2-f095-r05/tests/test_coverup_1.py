# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

from f095 import check_dict_case


def test_empty_dict_returns_false():
    assert check_dict_case({}) is False


def test_single_upper_returns_true():
    assert check_dict_case({"A": 1}) is True


def test_single_lower_returns_true():
    assert check_dict_case({"a": 1}) is True


def test_single_non_str_returns_false():
    assert check_dict_case({1: "x"}) is False
    assert check_dict_case({None: 1}) is False


def test_single_neither_upper_nor_lower_returns_false():
    # "123" is neither upper nor lower -> hits else: break with state == "start"
    assert check_dict_case({"123": 1}) is False
    assert check_dict_case({"Hello": 1}) is False


def test_two_upper_match_returns_true():
    # second iteration: state == upper and key matches -> else: break, still upper
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_two_lower_match_returns_true():
    # second iteration: state == lower and key matches -> else: break, still lower
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_upper_then_lower_mismatch_returns_false():
    # second iteration: state == upper and not key.isupper() -> mixed
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_mismatch_returns_false():
    # second iteration: state == lower and not key.islower() -> mixed
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_upper_then_non_str_returns_false():
    # second iteration hits isinstance(key, str) == False -> mixed
    assert check_dict_case({"A": 1, 123: 2}) is False


def test_lower_then_neither_returns_false():
    # "123".isupper() is False and islower() is False, so lower-state mismatches
    assert check_dict_case({"a": 1, "123": 2}) is False
