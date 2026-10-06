# file: script_54.py:1-17
# asked: {"lines": [17], "branches": []}
# gained: {"lines": [17], "branches": []}

import pytest
from script_54 import same_chars


def test_same_chars_equal_sets():
    """Test when both strings have the same character set."""
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True


def test_same_chars_different_sets():
    """Test when strings have different character sets."""
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabce') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False


def test_same_chars_empty_strings():
    """Test with empty strings."""
    assert same_chars('', '') == True


def test_same_chars_one_empty():
    """Test when one string is empty."""
    assert same_chars('abc', '') == False
    assert same_chars('', 'abc') == False


def test_same_chars_single_character():
    """Test with single character strings."""
    assert same_chars('a', 'a') == True
    assert same_chars('a', 'b') == False


def test_same_chars_repeated_characters():
    """Test with only repeated characters."""
    assert same_chars('aaa', 'aaaa') == True
    assert same_chars('aaa', 'bbb') == False
