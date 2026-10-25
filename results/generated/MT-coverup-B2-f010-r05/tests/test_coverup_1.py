# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

from f010 import is_palindrome, make_palindrome


def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""


def test_make_palindrome_already_palindrome():
    result = make_palindrome("racecar")

    assert result == "racecar"
    assert is_palindrome(result)


def test_make_palindrome_appends_reversed_prefix():
    result = make_palindrome("abcd")

    assert result == "abcdcba"
    assert result.startswith("abcd")
    assert is_palindrome(result)
