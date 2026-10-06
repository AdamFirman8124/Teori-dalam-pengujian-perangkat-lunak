# file: script_86.py:1-14
# asked: {"lines": [14], "branches": []}
# gained: {"lines": [14], "branches": []}

import pytest
from script_86 import anti_shuffle


def test_anti_shuffle_empty_string():
    """Test with empty string"""
    assert anti_shuffle('') == ''


def test_anti_shuffle_single_word():
    """Test with single word"""
    assert anti_shuffle('hello') == 'ehllo'


def test_anti_shuffle_single_uppercase_word():
    """Test with single uppercase word"""
    assert anti_shuffle('Hi') == 'Hi'


def test_anti_shuffle_multiple_words():
    """Test with multiple words"""
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'


def test_anti_shuffle_multiple_spaces():
    """Test with multiple consecutive spaces"""
    assert anti_shuffle('a  b') == 'a  b'


def test_anti_shuffle_leading_trailing_spaces():
    """Test with leading and trailing spaces"""
    assert anti_shuffle(' hello ') == ' ehllo '


def test_anti_shuffle_numeric_characters():
    """Test with numeric characters"""
    assert anti_shuffle('321 abc') == '123 abc'


def test_anti_shuffle_special_characters():
    """Test with special characters - sorted by ASCII value"""
    assert anti_shuffle('!@# $%^') == '!#@ $%^'


def test_anti_shuffle_mixed_case():
    """Test with mixed case - uppercase comes before lowercase in ASCII"""
    assert anti_shuffle('aAbBcC') == 'ABCabc'
