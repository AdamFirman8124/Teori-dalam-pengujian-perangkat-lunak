# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string_returns_empty():
    """Covers lines 8-9: the true branch of `if not string`."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome_unchanged():
    """Covers line 8 (false branch), line 13 (loop condition False on the
    first check, so the loop body never runs) and line 16 (return)."""
    assert make_palindrome('racecar') == 'racecar'


def test_make_palindrome_appends_reversed_prefix():
    """Covers lines 13-14: the while loop body executes (suffix must be
    advanced several times before a palindromic suffix is found)."""
    assert make_palindrome('cat') == 'catac'


def test_make_palindrome_loop_runs_once():
    """Covers line 14 with exactly one iteration ('ata' is a palindrome)."""
    assert make_palindrome('cata') == 'catac'


@pytest.mark.parametrize(
    'string, expected',
    [
        ('', ''),
        ('x', 'x'),
        ('ab', 'aba'),
        ('racecar', 'racecar'),
        ('cata', 'catac'),
        ('cat', 'catac'),
        ('jerry', 'jerryrrej'),
    ],
)
def test_make_palindrome_produces_palindrome(string, expected):
    result = make_palindrome(string)
    assert result == expected
    # Postconditions: result is a palindrome and keeps the input as a prefix.
    assert result == result[::-1]
    assert result.startswith(string)
