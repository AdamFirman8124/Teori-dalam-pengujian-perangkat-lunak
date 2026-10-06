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


def test_concatenate_with_empty_strings():
    """Test concatenating list containing empty strings"""
    result = concatenate(['', 'a', '', 'b', ''])
    assert result == 'ab'


def test_concatenate_with_spaces():
    """Test concatenating strings with spaces"""
    result = concatenate(['hello', ' ', 'world'])
    assert result == 'hello world'


def test_concatenate_with_special_characters():
    """Test concatenating strings with special characters"""
    result = concatenate(['!', '@', '#', '$'])
    assert result == '!@#$'
