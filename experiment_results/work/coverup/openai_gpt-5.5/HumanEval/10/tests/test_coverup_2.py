# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest

from script_10 import make_palindrome


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", ""),
        ("a", "a"),
        ("cat", "catac"),
        ("cata", "catac"),
        ("race", "racecar"),
        ("abba", "abba"),
    ],
)
def test_make_palindrome_returns_shortest_palindrome_beginning_with_input(value, expected):
    result = make_palindrome(value)

    assert result == expected
    assert result.startswith(value)
    assert result == result[::-1]
