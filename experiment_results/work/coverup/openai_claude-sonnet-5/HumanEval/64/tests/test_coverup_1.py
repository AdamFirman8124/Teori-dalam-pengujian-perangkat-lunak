# file: script_64.py:1-17
# asked: {"lines": [13, 14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}
# gained: {"lines": [13, 14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}

import pytest
from script_64 import vowels_count


def test_vowels_count_basic():
    """Test basic vowel counting without y at the end."""
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3


def test_vowels_count_with_y_at_end():
    """Test that 'y' at the end is counted as a vowel."""
    assert vowels_count("sky") == 1
    assert vowels_count("cry") == 1


def test_vowels_count_with_uppercase_y_at_end():
    """Test that 'Y' at the end is counted as a vowel."""
    assert vowels_count("skY") == 1
    assert vowels_count("crY") == 1


def test_vowels_count_without_y_at_end():
    """Test that 'y' not at the end is not counted as a vowel."""
    assert vowels_count("yellow") == 2
    assert vowels_count("yes") == 1


def test_vowels_count_only_consonants():
    """Test string with only consonants (no y at end)."""
    assert vowels_count("bcdfg") == 0


def test_vowels_count_only_vowels():
    """Test string with only vowels."""
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5


def test_vowels_count_single_y():
    """Test single character 'y'."""
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1


def test_vowels_count_mixed_case():
    """Test mixed case vowels."""
    assert vowels_count("AaBbEe") == 4
