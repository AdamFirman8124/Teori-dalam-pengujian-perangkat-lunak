# file: script_51.py:1-17
# asked: {"lines": [17], "branches": []}
# gained: {"lines": [17], "branches": []}

import pytest
from script_51 import remove_vowels


def test_remove_vowels_empty_string():
    """Test with empty string."""
    assert remove_vowels('') == ''


def test_remove_vowels_with_newline():
    """Test with string containing newline."""
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'


def test_remove_vowels_simple():
    """Test with simple string."""
    assert remove_vowels('abcdef') == 'bcdf'


def test_remove_vowels_all_vowels():
    """Test with all vowels."""
    assert remove_vowels('aaaaa') == ''


def test_remove_vowels_mixed_case():
    """Test with mixed case vowels."""
    assert remove_vowels('aaBAA') == 'B'


def test_remove_vowels_no_vowels():
    """Test with no vowels."""
    assert remove_vowels('zbcd') == 'zbcd'


def test_remove_vowels_all_vowel_types():
    """Test with all vowel types to ensure line 17 executes."""
    assert remove_vowels('aeiouAEIOU') == ''


def test_remove_vowels_uppercase_vowels():
    """Test with uppercase vowels."""
    assert remove_vowels('HELLO') == 'HLL'


def test_remove_vowels_special_characters():
    """Test with special characters and vowels."""
    assert remove_vowels('a!e@i#o$u%') == '!@#$%'


def test_remove_vowels_numbers_and_vowels():
    """Test with numbers and vowels."""
    assert remove_vowels('a1e2i3o4u5') == '12345'


def test_remove_vowels_single_vowel():
    """Test with single vowel."""
    assert remove_vowels('a') == ''


def test_remove_vowels_single_consonant():
    """Test with single consonant."""
    assert remove_vowels('b') == 'b'
