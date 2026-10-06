# file: script_66.py:1-15
# asked: {"lines": [14, 15], "branches": [[14, 14], [14, 15]]}
# gained: {"lines": [14, 15], "branches": [[14, 14], [14, 15]]}

import pytest
from script_66 import digitSum


def test_digitSum_empty_string():
    """Test that empty string returns 0."""
    assert digitSum("") == 0


def test_digitSum_mixed_case():
    """Test with mixed upper and lower case characters."""
    assert digitSum("abAB") == 131


def test_digitSum_single_upper():
    """Test with single uppercase character."""
    assert digitSum("abcCd") == 67


def test_digitSum_upper_at_end():
    """Test with uppercase character at the end."""
    assert digitSum("helloE") == 69


def test_digitSum_multiple_uppers():
    """Test with multiple uppercase characters."""
    assert digitSum("woArBld") == 131


def test_digitSum_repeated_upper():
    """Test with repeated uppercase characters."""
    assert digitSum("aAaaaXa") == 153


def test_digitSum_all_lowercase():
    """Test with all lowercase characters returns 0."""
    assert digitSum("abcdefg") == 0


def test_digitSum_all_uppercase():
    """Test with all uppercase characters."""
    assert digitSum("ABC") == 65 + 66 + 67


def test_digitSum_single_lowercase():
    """Test with single lowercase character returns 0."""
    assert digitSum("a") == 0


def test_digitSum_single_uppercase_char():
    """Test with single uppercase character."""
    assert digitSum("A") == 65
