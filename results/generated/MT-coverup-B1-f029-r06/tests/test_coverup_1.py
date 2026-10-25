# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_only_strings_with_prefix():
    strings = ["apple", "apricot", "banana", "application"]

    result = filter_by_prefix(strings, "app")

    assert result == ["apple", "application"]
