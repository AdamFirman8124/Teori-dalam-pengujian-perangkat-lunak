# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_matching_strings():
    result = filter_by_prefix(["apple", "banana", "apricot", "cherry"], "ap")
    assert result == ["apple", "apricot"]


def test_filter_by_prefix_returns_empty_when_no_matches():
    result = filter_by_prefix(["banana", "cherry", "date"], "ap")
    assert result == []


def test_filter_by_prefix_empty_input_list():
    result = filter_by_prefix([], "ap")
    assert result == []


def test_filter_by_prefix_empty_prefix_matches_all():
    result = filter_by_prefix(["apple", "banana", "cherry"], "")
    assert result == ["apple", "banana", "cherry"]


def test_filter_by_prefix_preserves_order_and_does_not_mutate_input():
    strings = ["prefix_one", "other", "prefix_two"]
    original = list(strings)
    result = filter_by_prefix(strings, "prefix_")
    assert result == ["prefix_one", "prefix_two"]
    assert strings == original
    assert result is not strings


def test_filter_by_prefix_exact_match_and_case_sensitivity():
    result = filter_by_prefix(["Apple", "apple", "app", "ap"], "app")
    assert result == ["apple", "app"]
