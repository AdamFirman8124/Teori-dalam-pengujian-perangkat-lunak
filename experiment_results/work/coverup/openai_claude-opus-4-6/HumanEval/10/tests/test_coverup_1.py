# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest

import script_10
from script_10 import make_palindrome, is_palindrome


def brute_force_shortest_palindrome(string):
    """Reference implementation: the smallest palindrome beginning with string."""
    for k in range(len(string) + 1):
        candidate = string + string[:k][::-1]
        if is_palindrome(candidate):
            return candidate
    raise AssertionError('unreachable: string + reversed(string) is a palindrome')


@pytest.mark.parametrize(
    'string, expected',
    [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('aba', 'aba'),
        ('abba', 'abba'),
        ('cat', 'catac'),
        ('cata', 'catac'),
        ('abab', 'ababa'),
        ('abac', 'abacaba'),
        ('abcd', 'abcdcba'),
    ],
)
def test_make_palindrome(string, expected):
    result = make_palindrome(string)
    assert result == expected
    assert result.startswith(string)
    assert is_palindrome(result)
    assert result == brute_force_shortest_palindrome(string)


def test_make_palindrome_empty_string_returns_empty_string():
    assert make_palindrome('') == ''


def test_make_palindrome_returns_palindrome_input_unchanged():
    palindrome = 'racecar'
    assert make_palindrome(palindrome) == palindrome


def test_make_palindrome_checks_suffixes_with_is_palindrome(monkeypatch):
    calls = []

    def recording_is_palindrome(text):
        calls.append(text)
        return text == text[::-1]

    monkeypatch.setattr(script_10, 'is_palindrome', recording_is_palindrome)

    result = make_palindrome('abc')

    assert calls == ['abc', 'bc', 'c']
    assert result == 'abcba'
    assert is_palindrome(result)
    assert result.startswith('abc')


def test_make_palindrome_empty_input_never_calls_is_palindrome(monkeypatch):
    def fail_if_called(text):
        raise AssertionError('is_palindrome must not be called for empty input')

    monkeypatch.setattr(script_10, 'is_palindrome', fail_if_called)

    assert make_palindrome('') == ''
