# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

from f154 import cycpattern_check


def test_exact_match_returns_true():
    assert cycpattern_check("hello", "hello") is True


def test_rotation_returns_true():
    # "abcd" is a rotation of "bcda" (pat[3:7] == "abcd")
    assert cycpattern_check("abcd", "bcda") is True


def test_rotation_in_substring_late_match_returns_true():
    # "abc" at index 2 is a rotation of "cab" (j=1)
    # exercises later outer iteration (i=2) and later inner iteration (j=1)
    assert cycpattern_check("xxabcxx", "cab") is True


def test_no_match_returns_false():
    # exhausts both loops without hitting return True, covers line 9
    assert cycpattern_check("abcd", "abce") is False


def test_a_shorter_than_b_returns_false():
    # range(len(a) - l + 1) is empty, outer loop body never runs
    assert cycpattern_check("ab", "abc") is False


def test_empty_a_returns_false():
    assert cycpattern_check("", "a") is False


def test_empty_b_returns_true():
    # l == 0, pat == "", a[i:i] == "" matches immediately
    assert cycpattern_check("abc", "") is True
