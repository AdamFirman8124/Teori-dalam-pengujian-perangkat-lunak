# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case.

The function under test is pure: it only reads its argument and returns a
bool, and it does not touch any module-level or global state.  Therefore no
monkeypatching or fixture-based teardown is needed -- each test builds its
own throwaway dict, so there is no state pollution between tests.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_all_upper_keys_returns_true():
    # Lines 6-7, 9, 12-14 set state="upper"; the second key takes the
    # else-branch break (lines 22-23); line 24 returns True.
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Lines 15-16 set state="lower"; second key takes the else-break; True.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_single_upper_key_returns_true():
    # Loop exhausts after one key; lines 13-14 and 24 covered.
    assert check_dict_case({"ABC": 1}) is True


def test_single_lower_key_returns_true():
    # Loop exhausts after one key; lines 15-16 and 24 covered.
    assert check_dict_case({"abc": 1}) is True


def test_upper_then_lower_is_mixed():
    # Lines 19-21: state "upper" broken by a lower-case key -> "mixed".
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_is_mixed():
    # Second disjunct of line 19: state "lower" broken by an upper-case key.
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_non_string_key_is_mixed():
    # Lines 9-11: non-string key -> state "mixed" -> False.
    assert check_dict_case({1: "one"}) is False


def test_non_string_key_after_string_key_is_mixed():
    # Lines 9-11 reached on a later iteration, with state != "start".
    assert check_dict_case({"A": 1, 2: "two"}) is False


def test_first_key_without_case_breaks():
    # Lines 17-18: "123" is neither isupper() nor islower() -> break.
    assert check_dict_case({"123": 1}) is False


def test_mixed_case_first_key_breaks():
    # Lines 17-18: "Hello" is neither all-upper nor all-lower -> break.
    assert check_dict_case({"Hello": 1}) is False
