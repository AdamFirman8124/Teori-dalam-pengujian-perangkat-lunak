# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from script_10 import is_palindrome


@pytest.mark.parametrize(
    "string, expected",
    [
        ("racecar", True),
        ("abba", True),
        ("a", True),
        ("", True),
        ("hello", False),
        ("ab", False),
        ("AbBa", False),
    ],
)
def test_is_palindrome_executes_return_line(string, expected):
    # Calling the function executes the previously uncovered return statement.
    result = is_palindrome(string)
    assert result is expected
    # Postcondition: result agrees with direct evaluation of the palindrome check.
    assert result is (string == string[::-1])


def test_is_palindrome_matches_reference_on_edge_cases():
    for string in ["", "x", "xx", "xy", "aba", "abc", "12321", "12345", "aa bb aa", "Aa"]:
        assert is_palindrome(string) is (string == string[::-1])
