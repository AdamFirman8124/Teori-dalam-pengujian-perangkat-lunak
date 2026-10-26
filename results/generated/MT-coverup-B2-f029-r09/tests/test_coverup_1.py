# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_only_matching_strings():
    strings = ["apple", "apricot", "banana", "berry"]

    result = filter_by_prefix(strings, "ap")

    assert result == ["apple", "apricot"]
    assert strings == ["apple", "apricot", "banana", "berry"]
