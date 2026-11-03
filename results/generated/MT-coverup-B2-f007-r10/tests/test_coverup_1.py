# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_filters_matching_strings():
    strings = ["abc", "bacd", "cde", "array"]
    result = filter_by_substring(strings, "a")
    assert result == ["abc", "bacd", "array"]


def test_filter_by_substring_no_matches_returns_empty_list():
    result = filter_by_substring(["xyz", "uvw"], "a")
    assert result == []


def test_filter_by_substring_empty_input_list():
    result = filter_by_substring([], "a")
    assert result == []


def test_filter_by_substring_empty_substring_matches_all():
    result = filter_by_substring(["abc", "def"], "")
    assert result == ["abc", "def"]


def test_filter_by_substring_does_not_mutate_input():
    strings = ["abc", "xyz"]
    result = filter_by_substring(strings, "a")
    assert strings == ["abc", "xyz"]
    assert result is not strings
