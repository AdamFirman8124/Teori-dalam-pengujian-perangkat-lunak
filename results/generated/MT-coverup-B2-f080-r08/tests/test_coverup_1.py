# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

"""Tests for f080.is_happy covering all lines and branches."""

from f080 import is_happy


def test_empty_string_returns_false():
    """Length < 3 (empty) -> False (first branch of line 3)."""
    assert is_happy("") is False


def test_short_string_returns_false():
    """Length < 3 (length 2) -> False (first branch of line 3)."""
    assert is_happy("ab") is False


def test_happy_string_returns_true():
    """All 3-windows have distinct chars -> True (loop completes, line 10)."""
    assert is_happy("abc") is True


def test_longer_happy_string_returns_true():
    """Longer string with every 3-window distinct -> True."""
    assert is_happy("abcdef") is True


def test_first_condition_triggers_false():
    """s[i] == s[i+1] -> False (first condition of line 8)."""
    assert is_happy("aabc") is False


def test_second_condition_triggers_false():
    """s[i+1] == s[i+2] (with s[i] != s[i+1]) -> False (second condition)."""
    assert is_happy("abbc") is False


def test_third_condition_triggers_false():
    """s[i] == s[i+2] (first two conditions false) -> False (third condition)."""
    assert is_happy("abab") is False


def test_boundary_length_three_happy():
    """Exactly length 3, all distinct -> True."""
    assert is_happy("xyz") is True


def test_boundary_length_three_unhappy():
    """Exactly length 3, duplicate present -> False."""
    assert is_happy("xyx") is False
