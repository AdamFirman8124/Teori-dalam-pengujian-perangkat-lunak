# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_cycpattern_check_returns_true_when_rotation_is_substring():
    # Rotations of "baa": "baa", "aab", "aba" — "aba" occurs in "abab".
    assert cycpattern_check("abab", "baa") is True


def test_cycpattern_check_returns_true_for_exact_substring():
    # First rotation checked (j == 0) matches directly.
    assert cycpattern_check("hello", "ell") is True


def test_cycpattern_check_returns_false_when_no_rotation_matches():
    # Rotations of "eeff": "eeff", "effe", "ffee", "feef" — none in "efef".
    # Exercises the full loops and the final `return False` (line 9).
    assert cycpattern_check("efef", "eeff") is False


def test_cycpattern_check_b_longer_than_a():
    # Outer range is empty; only lines 3, 4, 5 and 9 execute.
    assert cycpattern_check("ab", "abc") is False


def test_cycpattern_check_empty_pattern():
    # Empty pattern is trivially a substring of any string.
    assert cycpattern_check("abc", "") is True


def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") is True


def test_cycpattern_check_empty_string_nonempty_pattern():
    assert cycpattern_check("", "a") is False


def test_cycpattern_check_rotation_at_end_of_string():
    # Rotations of "cab": "cab", "abc", "bca" — "abc" occurs at the
    # last possible position of "xabc" (i == len(a) - len(b)).
    assert cycpattern_check("xabc", "cab") is True
