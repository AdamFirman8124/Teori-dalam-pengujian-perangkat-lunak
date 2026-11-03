# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


def test_is_happy_short_strings_return_false():
    """Covers lines 3-4: strings shorter than 3 chars are not happy."""
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_adjacent_duplicate_returns_false():
    """Covers lines 6, 8, 9 via the s[i] == s[i+1] clause."""
    assert is_happy("aab") is False


def test_is_happy_last_two_duplicate_returns_false():
    """Covers lines 6, 8, 9 via the s[i+1] == s[i+2] clause."""
    assert is_happy("abb") is False


def test_is_happy_first_and_third_duplicate_returns_false():
    """Covers lines 6, 8, 9 via the s[i] == s[i+2] clause."""
    assert is_happy("aba") is False


def test_is_happy_violation_after_several_iterations_returns_false():
    """Covers lines 6, 8, 9 with the loop running multiple times before failing."""
    assert is_happy("abcba") is False


def test_is_happy_happy_strings_return_true():
    """Covers lines 6, 8, 10: every window of 3 chars has all-distinct chars."""
    assert is_happy("abc") is True
    assert is_happy("abcabc") is True
    assert is_happy("abcdef") is True
