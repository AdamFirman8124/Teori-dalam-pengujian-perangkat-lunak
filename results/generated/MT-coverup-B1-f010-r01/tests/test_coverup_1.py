# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest

from f010 import make_palindrome


def test_make_palindrome_empty_string_returns_empty():
    result = make_palindrome("")
    assert result == ""
    assert result == result[::-1]


def test_make_palindrome_already_palindrome_returns_unchanged():
    result = make_palindrome("aba")
    assert result == "aba"
    assert result == result[::-1]


def test_make_palindrome_single_char_returns_unchanged():
    result = make_palindrome("a")
    assert result == "a"
    assert result == result[::-1]


def test_make_palindrome_loop_runs_once():
    # "ab" -> suffix "b" is a palindrome at index 1
    result = make_palindrome("ab")
    assert result == "aba"
    assert result == result[::-1]


def test_make_palindrome_loop_runs_multiple_times():
    # "abc" -> "abcba"
    result = make_palindrome("abc")
    assert result == "abcba"
    assert result == result[::-1]


def test_make_palindrome_longer_input():
    result = make_palindrome("racecarx")
    assert result == "racecarxracecar"
    assert result == result[::-1]


def test_make_palindrome_does_not_mutate_input():
    original = "abc"
    value = "abc"
    make_palindrome(value)
    assert value == original


def test_make_palindrome_uses_is_palindrome(monkeypatch):
    calls = []

    def fake_is_palindrome(string: str) -> bool:
        calls.append(string)
        return string == string[::-1]

    monkeypatch.setattr("f010.is_palindrome", fake_is_palindrome)

    result = make_palindrome("abc")
    assert result == "abcba"
    assert calls == ["abc", "bc", "c"]
