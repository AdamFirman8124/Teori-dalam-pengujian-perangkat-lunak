# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_matching_strings():
    strings = ["apple", "apricot", "banana", "application"]

    result = filter_by_prefix(strings, "ap")

    assert result == ["apple", "apricot", "application"]


def test_filter_by_prefix_returns_empty_list_when_nothing_matches():
    strings = ["apple", "banana", "cherry"]

    result = filter_by_prefix(strings, "z")

    assert result == []
