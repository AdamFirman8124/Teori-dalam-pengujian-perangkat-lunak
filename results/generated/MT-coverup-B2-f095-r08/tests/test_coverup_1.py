# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_all_uppercase_keys_returns_true():
    # Lines 6-7, 9, 12-14: first key sets state to "upper";
    # lines 19, 22-23: second key keeps "upper" state via the else-break.
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lowercase_keys_returns_true():
    # Lines 15-16: first key sets state to "lower";
    # lines 19, 22-23: second key keeps "lower" state via the else-break.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_upper_then_lowercase_key_returns_false():
    # Lines 19-21: state == "upper" and not key.isupper() -> "mixed".
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_uppercase_key_returns_false():
    # Lines 19-21: state == "lower" and not key.islower() -> "mixed".
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_non_string_key_returns_false():
    # Lines 9-11: non-string key immediately sets state to "mixed".
    assert check_dict_case({1: "a"}) is False


def test_non_string_key_after_string_key_returns_false():
    # Lines 9-11 reached again after state was already set to "upper".
    assert check_dict_case({"A": 1, 2: "b"}) is False


def test_first_key_neither_upper_nor_lower_returns_false():
    # Lines 17-18: "1".isupper() and "1".islower() are both False -> break.
    assert check_dict_case({"1": 1}) is False


def test_single_uppercase_key_returns_true():
    # Loop ends without break; line 24 returns True for "upper" state.
    assert check_dict_case({"A": 1}) is True


def test_single_lowercase_key_returns_true():
    # Loop ends without break; line 24 returns True for "lower" state.
    assert check_dict_case({"a": 1}) is True
