# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case covering all lines and branches (lines 3-24).

The function under test is pure (no globals, I/O, or input mutation), so no
monkeypatching or teardown is required; each test builds its own fresh inputs
to avoid any state pollution between tests.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    """Covers lines 3-4: empty dict short-circuits to False."""
    assert check_dict_case({}) is False


def test_non_string_first_key_returns_false():
    """Covers lines 9-11: non-string key sets state to 'mixed' and breaks."""
    assert check_dict_case({1: "a", "b": 2}) is False


def test_non_string_key_after_string_key_returns_false():
    """Covers lines 9-11 reached again while state is 'lower'."""
    assert check_dict_case({"a": 1, 2: "b"}) is False


def test_all_upper_case_keys_returns_true():
    """Covers lines 12-14 (state -> 'upper') and lines 22-23 (else-break)."""
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_case_keys_returns_true():
    """Covers lines 15-16 (state -> 'lower') and lines 22-23 (else-break)."""
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_single_upper_key_returns_true():
    """Covers natural loop exit (no break) ending in 'upper' state."""
    assert check_dict_case({"A": 1}) is True


def test_single_lower_key_returns_true():
    """Covers natural loop exit (no break) ending in 'lower' state."""
    assert check_dict_case({"a": 1}) is True


def test_upper_then_lower_returns_false():
    """Covers lines 19-21: 'upper' state broken by a lower-case key."""
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_lower_then_upper_returns_false():
    """Covers lines 19-21: 'lower' state broken by an upper-case key."""
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_first_key_neither_upper_nor_lower_returns_false():
    """Covers lines 17-18: break when first key is neither upper nor lower."""
    assert check_dict_case({"1": 1, "A": 2}) is False
