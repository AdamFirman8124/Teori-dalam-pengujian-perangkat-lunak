# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

import pytest

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Covers lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_single_upper_key_returns_true():
    # Covers lines 6-7, 12-14 (state "start" -> "upper") and line 24.
    assert check_dict_case({"A": 1}) is True


def test_single_lower_key_returns_true():
    # Covers lines 15-16 (state "start" -> "lower") and line 24.
    assert check_dict_case({"a": 1}) is True


def test_all_upper_keys_returns_true():
    # Covers lines 22-23 (else branch: state "upper" and key still upper -> break).
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Covers lines 22-23 for the "lower" state path.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_non_string_key_returns_false():
    # Covers lines 9-11: non-string key forces "mixed" state.
    assert check_dict_case({1: "a"}) is False


def test_non_alphabetic_string_key_returns_false():
    # Covers lines 17-18: "start" state with key neither upper nor lower -> break.
    assert check_dict_case({"1": "a"}) is False


def test_upper_then_lower_key_returns_false():
    # Covers lines 19-21: state "upper" broken by a non-upper key -> "mixed".
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_key_returns_false():
    # Covers the second disjunct of line 19: state "lower" broken by a non-lower key.
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_upper_then_non_alphabetic_key_returns_false():
    # Line 19 also triggers for a non-alphabetic follow-up key.
    assert check_dict_case({"A": 1, "1": 2}) is False


def test_non_string_key_after_start_returns_false():
    # Non-string key detected even after the first key set the state.
    assert check_dict_case({"A": 1, 2: "b"}) is False
