# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from script_7 import filter_by_substring


def test_filter_by_substring_returns_only_matching_strings():
    strings = ["abc", "bacd", "cde", "array"]

    result = filter_by_substring(strings, "a")

    assert result == ["abc", "bacd", "array"]
    assert strings == ["abc", "bacd", "cde", "array"]


def test_filter_by_substring_returns_empty_for_empty_input():
    assert filter_by_substring([], "a") == []


def test_filter_by_substring_returns_empty_when_no_strings_match():
    assert filter_by_substring(["abc", "def", "ghi"], "x") == []


def test_filter_by_substring_matches_substring_at_any_position():
    assert filter_by_substring(["prefix", "middle", "suffix"], "fix") == [
        "prefix",
        "suffix",
    ]
