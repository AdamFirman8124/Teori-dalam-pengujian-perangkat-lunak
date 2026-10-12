# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest

from script_10 import make_palindrome


def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("racecar", "racecar"),
        ("cat", "catac"),
        ("cata", "catac"),
    ],
)
def test_make_palindrome_returns_shortest_palindrome(string, expected):
    result = make_palindrome(string)

    assert result == expected
    assert result == result[::-1]
    assert result.startswith(string)
