# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_cycpattern_check_true_direct_match():
    """b itself (rotation j=0) is a substring of a: hits line 8 via the j=0 branch."""
    assert cycpattern_check("hello", "ell") is True


def test_cycpattern_check_true_rotated_match():
    """Only a non-trivial rotation of b matches: exercises inner loop j > 0 and line 8."""
    assert cycpattern_check("abcd", "cdab") is True


def test_cycpattern_check_false_after_full_scan():
    """No rotation of b occurs in a: both loops run to completion, line 9 executes."""
    assert cycpattern_check("abcd", "abd") is False


def test_cycpattern_check_b_longer_than_a():
    """len(b) > len(a) makes the outer range empty (line 5 branch with no iterations), then line 9."""
    assert cycpattern_check("ab", "abc") is False


def test_cycpattern_check_empty_a():
    """Empty a with non-empty b: outer range is empty, returns False."""
    assert cycpattern_check("", "a") is False


def test_cycpattern_check_empty_b():
    """Empty b: l == 0, inner range has a single element and '' == '' matches -> True."""
    assert cycpattern_check("abc", "") is True


def test_cycpattern_check_equal_lengths_rotated():
    """Equal lengths where only a rotation matches: covers full outer range with a hit."""
    assert cycpattern_check("abab", "ba") is True


def test_cycpattern_check_single_chars():
    """Single-character strings: minimal loop bounds, both True and False outcomes."""
    assert cycpattern_check("a", "a") is True
    assert cycpattern_check("a", "b") is False
