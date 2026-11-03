# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case.

These tests execute every line (3-24) and every branch of the function.
The function under test is pure (it only inspects the dict passed in and
returns a bool, touching no globals, files, or other external state), so
no monkeypatching/teardown is required; all inputs are local literals and
no state can leak between tests.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Lines 3-4: empty dict short-circuits to False.
    assert check_dict_case({}) is False


def test_single_upper_key_returns_true():
    # Lines 6-7, 12-14: first key sets state to "upper"; loop then exits
    # normally to line 24, which returns True.
    assert check_dict_case({"A": 1}) is True


def test_single_lower_key_returns_true():
    # Lines 15-16: first key sets state to "lower"; loop exits; True.
    assert check_dict_case({"a": 1}) is True


def test_all_upper_keys_returns_true():
    # Line 19 evaluates False (state "upper", key is upper) -> line 23
    # (final else: break) is executed; result is True.
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Line 19 evaluates False (state "lower", key is lower) -> line 23
    # (final else: break) is executed; result is True.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_lower_then_upper_key_returns_false():
    # Lines 20-21: line 19 taken via (state == "lower" and not key.islower()).
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_upper_then_lower_key_returns_false():
    # Lines 20-21: line 19 taken via (state == "upper" and not key.isupper()).
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_non_string_first_key_returns_false():
    # Lines 9-11: non-string key on the first iteration -> "mixed", break.
    assert check_dict_case({1: "one"}) is False


def test_non_string_later_key_returns_false():
    # Lines 9-11: non-string key encountered after state was already set.
    assert check_dict_case({"a": 1, 2: "two"}) is False


def test_non_cased_first_key_returns_false():
    # Line 18: string key that is neither upper nor lower while state is
    # still "start" -> break leaves state as "start", so line 24 is False.
    assert check_dict_case({"1": 1}) is False
