# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_matches():
    strings = ["apple", "banana", "apricot", "cherry"]
    result = filter_by_prefix(strings, "ap")
    assert result == ["apple", "apricot"]


def test_filter_by_prefix_no_matches():
    strings = ["apple", "banana", "cherry"]
    result = filter_by_prefix(strings, "z")
    assert result == []


def test_filter_by_prefix_empty_prefix():
    strings = ["apple", "banana"]
    result = filter_by_prefix(strings, "")
    assert result == ["apple", "banana"]


def test_filter_by_prefix_empty_list():
    result = filter_by_prefix([], "a")
    assert result == []


def test_filter_by_prefix_exact_match():
    strings = ["apple", "applesauce"]
    result = filter_by_prefix(strings, "apple")
    assert result == ["apple", "applesauce"]


def test_filter_by_prefix_does_not_mutate_input():
    strings = ["apple", "banana"]
    original = list(strings)
    filter_by_prefix(strings, "a")
    assert strings == original
