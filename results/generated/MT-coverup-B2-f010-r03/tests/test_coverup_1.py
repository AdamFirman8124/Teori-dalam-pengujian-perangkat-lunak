# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

from f010 import make_palindrome


def test_make_palindrome_empty_string() -> None:
    assert make_palindrome("") == ""


def test_make_palindrome_appends_reversed_prefix() -> None:
    result = make_palindrome("ab")
    assert result == "aba"
    assert result == result[::-1]
