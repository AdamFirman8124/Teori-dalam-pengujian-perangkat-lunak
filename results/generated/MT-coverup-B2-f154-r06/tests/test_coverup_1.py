# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_returns_true_when_b_is_substring_of_a():
    # Exercises lines 3-8; the inner `if` takes the True branch,
    # returning early from line 8.
    assert cycpattern_check("hello", "ell") is True


def test_returns_true_when_rotation_of_b_is_substring_of_a():
    # "aba" (a rotation of "baa") occurs in "abab"; the match is found
    # at j > 0, so several False evaluations of the `if` precede the
    # True one.
    assert cycpattern_check("abab", "baa") is True


def test_returns_true_when_a_equals_b():
    # Match found on the very first (i=0, j=0) comparison.
    assert cycpattern_check("abc", "abc") is True


def test_returns_false_when_no_rotation_of_b_occurs_in_a():
    # Both loops run to completion with the `if` always False,
    # exercising line 9 (`return False`).
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("efef", "eeff") is False


def test_returns_false_when_a_is_shorter_than_b():
    # len(a) - len(b) + 1 <= 0 makes the outer loop range empty, so the
    # loop body (and inner loop) never execute; covers the loop-skipped
    # branch and falls through to line 9.
    assert cycpattern_check("ab", "abcd") is False


def test_empty_pattern_is_found():
    # Edge case: l == 0 gives a single-iteration inner loop and an
    # immediate empty-slice match.
    assert cycpattern_check("xyz", "") is True
