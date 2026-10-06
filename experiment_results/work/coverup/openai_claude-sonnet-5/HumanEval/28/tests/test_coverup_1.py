# file: script_28.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest
from script_28 import concatenate


def test_concatenate_empty_list():
    """Test concatenating an empty list returns empty string"""
    result = concatenate([])
    assert result == ''
    assert isinstance(result, str)


def test_concatenate_single_string():
    """Test concatenating a list with one string"""
    result = concatenate(['hello'])
    assert result == 'hello'


def test_concatenate_multiple_strings():
    """Test concatenating multiple strings"""
    result = concatenate(['a', 'b', 'c'])
    assert result == 'abc'


def test_concatenate_strings_with_spaces():
    """Test concatenating strings that contain spaces"""
    result = concatenate(['hello ', 'world', '!'])
    assert result == 'hello world!'


def test_concatenate_empty_strings():
    """Test concatenating list containing empty strings"""
    result = concatenate(['', '', ''])
    assert result == ''


def test_concatenate_mixed_content():
    """Test concatenating strings with various content"""
    result = concatenate(['foo', '', 'bar', 'baz'])
    assert result == 'foobarbaz'
