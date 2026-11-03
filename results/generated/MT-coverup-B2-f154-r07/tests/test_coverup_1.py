# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

"""Tests for f154.cycpattern_check, covering lines 3-9 (all lines/branches).

cycpattern_check(a, b) returns True if b or any of its rotations is a
substring of a, else False. The function is pure (no I/O, no globals,
no mutable state), so no monkeypatching/cleanup is required.
"""

from f154 import cycpattern_check


def test_exact_substring_match_returns_true():
    # Covers lines 3-8: match found at i > 0 with j == 0.
    assert cycpattern_check("hello", "ell") is True


def test_rotated_pattern_match_returns_true():
    # Covers lines 3-8: match found via a rotation of b (j > 0 branch).
    assert cycpattern_check("abab", "ba") is True


def test_rotation_match_after_shift():
    # Covers lines 3-8: rotation "aab" of "baa" occurs in a.
    assert cycpattern_check("aab", "baa") is True


def test_identical_strings_return_true():
    # Covers lines 3-8: immediate match at i == 0, j == 0.
    assert cycpattern_check("abc", "abc") is True


def test_empty_pattern_always_matches():
    # Covers lines 3-8 with l == 0: inner loop runs once, empty slices match.
    assert cycpattern_check("abc", "") is True


def test_no_rotation_present_returns_false():
    # Covers lines 3-7 and 9: both loops fully exhausted, no match.
    assert cycpattern_check("abcd", "abd") is False


def test_full_exhaustion_single_window_false():
    # Covers lines 3-7 and 9: single outer iteration, all inner j values fail.
    assert cycpattern_check("efef", "eeff") is False


def test_pattern_longer_than_text_returns_false():
    # Covers lines 3-5 and 9: outer loop body never runs (empty range).
    assert cycpattern_check("ab", "abc") is False


def test_empty_text_with_nonempty_pattern_returns_false():
    # Covers lines 3-5 and 9: outer loop body never runs (empty range).
    assert cycpattern_check("", "a") is False
