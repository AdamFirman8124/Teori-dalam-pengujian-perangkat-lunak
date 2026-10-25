# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_direct_match():
    assert cycpattern_check("abcd", "abcd") is True


def test_rotated_match():
    # "cdab" rotation "abcd" appears in "abcd" at j=2
    assert cycpattern_check("abcd", "cdab") is True


def test_embedded_rotated_match():
    # "abc" at index 4 is a rotation of "cab"
    assert cycpattern_check("xxxxabcxxxx", "cab") is True


def test_no_match_same_length():
    assert cycpattern_check("hello", "world") is False


def test_no_match_longer_a():
    assert cycpattern_check("hello world", "xyzab") is False


def test_a_shorter_than_b_no_outer_iteration():
    # len(a) - len(b) + 1 <= 0 so outer loop never runs
    assert cycpattern_check("ab", "abcde") is False


def test_empty_a_nonempty_b():
    assert cycpattern_check("", "a") is False


def test_empty_b():
    # l == 0, empty string matches immediately
    assert cycpattern_check("anything", "") is True
