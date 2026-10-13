# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest
from script_7 import filter_by_substring


def test_filter_by_substring_empty_list():
    """Test with empty list"""
    result = filter_by_substring([], 'a')
    assert result == []


def test_filter_by_substring_with_matches():
    """Test with strings containing substring"""
    result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    assert result == ['abc', 'bacd', 'array']


def test_filter_by_substring_no_matches():
    """Test with no strings containing substring"""
    result = filter_by_substring(['xyz', 'def', 'ghi'], 'a')
    assert result == []


def test_filter_by_substring_all_match():
    """Test where all strings contain substring"""
    result = filter_by_substring(['apple', 'banana', 'apricot'], 'a')
    assert result == ['apple', 'banana', 'apricot']


def test_filter_by_substring_single_element_match():
    """Test with single element that matches"""
    result = filter_by_substring(['test'], 'es')
    assert result == ['test']


def test_filter_by_substring_single_element_no_match():
    """Test with single element that doesn't match"""
    result = filter_by_substring(['test'], 'xyz')
    assert result == []


def test_filter_by_substring_case_sensitive():
    """Test that filtering is case sensitive"""
    result = filter_by_substring(['ABC', 'abc', 'aBc'], 'ab')
    assert result == ['abc']


def test_filter_by_substring_full_string_match():
    """Test with substring being the full string"""
    result = filter_by_substring(['hello', 'world'], 'hello')
    assert result == ['hello']


def test_filter_by_substring_empty_substring():
    """Test with empty substring - all strings should match"""
    result = filter_by_substring(['a', 'b', 'c'], '')
    assert result == ['a', 'b', 'c']
