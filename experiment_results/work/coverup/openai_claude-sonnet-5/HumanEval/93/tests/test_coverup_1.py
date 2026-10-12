# file: script_93.py:1-18
# asked: {"lines": [15, 16, 17, 18], "branches": []}
# gained: {"lines": [15, 16, 17, 18], "branches": []}

import pytest
from script_93 import encode


def test_encode_lowercase_vowels():
    """Test encoding with lowercase vowels"""
    assert encode('aeiou') == 'CGKQW'


def test_encode_uppercase_vowels():
    """Test encoding with uppercase vowels"""
    assert encode('AEIOU') == 'cgkqw'


def test_encode_mixed_case_with_vowels():
    """Test encoding with mixed case letters including vowels"""
    assert encode('test') == 'TGST'


def test_encode_sentence_with_spaces():
    """Test encoding a sentence with spaces"""
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'


def test_encode_consonants_only():
    """Test encoding with only consonants"""
    assert encode('bcdfg') == 'BCDFG'


def test_encode_all_vowels_lowercase():
    """Test all lowercase vowels are replaced correctly"""
    result = encode('aeiou')
    assert result == 'CGKQW'
    assert 'a' not in result
    assert 'e' not in result
    assert 'i' not in result
    assert 'o' not in result
    assert 'u' not in result


def test_encode_all_vowels_uppercase():
    """Test all uppercase vowels are replaced correctly"""
    result = encode('AEIOU')
    assert result == 'cgkqw'
    assert 'A' not in result
    assert 'E' not in result
    assert 'I' not in result
    assert 'O' not in result
    assert 'U' not in result


def test_encode_empty_string():
    """Test encoding an empty string"""
    assert encode('') == ''


def test_encode_single_lowercase_vowel():
    """Test encoding a single lowercase vowel"""
    assert encode('a') == 'C'


def test_encode_single_uppercase_vowel():
    """Test encoding a single uppercase vowel"""
    assert encode('E') == 'g'
