# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_cycpattern_check_rotation_found():
    # 'abc' rotated is contained in 'xabcx' -> returns True at line 8
    assert cycpattern_check("xabcx", "cab") is True


def test_cycpattern_check_rotation_not_found():
    # no rotation of 'b' occurs in 'a' -> falls through to line 9
    assert cycpattern_check("xyzw", "abc") is False


def test_cycpattern_check_empty_pattern():
    # empty b: pat = '', inner loop matches empty slice -> True
    assert cycpattern_check("hello", "") is True


def test_cycpattern_check_pattern_longer_than_a():
    # len(b) > len(a): outer range is empty -> returns False at line 9
    assert cycpattern_check("ab", "abcd") is False


def test_cycpattern_check_exact_match():
    # b equals a: matches at j == 0 on first outer iteration
    assert cycpattern_check("abcd", "abcd") is True


def test_cycpattern_check_rotation_at_end():
    # rotation of 'b' appears only at the very end of 'a'
    assert cycpattern_check("xxxybcab", "abc") is True
