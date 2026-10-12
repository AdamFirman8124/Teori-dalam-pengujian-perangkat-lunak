# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import script_7


def test_filter_by_substring_returns_matching_strings():
    strings = ["abc", "bacd", "cde", "array"]

    result = script_7.filter_by_substring(strings, "a")

    assert result == ["abc", "bacd", "array"]


def test_filter_by_substring_excludes_nonmatching_strings():
    strings = ["apple", "banana", "cherry"]

    result = script_7.filter_by_substring(strings, "z")

    assert result == []


def test_filter_by_substring_handles_empty_input():
    result = script_7.filter_by_substring([], "a")

    assert result == []
