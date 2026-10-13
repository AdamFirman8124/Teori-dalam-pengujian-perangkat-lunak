# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from script_7 import filter_by_substring


def test_filter_by_substring_returns_only_matching_strings():
    strings = ["abc", "bacd", "cde", "array"]

    result = filter_by_substring(strings, "a")

    assert result == ["abc", "bacd", "array"]
    assert all("a" in value for value in result)


def test_filter_by_substring_returns_empty_for_empty_input():
    assert filter_by_substring([], "a") == []


def test_filter_by_substring_returns_empty_when_no_strings_match():
    strings = ["one", "two", "three"]

    result = filter_by_substring(strings, "z")

    assert result == []
