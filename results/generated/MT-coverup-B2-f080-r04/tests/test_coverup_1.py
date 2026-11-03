# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


@pytest.mark.parametrize("s", ["", "a", "ab", "x", "yz"])
def test_too_short_returns_false(s):
    # Covers lines 3-4: the len(s) < 3 branch taken (and its False outcome
    # is exercised by the longer-string tests below).
    assert is_happy(s) is False


@pytest.mark.parametrize("s", ["aab", "aabb", "aaab", "xx"])
def test_first_disjunct_returns_false(s):
    # Covers lines 6, 8-9 with the first condition s[i] == s[i+1] true.
    assert is_happy(s) is False


@pytest.mark.parametrize("s", ["abb", "adbbd", "abbb"])
def test_second_disjunct_returns_false(s):
    # Covers lines 8-9 with s[i] != s[i+1] but s[i+1] == s[i+2] true.
    assert is_happy(s) is False


@pytest.mark.parametrize("s", ["aba", "abab", "abcac"])
def test_third_disjunct_returns_false(s):
    # Covers lines 8-9 with the first two conditions false but
    # s[i] == s[i+2] true (e.g. "aba").
    assert is_happy(s) is False


@pytest.mark.parametrize("s", ["abc", "adb", "abcd", "abcdef", "xyz"])
def test_happy_strings_return_true(s):
    # Covers line 10: loop runs to completion without any violation.
    # Also covers the False outcome of the len(s) < 3 branch (line 3).
    assert is_happy(s) is True


def test_exact_length_three_boundaries():
    # Boundary between the two branches: length 3 is the smallest happy case,
    # length 2 is the largest short case.
    assert is_happy("abc") is True
    assert is_happy("aba") is False
    assert is_happy("ab") is False
