# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Covers lines 8-9: empty input returns '' immediately."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """Covers the loop condition evaluating False on first check (line 13)."""
    assert make_palindrome('racecar') == 'racecar'


def test_make_palindrome_non_palindrome():
    """Covers lines 13-14 (loop body) and line 16 (suffix reversal appended)."""
    result = make_palindrome('cat')
    assert result == 'catac'
    assert result == result[::-1]  # postcondition: result is a palindrome


def test_make_palindrome_multi_iteration():
    """Forces multiple loop iterations (line 14 executed more than once)."""
    result = make_palindrome('abcd')
    assert result == 'abcdcba'
    assert result == result[::-1]


def test_make_palindrome_single_char():
    """Single character is already a palindrome; loop never entered."""
    assert make_palindrome('x') == 'x'
