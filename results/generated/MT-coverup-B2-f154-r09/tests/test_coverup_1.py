# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_cycpattern_check_true_rotation_found():
    # Rotated pattern "abc" -> "cab" occurs in "xyzcabyz"
    assert cycpattern_check("xyzcabyz", "abc") is True


def test_cycpattern_check_false_no_rotation():
    # No rotation of "abc" appears in "xyzabyz"
    assert cycpattern_check("xyzabyz", "abc") is False


def test_cycpattern_check_pattern_longer_than_text():
    # Outer loop range is empty -> falls through to return False (line 9)
    assert cycpattern_check("ab", "abc") is False


def test_cycpattern_check_empty_pattern_matches_anything():
    # l == 0: pat == "", a[i:i] == "" == pat[0:0] -> True on first iteration
    assert cycpattern_check("hello", "") is True


def test_cycpattern_check_both_empty():
    # Both strings empty: single iteration, empty slice matches -> True
    assert cycpattern_check("", "") is True


def test_cycpattern_check_empty_text_nonempty_pattern():
    # len(a) - l + 1 == 0 -> outer loop never runs -> False
    assert cycpattern_check("", "abc") is False


def test_cycpattern_check_match_only_via_rotation_at_end():
    # Only the rotation "le" of "el" appears (at the end of "whale")
    assert cycpattern_check("whale", "el") is True


def test_cycpattern_check_exact_substring_match():
    # Direct (non-rotated) match exercises j == 0 branch
    assert cycpattern_check("abcdef", "cde") is True
