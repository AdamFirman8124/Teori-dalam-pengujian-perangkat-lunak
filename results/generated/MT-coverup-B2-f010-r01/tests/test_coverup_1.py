# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Covers lines 8-9: empty string short-circuits to ''."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """Covers line 13 (loop condition false immediately) and line 16 with suffix 0."""
    result = make_palindrome('aba')
    assert result == 'aba'
    assert result == result[::-1]


def test_make_palindrome_single_char():
    """Single character is already a palindrome; loop body never runs."""
    assert make_palindrome('x') == 'x'


def test_make_palindrome_appends_reversed_prefix():
    """Covers line 14 (loop increments) and line 16 with a non-zero suffix."""
    result = make_palindrome('cat')
    assert result == 'catac'
    assert result == result[::-1]
    assert result.startswith('cat')


def test_make_palindrome_partial_palindrome_suffix():
    """'cata' has palindromic suffix 'ata', so only 'c' is mirrored."""
    result = make_palindrome('cata')
    assert result == 'catac'
    assert result == result[::-1]


def test_make_palindrome_two_chars():
    """Minimal case exercising one loop iteration."""
    result = make_palindrome('ab')
    assert result == 'aba'
    assert result == result[::-1]


def test_make_palindrome_result_is_palindrome_for_various_inputs():
    """Property check: output is always a palindrome containing the input."""
    for s in ['race', 'abcba', 'abab', 'z', '']:
        result = make_palindrome(s)
        assert result == result[::-1]
        assert result.startswith(s)
