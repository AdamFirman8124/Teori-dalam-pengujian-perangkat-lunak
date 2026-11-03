# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

"""Tests for f080.is_happy.

is_happy is a pure function (no module state, no I/O), so no monkeypatching
or teardown is required; each test is self-contained and leaves no residue.
"""


def test_is_happy_too_short_returns_false():
    """Covers lines 3-4: strings shorter than 3 chars are not happy."""
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_all_windows_distinct_returns_true():
    """Covers lines 6 and 10: loop runs to completion and returns True."""
    assert is_happy("abc") is True
    assert is_happy("abcd") is True
    assert is_happy("abcdefg") is True


def test_is_happy_first_two_equal_returns_false():
    """Covers lines 8-9 via the s[i] == s[i+1] clause."""
    assert is_happy("aab") is False
    assert is_happy("aabb") is False


def test_is_happy_last_two_equal_returns_false():
    """Covers lines 8-9 via the s[i+1] == s[i+2] clause."""
    assert is_happy("abb") is False
    assert is_happy("abbc") is False


def test_is_happy_first_and_third_equal_returns_false():
    """Covers lines 8-9 via the s[i] == s[i+2] clause."""
    assert is_happy("aba") is False
    assert is_happy("abab") is False


def test_is_happy_failure_in_later_window_returns_false():
    """Covers the loop advancing past the first window before returning False."""
    assert is_happy("abcba") is False


from f080 import is_happy  # noqa: E402  (import kept at bottom is unusual; moved below)
