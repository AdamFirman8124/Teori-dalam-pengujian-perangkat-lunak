# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

import pytest

from f095 import check_dict_case


def test_empty_dict_returns_false():
    assert check_dict_case({}) is False


def test_non_string_key_returns_false():
    # non-str key triggers state = "mixed" and break (lines 9-11)
    d = {1: "a", "B": "b"}
    assert check_dict_case(d) is False


def test_all_upper_keys_returns_true():
    # covers "upper" state, and the else-break at line 23
    d = {"A": 1, "B": 2}
    assert check_dict_case(d) is True


def test_all_lower_keys_returns_true():
    # covers "lower" state, and the else-break at line 23
    d = {"a": 1, "b": 2}
    assert check_dict_case(d) is True


def test_first_key_uncased_breaks_and_returns_false():
    # "123" is neither upper nor lower -> break at line 18, state stays "start"
    d = {"123": 1, "B": 2}
    assert check_dict_case(d) is False


def test_upper_then_lower_becomes_mixed():
    # covers line 19-21: state "upper" but key not upper
    d = {"A": 1, "b": 2}
    assert check_dict_case(d) is False


def test_lower_then_upper_becomes_mixed():
    # covers line 19-21: state "lower" but key not lower
    d = {"a": 1, "B": 2}
    assert check_dict_case(d) is False


def test_single_upper_key_returns_true():
    # loop ends without break; state remains "upper"
    d = {"A": 1}
    assert check_dict_case(d) is True


def test_single_lower_key_returns_true():
    # loop ends without break; state remains "lower"
    d = {"a": 1}
    assert check_dict_case(d) is True


def test_does_not_mutate_input():
    d = {"A": 1, "B": 2}
    snapshot = dict(d)
    check_dict_case(d)
    assert d == snapshot
