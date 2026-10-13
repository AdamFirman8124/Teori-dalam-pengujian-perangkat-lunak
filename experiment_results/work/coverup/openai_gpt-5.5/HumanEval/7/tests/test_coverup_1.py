# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from script_7 import filter_by_substring


@pytest.mark.parametrize(
    ("strings", "substring", "expected"),
    [
        ([], "a", []),
        (["abc", "bacd", "cde", "array"], "a", ["abc", "bacd", "array"]),
        (["apple", "banana", "cherry"], "na", ["banana"]),
        (["one", "two", "three"], "xyz", []),
    ],
)
def test_filter_by_substring(strings, substring, expected):
    original_strings = list(strings)

    result = filter_by_substring(strings, substring)

    assert result == expected
    assert strings == original_strings
