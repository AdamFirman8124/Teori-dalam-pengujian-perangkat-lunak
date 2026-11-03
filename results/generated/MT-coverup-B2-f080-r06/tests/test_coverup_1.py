# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


def test_is_happy_short_string_returns_false():
    """Covers line 3-4: strings shorter than 3 characters are not happy."""
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_exactly_three_distinct_chars():
    """Covers line 6 loop executing and line 8-10 with all conditions false."""
    assert is_happy("abc") is True


def test_is_happy_longer_string_all_distinct():
    """Covers multiple loop iterations where the condition never triggers."""
    assert is_happy("abcdef") is True
    assert is_happy("abcd") is True


def test_is_happy_first_two_equal():
    """Covers lines 8-9 triggered by s[i] == s[i+1]."""
    assert is_happy("aab") is False


def test_is_happy_last_two_equal():
    """Covers lines 8-9 triggered by s[i+1] == s[i+2] (short-circuit after first clause is False)."""
    assert is_happy("abb") is False


def test_is_happy_first_and_third_equal():
    """Covers lines 8-9 triggered by s[i] == s[i+2] (short-circuit after first two clauses are False)."""
    assert is_happy("aba") is False


def test_is_happy_violation_later_in_string():
    """Covers loop continuing past an initial valid window before hitting a violation."""
    assert is_happy("abcdef") is True
    assert is_happy("abcdd") is False


def test_is_happy_typical_examples():
    """Sanity checks with well-known examples."""
    assert is_happy("a") is False
    assert is_happy("aa") is False
    assert is_happy("abcd") is True
    assert is_happy("aabb") is False
    assert is_happy("adb") is True
    assert is_happy("xyy") is False
