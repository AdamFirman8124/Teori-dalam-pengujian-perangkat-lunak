# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from script_7 import filter_by_substring

def test_filter_by_substring_empty():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_no_match():
    assert filter_by_substring(['abc', 'def'], 'z') == []

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['abc', ''], '') == ['abc', '']
