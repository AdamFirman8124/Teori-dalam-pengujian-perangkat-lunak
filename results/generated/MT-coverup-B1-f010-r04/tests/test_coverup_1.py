# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_empty_string_returns_empty():
    assert make_palindrome('') == ''


def test_already_palindrome_returns_same_string():
    assert make_palindrome('racecar') == 'racecar'


def test_single_character_is_palindrome():
    assert make_palindrome('x') == 'x'


def test_non_palindrome_gets_shortest_palindrome_suffix():
    assert make_palindrome('cat') == 'catac'


def test_another_non_palindrome():
    assert make_palindrome('cata') == 'catac'


def test_result_is_always_a_palindrome():
    for s in ['', 'a', 'ab', 'abc', 'race', 'test', 'amanaplanacanal']:
        result = make_palindrome(s)
        assert result == result[::-1]
        assert result.startswith(s)
