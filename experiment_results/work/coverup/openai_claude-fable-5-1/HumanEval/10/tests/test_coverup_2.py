# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest
from script_10 import make_palindrome


def test_make_palindrome_empty():
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    assert make_palindrome('catac') == 'catac'


def test_make_palindrome_needs_suffix():
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'


def test_make_palindrome_single_char():
    assert make_palindrome('a') == 'a'


def test_make_palindrome_multiple_iterations():
    assert make_palindrome('ab') == 'aba'
    assert make_palindrome('abc') == 'abcba'
