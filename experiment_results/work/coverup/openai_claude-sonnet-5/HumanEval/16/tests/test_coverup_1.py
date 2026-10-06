# file: script_16.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_16 import count_distinct_characters


def test_count_distinct_characters_mixed_case():
    """Test with mixed case characters"""
    assert count_distinct_characters('xyzXYZ') == 3


def test_count_distinct_characters_repeated():
    """Test with repeated characters"""
    assert count_distinct_characters('Jerry') == 4


def test_count_distinct_characters_empty_string():
    """Test with empty string - executes line 8"""
    assert count_distinct_characters('') == 0


def test_count_distinct_characters_single_character():
    """Test with single character"""
    assert count_distinct_characters('a') == 1


def test_count_distinct_characters_all_same():
    """Test with all same characters"""
    assert count_distinct_characters('aaaa') == 1


def test_count_distinct_characters_with_spaces():
    """Test with spaces and special characters"""
    assert count_distinct_characters('a b c') == 4


def test_count_distinct_characters_numbers_and_letters():
    """Test with numbers and letters"""
    assert count_distinct_characters('abc123ABC') == 6
