# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_cycpattern_check_true_rotation():
    # 'b' rotated ('bcda') appears in 'a' -> executes lines 3-8, returns True
    assert cycpattern_check("abcd", "dabc") is True


def test_cycpattern_check_false():
    # no rotation of 'b' appears in 'a' -> executes lines 3-7 and line 9, returns False
    assert cycpattern_check("abcd", "abd") is False


def test_cycpattern_check_exact_substring():
    # 'b' itself (no rotation needed) is a substring of 'a'
    assert cycpattern_check("hello", "ell") is True


def test_cycpattern_check_longer_than_a():
    # len(b) > len(a): range(len(a) - l + 1) is empty -> falls through to line 9
    assert cycpattern_check("ab", "abc") is False


def test_cycpattern_check_empty_b():
    # empty pattern: l == 0, inner loop runs once, a[i:i] == pat[0:0] -> True
    assert cycpattern_check("abc", "") is True


def test_cycpattern_check_empty_a():
    # empty 'a' with non-empty 'b': outer range is empty -> line 9
    assert cycpattern_check("", "abc") is False


def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") is True


def test_cycpattern_check_rotation_at_end():
    # rotation matches only at the very end of 'a' -> exercises full outer loop
    assert cycpattern_check("xyzabc", "cab") is True
