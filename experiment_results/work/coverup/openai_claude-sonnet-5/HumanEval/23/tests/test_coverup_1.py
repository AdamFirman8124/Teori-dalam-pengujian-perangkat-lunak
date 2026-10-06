# file: script_23.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_23 import strlen


def test_strlen_empty_string():
    """Test strlen with empty string"""
    assert strlen('') == 0


def test_strlen_non_empty_string():
    """Test strlen with non-empty string"""
    assert strlen('abc') == 3


def test_strlen_single_character():
    """Test strlen with single character"""
    assert strlen('a') == 1


def test_strlen_with_spaces():
    """Test strlen with spaces"""
    assert strlen('hello world') == 11


def test_strlen_with_special_characters():
    """Test strlen with special characters"""
    assert strlen('!@#$%') == 5
