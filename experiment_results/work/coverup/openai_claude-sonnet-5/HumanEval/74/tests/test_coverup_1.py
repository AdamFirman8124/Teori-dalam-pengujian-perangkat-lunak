# file: script_74.py:1-26
# asked: {"lines": [15, 16, 17, 19, 20, 21, 23, 24, 26], "branches": [[16, 17], [16, 19], [20, 21], [20, 23], [23, 24], [23, 26]]}
# gained: {"lines": [15, 16, 17, 19, 20, 21, 23, 24, 26], "branches": [[16, 17], [16, 19], [20, 21], [20, 23], [23, 24], [23, 26]]}

import pytest
from script_74 import total_match


def test_total_match_empty_lists():
    """Test with two empty lists."""
    assert total_match([], []) == []


def test_total_match_first_list_shorter():
    """Test when first list has fewer total characters."""
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']


def test_total_match_second_list_shorter():
    """Test when second list has fewer total characters."""
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']


def test_total_match_first_list_shorter_multiple():
    """Test when first list has fewer total characters with multiple strings."""
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']


def test_total_match_single_vs_multiple():
    """Test with single element vs multiple elements."""
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']


def test_total_match_equal_length():
    """Test when both lists have equal total characters - should return first list."""
    assert total_match(['ab', 'cd'], ['ef', 'gh']) == ['ab', 'cd']


def test_total_match_first_empty():
    """Test when first list is empty and second is not."""
    assert total_match([], ['hello']) == []


def test_total_match_second_empty():
    """Test when second list is empty and first is not."""
    assert total_match(['hello'], []) == []


def test_total_match_first_list_longer():
    """Test when first list has more total characters."""
    assert total_match(['hello', 'world'], ['hi']) == ['hi']
