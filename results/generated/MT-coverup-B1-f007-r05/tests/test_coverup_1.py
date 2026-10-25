# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_matches():
    result = filter_by_substring(["apple", "banana", "grape"], "an")
    assert result == ["banana"]


def test_filter_by_substring_no_matches():
    result = filter_by_substring(["apple", "kiwi"], "zzz")
    assert result == []


def test_filter_by_substring_empty_input():
    result = filter_by_substring([], "a")
    assert result == []


def test_filter_by_substring_empty_substring():
    result = filter_by_substring(["a", "b"], "")
    assert result == ["a", "b"]


def test_filter_by_substring_multiple_matches_preserves_order():
    result = filter_by_substring(["axb", "bxa", "xx", "axa"], "a")
    assert result == ["axb", "bxa", "axa"]
