# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_mixed_match_and_non_match():
    strings = ["apple", "apricot", "banana", "avocado", "blueberry"]
    result = filter_by_prefix(strings, "ap")
    assert result == ["apple", "apricot"]
    # postcondition: input list is not mutated
    assert strings == ["apple", "apricot", "banana", "avocado", "blueberry"]


def test_filter_by_prefix_no_match():
    result = filter_by_prefix(["cat", "dog", "bird"], "z")
    assert result == []


def test_filter_by_prefix_all_match():
    result = filter_by_prefix(["prefix1", "prefix2", "prefix3"], "prefix")
    assert result == ["prefix1", "prefix2", "prefix3"]


def test_filter_by_prefix_empty_prefix_returns_all():
    strings = ["a", "b", "c"]
    result = filter_by_prefix(strings, "")
    assert result == ["a", "b", "c"]


def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], "pre") == []
    assert filter_by_prefix([], "") == []
