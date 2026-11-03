# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Covers lines 8-9: empty input short-circuits to ''."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """Covers lines 11, 13 (loop condition immediately false) and 16."""
    assert make_palindrome('aba') == 'aba'


def test_make_palindrome_single_char():
    """A single character is already a palindrome; loop body never runs."""
    assert make_palindrome('x') == 'x'


def test_make_palindrome_loop_runs_once():
    """Covers lines 13-14: while loop body executes once."""
    assert make_palindrome('ab') == 'aba'


def test_make_palindrome_loop_runs_multiple_times():
    """Covers lines 13-14: while loop body executes multiple times."""
    assert make_palindrome('cat') == 'catac'


@pytest.mark.parametrize(
    'string, expected',
    [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('ab', 'aba'),
        ('abc', 'abcba'),
        ('cat', 'catac'),
        ('cata', 'catac'),
        ('race', 'racecar'),
    ],
)
def test_make_palindrome_postconditions(string, expected):
    """Postconditions: exact expected value, result is a palindrome,
    and it preserves the original string as a prefix."""
    result = make_palindrome(string)
    assert result == expected
    assert result == result[::-1]
    assert result.startswith(string)
