# file: script_29.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_29 import filter_by_prefix


def test_filter_by_prefix_empty_list():
    """Test with empty list."""
    result = filter_by_prefix([], "test")
    assert result == []


def test_filter_by_prefix_no_matches():
    """Test when no strings have the prefix."""
    result = filter_by_prefix(["hello", "world", "foo"], "test")
    assert result == ["hello", "world", "foo"]


def test_filter_by_prefix_all_match():
    """Test when all strings have the prefix."""
    result = filter_by_prefix(["test1", "test2", "test3"], "test")
    assert result == []


def test_filter_by_prefix_some_match():
    """Test when some strings have the prefix."""
    result = filter_by_prefix(["test1", "hello", "test2", "world"], "test")
    assert result == ["hello", "world"]


def test_filter_by_prefix_empty_prefix():
    """Test with empty prefix - all strings start with empty string."""
    result = filter_by_prefix(["hello", "world"], "")
    assert result == []


def test_filter_by_prefix_case_sensitive():
    """Test that prefix matching is case-sensitive."""
    result = filter_by_prefix(["Test", "test", "hello"], "test")
    assert result == ["Test", "hello"]
