# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Covers lines 8-9: empty input returns '' immediately."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """Covers the while-loop condition evaluating False on first check:
    a palindrome input is returned unchanged (suffix length 0)."""
    assert make_palindrome('racecar') == 'racecar'
    assert make_palindrome('a') == 'a'


def test_make_palindrome_appends_reverse_prefix():
    """Covers lines 13-14 and 16: loop advances beginning_of_suffix until
    the remaining suffix is a palindrome, then appends the reversed prefix."""
    # 'cat' -> longest palindromic suffix is 't', prefix 'ca' reversed -> 'ac'
    assert make_palindrome('cat') == 'catac'
    # 'abcd' -> longest palindromic suffix is 'd', prefix 'abc' reversed -> 'cba'
    assert make_palindrome('abcd') == 'abcdcba'
    # result must be a palindrome
    for s in ('cat', 'abcd', 'abab'):
        result = make_palindrome(s)
        assert result == result[::-1]
        assert result.startswith(s)
