# file: script_74.py:1-26
# asked: {"lines": [15, 16, 17, 19, 20, 21, 23, 24, 26], "branches": [[16, 17], [16, 19], [20, 21], [20, 23], [23, 24], [23, 26]]}
# gained: {"lines": [15, 16, 17, 19, 20, 21, 23, 24, 26], "branches": [[16, 17], [16, 19], [20, 21], [20, 23], [23, 24], [23, 26]]}

import pytest
from script_74 import total_match


def test_total_match_empty_lists():
    """Test with both lists empty"""
    assert total_match([], []) == []


def test_total_match_first_list_shorter():
    """Test when first list has fewer total characters"""
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']


def test_total_match_second_list_shorter():
    """Test when second list has fewer total characters"""
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']


def test_total_match_first_list_equal():
    """Test when both lists have equal total characters"""
    # ['hi', 'admin'] = 2 + 5 = 7 chars
    # ['abc', 'defg'] = 3 + 4 = 7 chars
    assert total_match(['hi', 'admin'], ['abc', 'defg']) == ['hi', 'admin']


def test_total_match_single_vs_multiple():
    """Test single element vs multiple elements"""
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']


def test_total_match_first_empty_second_nonempty():
    """Test when first list is empty and second is not"""
    assert total_match([], ['a', 'b']) == []


def test_total_match_first_nonempty_second_empty():
    """Test when first list is not empty and second is empty"""
    assert total_match(['a', 'b'], []) == []


def test_total_match_both_single_element():
    """Test with both lists having single elements"""
    assert total_match(['abc'], ['ab']) == ['ab']
    assert total_match(['ab'], ['abc']) == ['ab']
