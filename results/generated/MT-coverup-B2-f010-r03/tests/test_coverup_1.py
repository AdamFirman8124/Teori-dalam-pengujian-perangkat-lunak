# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Empty input hits the early return (lines 8-9)."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """A palindrome needs no appending: loop condition is False immediately
    (lines 11, 13 evaluated, 16 executed)."""
    assert make_palindrome('aba') == 'aba'
    assert make_palindrome('x') == 'x'


def test_make_palindrome_loop_executes():
    """Non-palindromic input exercises the loop body (lines 13-14) and the
    final concatenation (line 16)."""
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('race') == 'racecar'
    assert make_palindrome('ab') == 'aba'


def test_make_palindrome_postconditions():
    """Postconditions: result starts with the original string and is a
    palindrome; it is the shortest such palindrome (built from the longest
    palindromic suffix of the input)."""
    for s in ['', 'a', 'ab', 'abc', 'race', 'abab', 'xyzzy']:
        result = make_palindrome(s)
        assert result.startswith(s)
        assert result == result[::-1]
        # Independently compute the longest palindromic suffix of s.
        suffix_start = 0
        while s[suffix_start:] != s[suffix_start:][::-1]:
            suffix_start += 1
        assert result == s + s[:suffix_start][::-1]
