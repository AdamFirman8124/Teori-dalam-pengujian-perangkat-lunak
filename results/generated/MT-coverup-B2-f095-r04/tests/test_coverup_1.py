# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case covering all lines and branches (lines 3-24).

check_dict_case is a pure function (it only reads its argument and touches no
global state), so no monkeypatching/cleanup is required; each test uses fresh
dict literals to avoid any shared state.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Covers lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_single_upper_key_returns_true():
    # Covers lines 6-7, 9 (False branch), 12-14, 24 (first operand True).
    assert check_dict_case({"A": 1}) is True


def test_single_lower_key_returns_true():
    # Covers lines 15-16 and 24 (first operand False, second operand True).
    assert check_dict_case({"a": 1}) is True


def test_non_cased_first_key_returns_false():
    # Covers lines 17-18: first key neither upper nor lower -> break, state
    # stays "start", so line 24 evaluates to False.
    assert check_dict_case({"1": 1}) is False


def test_non_string_key_returns_false():
    # Covers lines 9-11: non-str key -> state "mixed", break.
    assert check_dict_case({1: "a"}) is False


def test_all_upper_keys_returns_true():
    # Covers line 12 (False branch), line 19 (False: state "upper" and
    # key.isupper() True), lines 22-23 (else -> break), line 24 True.
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Covers line 19 (False: state "lower" and key.islower() True),
    # lines 22-23, line 24 True via second operand.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_upper_then_lower_returns_false():
    # Covers line 19 (True: state "upper" and not key.isupper()), lines 20-21.
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_returns_false():
    # Covers line 19 (True: state "lower" and not key.islower()), lines 20-21.
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_non_string_key_after_string_key_returns_false():
    # Covers line 9 (True branch) reached with state already "upper".
    assert check_dict_case({"A": 1, 2: "b"}) is False
