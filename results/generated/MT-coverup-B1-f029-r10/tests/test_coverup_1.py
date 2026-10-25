# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_mixed_matching_and_nonmatching():
    result = filter_by_prefix(["apple", "banana", "apricot", "cherry"], "ap")
    assert result == ["apple", "apricot"]


def test_filter_by_prefix_empty_list():
    result = filter_by_prefix([], "ap")
    assert result == []


def test_filter_by_prefix_no_matches():
    result = filter_by_prefix(["banana", "cherry", "date"], "ap")
    assert result == []


def test_filter_by_prefix_all_match():
    result = filter_by_prefix(["apple", "apricot", "application"], "ap")
    assert result == ["apple", "apricot", "application"]


def test_filter_by_prefix_empty_prefix_matches_all():
    result = filter_by_prefix(["apple", "banana", ""], "")
    assert result == ["apple", "banana", ""]


def test_filter_by_prefix_case_sensitive_and_exact_prefix():
    result = filter_by_prefix(["Apple", "apple", "app", "ap"], "app")
    assert result == ["apple", "app"]


def test_filter_by_prefix_does_not_mutate_input():
    strings = ["apple", "banana", "apricot"]
    original = list(strings)
    result = filter_by_prefix(strings, "ap")
    assert strings == original
    assert result == ["apple", "apricot"]
    assert result is not strings
