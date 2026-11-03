# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case covering all lines and branches (lines 3-24).

The function under test is pure (it only reads its argument and returns a
value), so no monkeypatching or fixture-based cleanup is required; each test
builds its own fresh dictionary, avoiding any state pollution.
"""

import pytest

from f095 import check_dict_case


def test_empty_dict_returns_false():
    """Lines 3-4: an empty dict short-circuits to False."""
    assert check_dict_case({}) is False


def test_single_upper_key_returns_true():
    """Lines 6-7, 9, 12-14, 24: first key sets state to 'upper' -> True."""
    assert check_dict_case({"ABC": 1}) is True


def test_single_lower_key_returns_true():
    """Lines 15-16: first key sets state to 'lower' -> True."""
    assert check_dict_case({"abc": 1}) is True


def test_non_string_key_returns_false():
    """Lines 10-11: a non-string key forces state 'mixed' -> False."""
    assert check_dict_case({1: "a"}) is False


def test_mixed_case_key_breaks_in_start_state():
    """Line 18: a key that is neither upper nor lower breaks out of the
    loop while state is still 'start' -> False."""
    assert check_dict_case({"Abc": 1}) is False


def test_upper_state_then_lower_key_becomes_mixed():
    """Lines 19-21 (first operand of the 'or'): a lower-case key while
    state is 'upper' sets state 'mixed' -> False."""
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_state_then_upper_key_becomes_mixed():
    """Lines 19-21 (second operand of the 'or'): an upper-case key while
    state is 'lower' sets state 'mixed' -> False."""
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_upper_state_then_matching_key_breaks_true():
    """Line 23 (else branch): a second upper-case key while state is
    'upper' hits the else-branch break -> True."""
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_lower_state_then_matching_key_breaks_true():
    """Line 23 (else branch) for the 'lower' state -> True."""
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_three_upper_keys_true():
    """Exercise the loop over several keys, all consistent -> True."""
    assert check_dict_case({"A": 1, "B": 2, "C": 3}) is True


def test_non_string_key_after_string_key():
    """Lines 10-11 reached mid-loop: state 'upper' then an int key -> False."""
    assert check_dict_case({"A": 1, 2: "b"}) is False
