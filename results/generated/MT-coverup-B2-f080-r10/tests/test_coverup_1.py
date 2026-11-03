# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

"""Tests for f080.is_happy covering all lines and branches.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
leaves no residual state behind.
"""

import pytest

from f080 import is_happy


def test_shorter_than_three_returns_false():
    """Covers lines 3-4: strings with len(s) < 3 are never happy."""
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_exact_length_three_all_distinct_returns_true():
    """Covers lines 6, 8 (condition False) and 10: minimal happy string."""
    assert is_happy("abc") is True


def test_longer_happy_string_returns_true():
    """Covers line 10 via multiple loop iterations with all-distinct windows."""
    assert is_happy("abcdef") is True
    assert is_happy("abcabc") is True


def test_first_pair_equal_returns_false():
    """Covers lines 8-9 via the s[i] == s[i+1] branch."""
    assert is_happy("aabc") is False


def test_second_pair_equal_returns_false():
    """Covers lines 8-9 via the s[i+1] == s[i+2] branch."""
    assert is_happy("abbc") is False


def test_outer_pair_equal_returns_false():
    """Covers lines 8-9 via the s[i] == s[i+2] branch."""
    assert is_happy("abac") is False


def test_violation_in_later_window_returns_false():
    """Covers lines 8-9 when the loop must iterate before finding a violation."""
    assert is_happy("abcdefgga") is False


def test_length_two_boundary_still_false():
    """Boundary check: len(s) == 2 takes the early-return branch (line 4)."""
    assert is_happy("aa") is False
    assert is_happy("ab") is False


def test_length_three_boundary_enters_loop():
    """Boundary check: len(s) == 3 enters the loop (line 6) and can return True."""
    assert is_happy("xyz") is True
    assert is_happy("xxy") is False
