# file: script_12.py:4-20
# asked: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 0], [18, 19], [19, 18], [19, 20]]}
# gained: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 19], [19, 18], [19, 20]]}

import pytest
from script_12 import longest


def test_longest_empty_list():
    """Test that longest returns None for an empty list."""
    result = longest([])
    assert result is None


def test_longest_single_string():
    """Test that longest returns the only string when list has one element."""
    result = longest(['hello'])
    assert result == 'hello'


def test_longest_multiple_strings_different_lengths():
    """Test that longest returns the longest string."""
    result = longest(['a', 'bb', 'ccc'])
    assert result == 'ccc'


def test_longest_multiple_strings_same_length():
    """Test that longest returns the first string when multiple have same length."""
    result = longest(['aa', 'bb', 'cc'])
    assert result == 'aa'


def test_longest_with_longer_string_at_end():
    """Test that longest finds the longest string even if it's at the end."""
    result = longest(['short', 'mid', 'longest'])
    assert result == 'longest'


def test_longest_with_empty_strings():
    """Test that longest handles empty strings in the list."""
    result = longest(['', 'a', ''])
    assert result == 'a'


def test_longest_all_empty_strings():
    """Test that longest returns first empty string when all are empty."""
    result = longest(['', '', ''])
    assert result == ''
