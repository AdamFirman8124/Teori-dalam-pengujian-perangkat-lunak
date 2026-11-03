# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

"""Tests for f080.is_happy.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; nothing here can pollute state.
"""

from f080 import is_happy


def test_is_happy_too_short_returns_false():
    """Lines 3-4: strings shorter than 3 characters are never happy."""
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_first_condition_rejects():
    """Lines 8-9: first or-condition (s[i] == s[i+1]) triggers rejection."""
    assert is_happy("aab") is False
    assert is_happy("aabbcc") is False


def test_is_happy_second_condition_rejects():
    """Lines 8-9: second or-condition (s[i+1] == s[i+2]) triggers rejection
    (first condition must be False for this branch to be reached)."""
    assert is_happy("abb") is False
    assert is_happy("abbbc") is False


def test_is_happy_third_condition_rejects():
    """Lines 8-9: third or-condition (s[i] == s[i+2]) triggers rejection
    (first two conditions must be False for this branch to be reached)."""
    assert is_happy("aba") is False
    assert is_happy("abcdad") is False  # rejection happens on a later iteration


def test_is_happy_rejection_on_last_iteration():
    """Lines 6-9: loop runs several times before finding a repetition."""
    # windows: abc, bca, cab, abb -> fails only at the final iteration
    assert is_happy("abcabb") is False


def test_is_happy_happy_strings_return_true():
    """Line 10: loop completes with all 3-windows distinct -> True."""
    assert is_happy("abc") is True
    assert is_happy("abcd") is True
    assert is_happy("abcdef") is True
    assert is_happy("abcdefg") is True
