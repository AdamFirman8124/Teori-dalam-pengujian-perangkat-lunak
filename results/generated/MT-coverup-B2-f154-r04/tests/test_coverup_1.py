# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

"""Tests for f154.cycpattern_check, covering lines 3-9 and all branches.

The function under test is pure (no I/O, no module state), so no
monkeypatching or teardown is required; each test is fully isolated.
"""

from f154 import cycpattern_check


def test_returns_true_when_a_rotation_of_b_is_in_a():
    # "aab" (a rotation of "baa") occurs in "abab" -> executes line 8.
    assert cycpattern_check("abab", "baa") is True


def test_returns_true_after_inner_loop_fails_for_earlier_positions():
    # For i == 0 no rotation of "simen" matches "himen", but for i == 1
    # the rotation "imens" matches. Exercises the False branch of the
    # inner `if` (full inner loop for i == 0) before hitting line 8.
    assert cycpattern_check("himenss", "simen") is True


def test_returns_false_when_no_rotation_matches():
    # No rotation of "abd" ("abd", "bda", "dab") occurs in "abcd":
    # both loops run to completion -> executes line 9.
    assert cycpattern_check("abcd", "abd") is False


def test_returns_false_when_b_is_longer_than_a():
    # len(b) > len(a): range(len(a) - l + 1) is empty, so the outer
    # loop body never executes -> covers the "loop not taken" branch
    # and falls through to line 9.
    assert cycpattern_check("ab", "abcd") is False


def test_empty_pattern_is_always_found():
    # l == 0: a[i:i] == "" == pat[0:0] on the very first comparison
    # -> covers the degenerate-length branch and line 8.
    assert cycpattern_check("abc", "") is True
