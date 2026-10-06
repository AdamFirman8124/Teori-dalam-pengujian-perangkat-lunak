# file: script_80.py:1-20
# asked: {"lines": [13, 14, 16, 18, 19, 20], "branches": [[13, 14], [13, 16], [16, 18], [16, 20], [18, 16], [18, 19]]}
# gained: {"lines": [13, 14, 16, 18, 19, 20], "branches": [[13, 14], [13, 16], [16, 18], [16, 20], [18, 16], [18, 19]]}

import pytest
from script_80 import is_happy


def test_is_happy_length_less_than_3():
    """Test strings with length < 3 return False"""
    assert is_happy("a") == False
    assert is_happy("ab") == False
    assert is_happy("") == False


def test_is_happy_all_distinct_consecutive():
    """Test strings where all 3 consecutive letters are distinct"""
    assert is_happy("abc") == True
    assert is_happy("abcd") == True
    assert is_happy("adb") == True
    assert is_happy("abcdef") == True


def test_is_happy_with_duplicates():
    """Test strings with duplicate consecutive letters"""
    assert is_happy("aabb") == False
    assert is_happy("xyy") == False
    assert is_happy("aaa") == False
    assert is_happy("abcc") == False


def test_is_happy_edge_case_exactly_3():
    """Test string with exactly 3 characters"""
    assert is_happy("xyz") == True
    assert is_happy("xyx") == False
    assert is_happy("xxy") == False
