# file: script_113.py:1-17
# asked: {"lines": [13, 14, 15, 16, 17], "branches": [[14, 15], [14, 17]]}
# gained: {"lines": [13, 14, 15, 16, 17], "branches": [[14, 15], [14, 17]]}

import pytest
from script_113 import odd_count


def test_odd_count_single_string_with_odd_digits():
    """Test with a single string containing odd digits."""
    result = odd_count(['1234567'])
    assert result == ["the number of odd elements 4n the str4ng 4 of the 4nput."]


def test_odd_count_multiple_strings():
    """Test with multiple strings."""
    result = odd_count(['3', "11111111"])
    assert result == [
        "the number of odd elements 1n the str1ng 1 of the 1nput.",
        "the number of odd elements 8n the str8ng 8 of the 8nput."
    ]


def test_odd_count_empty_list():
    """Test with an empty list."""
    result = odd_count([])
    assert result == []


def test_odd_count_string_with_no_odd_digits():
    """Test with a string containing only even digits."""
    result = odd_count(['2468'])
    assert result == ["the number of odd elements 0n the str0ng 0 of the 0nput."]


def test_odd_count_string_with_all_odd_digits():
    """Test with a string containing only odd digits."""
    result = odd_count(['13579'])
    assert result == ["the number of odd elements 5n the str5ng 5 of the 5nput."]


def test_odd_count_mixed_strings():
    """Test with multiple strings having different counts of odd digits."""
    result = odd_count(['123', '2468', '13579'])
    assert result == [
        "the number of odd elements 2n the str2ng 2 of the 2nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
        "the number of odd elements 5n the str5ng 5 of the 5nput."
    ]
