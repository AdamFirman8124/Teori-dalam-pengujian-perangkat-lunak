# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case covering all lines and branches.

The function is pure (no I/O, no globals mutated), so no monkeypatching or
cleanup fixtures are required; each test only builds throwaway dicts.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_non_string_key_returns_false():
    # Lines 9-11: a non-string key sets state to "mixed" and breaks.
    assert check_dict_case({1: "a"}) is False
    # Non-string key encountered after a valid string key.
    assert check_dict_case({"a": 1, 2: "b"}) is False


def test_all_upper_keys_returns_true():
    # Lines 12-14: first key switches state "start" -> "upper".
    # Lines 22-23: subsequent upper key takes the else branch and breaks.
    # Line 24: returns True because state == "upper".
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Lines 15-16: first key switches state "start" -> "lower".
    # Lines 22-23: subsequent lower key takes the else branch and breaks.
    # Line 24: returns True because state == "lower".
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_first_key_not_cased_returns_false():
    # Lines 17-18: first key is neither upper nor lower -> break with
    # state still "start", so line 24 evaluates to False.
    assert check_dict_case({"1": 1, "A": 2}) is False


def test_upper_then_lower_returns_false():
    # Lines 19-21: state "upper" broken by a non-upper key -> "mixed".
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_returns_false():
    # Lines 19-21 (second operand of the or): state "lower" broken by a
    # non-lower key -> "mixed".
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_single_key_cases():
    # Loop body executes exactly once for each state transition; both
    # outcomes of line 24 are exercised.
    assert check_dict_case({"A": 1}) is True
    assert check_dict_case({"a": 1}) is True
    assert check_dict_case({"A1": 1}) is True  # isupper() is True for "A1"
    assert check_dict_case({"a1": 1}) is True  # islower() is True for "a1"
