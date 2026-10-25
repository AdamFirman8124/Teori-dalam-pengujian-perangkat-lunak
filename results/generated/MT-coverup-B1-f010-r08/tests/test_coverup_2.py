# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f010 import is_palindrome


def test_is_palindrome_returns_expected_results():
    assert is_palindrome("racecar") is True
    assert is_palindrome("python") is False
