# file: script_101.py:1-22
# asked: {"lines": [10, 11, 13, 15, 16, 17, 19, 21, 22], "branches": [[10, 11], [10, 13], [15, 16], [15, 21], [16, 17], [16, 19]]}
# gained: {"lines": [10, 11, 13, 15, 16, 17, 19, 21, 22], "branches": [[10, 11], [10, 13], [15, 16], [15, 21], [16, 17], [16, 19]]}

import pytest
from script_101 import words_string


def test_empty_string():
    """Test that empty string returns empty list."""
    result = words_string("")
    assert result == []
    assert isinstance(result, list)


def test_single_word():
    """Test single word without separators."""
    result = words_string("Hello")
    assert result == ["Hello"]


def test_comma_separated():
    """Test comma-separated words."""
    result = words_string("One, two, three, four, five, six")
    assert result == ["One", "two", "three", "four", "five", "six"]


def test_space_separated():
    """Test space-separated words."""
    result = words_string("Hi my name is John")
    assert result == ["Hi", "my", "name", "is", "John"]


def test_mixed_separators():
    """Test mixed commas and spaces."""
    result = words_string("Hi, my name is John")
    assert result == ["Hi", "my", "name", "is", "John"]


def test_multiple_commas():
    """Test multiple consecutive commas."""
    result = words_string("word1,,word2")
    assert result == ["word1", "word2"]


def test_multiple_spaces():
    """Test multiple consecutive spaces."""
    result = words_string("word1    word2")
    assert result == ["word1", "word2"]


def test_leading_and_trailing_separators():
    """Test leading and trailing commas and spaces."""
    result = words_string(" , word1, word2 , ")
    assert result == ["word1", "word2"]


def test_only_commas():
    """Test string with only commas."""
    result = words_string(",,,")
    assert result == []


def test_only_spaces():
    """Test string with only spaces."""
    result = words_string("   ")
    assert result == []
