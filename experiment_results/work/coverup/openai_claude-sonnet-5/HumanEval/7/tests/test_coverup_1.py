# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest
from script_7 import filter_by_substring


def test_filter_by_substring_with_matches():
    """Test that line 11 executes with non-empty input containing matches."""
    result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    assert result == ['abc', 'bacd', 'array']
    assert len(result) == 3


def test_filter_by_substring_with_single_string():
    """Test with a single string that matches."""
    result = filter_by_substring(['hello'], 'ell')
    assert result == ['hello']


def test_filter_by_substring_empty_list():
    """Test with empty list."""
    result = filter_by_substring([], 'a')
    assert result == []


def test_filter_by_substring_no_matches():
    """Test when no strings contain the substring."""
    result = filter_by_substring(['xyz', 'def', 'ghi'], 'a')
    assert result == []


def test_filter_by_substring_all_match():
    """Test when all strings match."""
    result = filter_by_substring(['cat', 'catch', 'cattle'], 'cat')
    assert result == ['cat', 'catch', 'cattle']


def test_filter_by_substring_some_match():
    """Test when some strings match and some don't."""
    result = filter_by_substring(['apple', 'banana', 'cherry', 'apricot'], 'ap')
    assert result == ['apple', 'apricot']


def test_filter_by_substring_empty_substring():
    """Test with empty substring - all strings should match."""
    result = filter_by_substring(['abc', 'def'], '')
    assert result == ['abc', 'def']
