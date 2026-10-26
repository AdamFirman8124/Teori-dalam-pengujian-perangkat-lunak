# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

from f010 import make_palindrome, is_palindrome


def test_make_palindrome_empty_string():
    result = make_palindrome('')
    assert result == ''


def test_make_palindrome_already_palindrome():
    result = make_palindrome('aba')
    assert result == 'aba'
    assert is_palindrome(result)


def test_make_palindrome_single_char():
    result = make_palindrome('a')
    assert result == 'a'
    assert is_palindrome(result)


def test_make_palindrome_needs_suffix():
    result = make_palindrome('ab')
    assert result == 'aba'
    assert is_palindrome(result)
    assert result.startswith('ab')


def test_make_palindrome_longer_suffix():
    result = make_palindrome('abc')
    assert result == 'abcba'
    assert is_palindrome(result)
    assert result.startswith('abc')
