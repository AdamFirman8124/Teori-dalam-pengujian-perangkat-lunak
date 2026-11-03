# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

"""Tests for f154.cycpattern_check covering all lines and branches (lines 3-9)."""

from f154 import cycpattern_check


def test_cycpattern_check_true_early_return():
    """A rotation of b occurs in a: hits the inner 'if' True branch and 'return True' (lines 7-8)."""
    assert cycpattern_check("hello", "ell") is True   # rotation "ell" found directly
    assert cycpattern_check("abab", "baa") is True    # rotation "aba" found at index 1
    assert cycpattern_check("himenss", "simen") is True  # rotation "imens" found at index 1


def test_cycpattern_check_false_full_scan():
    """No rotation of b occurs in a: inner 'if' False branch taken, loops exhaust, 'return False' (lines 7 False, 9)."""
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("efef", "eeff") is False


def test_cycpattern_check_b_longer_than_a():
    """len(b) > len(a): outer loop range is empty, so its body (lines 6-7) never runs; falls through to 'return False'."""
    assert cycpattern_check("ab", "abc") is False
    assert cycpattern_check("", "a") is False


def test_cycpattern_check_empty_b():
    """Empty b: l == 0, so a[i:i] == pat[j:j] ('' == '') is True on the first comparison."""
    assert cycpattern_check("abc", "") is True
    assert cycpattern_check("", "") is True
