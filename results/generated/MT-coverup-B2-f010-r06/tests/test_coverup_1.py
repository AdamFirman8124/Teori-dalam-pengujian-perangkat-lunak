# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import f010


def test_make_palindrome_empty_string():
    assert f010.make_palindrome("") == ""


def test_make_palindrome_appends_reversed_prefix():
    result = f010.make_palindrome("abcd")
    assert result == "abcdcba"
    assert f010.is_palindrome(result)
