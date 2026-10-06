# file: script_64.py:1-17
# asked: {"lines": [13, 14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}
# gained: {"lines": [13, 14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}

import pytest
from script_64 import vowels_count


def test_vowels_count_basic():
    """Test basic vowel counting without y at the end"""
    assert vowels_count("abcde") == 2


def test_vowels_count_with_y_at_end():
    """Test that y at the end is counted as a vowel"""
    assert vowels_count("ACEDY") == 3


def test_vowels_count_lowercase_y_at_end():
    """Test that lowercase y at the end is counted as a vowel"""
    assert vowels_count("sky") == 1


def test_vowels_count_uppercase_Y_at_end():
    """Test that uppercase Y at the end is counted as a vowel"""
    assert vowels_count("SKY") == 1


def test_vowels_count_y_in_middle():
    """Test that y in the middle is not counted as a vowel"""
    assert vowels_count("python") == 1


def test_vowels_count_only_consonants():
    """Test string with only consonants (no y at end)"""
    assert vowels_count("bcdfg") == 0


def test_vowels_count_only_vowels():
    """Test string with only vowels"""
    assert vowels_count("aeiou") == 5


def test_vowels_count_mixed_case():
    """Test mixed case vowels"""
    assert vowels_count("AeIoU") == 5


def test_vowels_count_single_vowel():
    """Test single vowel character"""
    assert vowels_count("a") == 1


def test_vowels_count_single_y():
    """Test single y character (should count as vowel at end)"""
    assert vowels_count("y") == 1


def test_vowels_count_single_Y():
    """Test single uppercase Y character (should count as vowel at end)"""
    assert vowels_count("Y") == 1
