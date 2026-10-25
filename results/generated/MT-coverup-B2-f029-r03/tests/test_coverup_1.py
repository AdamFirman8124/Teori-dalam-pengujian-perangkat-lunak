# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_only_matching_strings():
    strings = ["prefix_one", "other", "prefix_two", "unrelated"]
    original = strings.copy()

    result = filter_by_prefix(strings, "prefix_")

    assert result == ["prefix_one", "prefix_two"]
    assert strings == original


def test_filter_by_prefix_returns_empty_list_when_input_is_empty():
    assert filter_by_prefix([], "prefix_") == []
