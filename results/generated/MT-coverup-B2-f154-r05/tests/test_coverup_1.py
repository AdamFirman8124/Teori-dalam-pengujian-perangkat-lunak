# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

"""Tests for f154.cycpattern_check covering lines 3-9 (previously uncovered).

The function is pure (no I/O, no globals, no side effects), so calling it
cannot pollute state and no monkeypatching/teardown is required.
"""

from f154 import cycpattern_check


def test_cycpattern_check_returns_true_on_rotation_match():
    # Exercises lines 3-8: len computation, doubled pattern, both loops,
    # the matching branch of the condition, and `return True`.
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("himenss", "simen") is True


def test_cycpattern_check_returns_false_when_no_rotation_matches():
    # Exercises lines 3-7 (False branch of the condition, inner loop fully
    # exhausted for every i) and line 9 (`return False`).
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("whassup", "psus") is False


def test_cycpattern_check_empty_pattern_matches_anything():
    # Edge case: b == "" -> l == 0, pat == "", matches at i == 0 (line 8).
    assert cycpattern_check("abc", "") is True
    assert cycpattern_check("", "") is True


def test_cycpattern_check_empty_haystack_never_matches():
    # Edge case: a == "" -> outer range is empty -> falls through to line 9.
    assert cycpattern_check("", "abc") is False


def test_cycpattern_check_pattern_longer_than_haystack():
    # Edge case: len(b) > len(a) -> range(len(a) - l + 1) is empty -> line 9.
    assert cycpattern_check("ab", "abcd") is False
