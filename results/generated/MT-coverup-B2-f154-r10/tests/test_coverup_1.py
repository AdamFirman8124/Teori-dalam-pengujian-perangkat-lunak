# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

"""Tests for f154.cycpattern_check, covering lines 3-9 and all branches.

The function under test is pure (no globals, I/O, or mutable state), so no
monkeypatching or cleanup is required; each test is self-contained.
"""

from f154 import cycpattern_check


def test_true_when_rotation_of_b_is_substring_of_a():
    # Covers lines 3-8: setup (l, pat), both loops, the true branch of the
    # `if` on line 7, and `return True` on line 8.
    # "baa" rotates to "aba", which occurs in "abab".
    assert cycpattern_check("abab", "baa") is True
    # "ell" occurs directly in "hello".
    assert cycpattern_check("hello", "ell") is True
    # "simen" rotates to "imens", which occurs in "himenss".
    assert cycpattern_check("himenss", "simen") is True


def test_false_when_no_rotation_of_b_is_substring_of_a():
    # Covers lines 3-7 and 9: the false branch of the `if` on line 7 for
    # every j (full exhaustion of the inner loop on line 6), full exhaustion
    # of the outer loop on line 5, and `return False` on line 9.
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("whassup", "psus") is False


def test_false_when_b_longer_than_a():
    # Covers the zero-iteration branch of the outer loop on line 5
    # (range(len(a) - l + 1) is empty when len(a) < len(b)), falling
    # straight through to `return False` on line 9.
    assert cycpattern_check("ab", "abc") is False
    # Also covers the negative-range variant (empty a).
    assert cycpattern_check("", "abc") is False


def test_true_for_empty_b():
    # Covers l == 0: pat == "", the inner loop on line 6 runs exactly once
    # (j == 0) and the empty slices compare equal on line 7, reaching
    # `return True` on line 8.
    assert cycpattern_check("abc", "") is True
    assert cycpattern_check("", "") is True


def test_single_character_cases():
    # Minimal inputs exercising both outcomes of the `if` on line 7.
    assert cycpattern_check("x", "x") is True
    assert cycpattern_check("x", "y") is False
