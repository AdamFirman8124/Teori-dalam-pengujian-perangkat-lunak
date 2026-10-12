# file: script_54.py:1-17
# asked: {"lines": [17], "branches": []}
# gained: {"lines": [17], "branches": []}

import pytest
from script_54 import same_chars


def test_same_chars_equal_sets():
    """Test when both strings have the same set of characters."""
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') is True


def test_same_chars_equal_sets_different_lengths():
    """Test when strings have different lengths but same characters."""
    assert same_chars('abcd', 'dddddddabc') is True


def test_same_chars_reversed_order():
    """Test with arguments reversed."""
    assert same_chars('dddddddabc', 'abcd') is True


def test_same_chars_first_has_extra():
    """Test when first string has a character not in second."""
    assert same_chars('eabcd', 'dddddddabc') is False


def test_same_chars_second_has_extra():
    """Test when second string has a character not in first."""
    assert same_chars('abcd', 'dddddddabce') is False


def test_same_chars_different_sets():
    """Test when both strings have different sets of characters."""
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') is False


def test_same_chars_empty_strings():
    """Test with empty strings."""
    assert same_chars('', '') is True


def test_same_chars_one_empty():
    """Test when one string is empty."""
    assert same_chars('a', '') is False
    assert same_chars('', 'a') is False


def test_same_chars_single_character():
    """Test with single character strings."""
    assert same_chars('a', 'a') is True
    assert same_chars('a', 'b') is False


def test_same_chars_special_characters():
    """Test with special characters and spaces."""
    assert same_chars('a b!', '!ba ') is True
    assert same_chars('a b', 'ab') is False
