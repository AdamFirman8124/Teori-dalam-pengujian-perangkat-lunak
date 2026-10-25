# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_matching_strings_in_order():
    strings = ["apple", "banana", "apricot", "berry"]

    result = filter_by_prefix(strings, "ap")

    assert result == ["apple", "apricot"]


def test_filter_by_prefix_returns_empty_list_when_no_strings_match():
    strings = ["apple", "banana", "berry"]

    result = filter_by_prefix(strings, "ch")

    assert result == []
