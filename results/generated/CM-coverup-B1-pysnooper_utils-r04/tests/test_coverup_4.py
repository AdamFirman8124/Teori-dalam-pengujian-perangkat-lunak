# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper.utils import truncate


def test_truncate_returns_string_when_max_length_is_none():
    string = "abcdefghijklmnopqrstuvwxyz"
    result = truncate(string, None)
    assert result == string
    assert result is string


def test_truncate_returns_string_when_length_equals_max_length():
    string = "abcdefghij"
    result = truncate(string, 10)
    assert result == string
    assert result is string


def test_truncate_returns_string_when_shorter_than_max_length():
    string = "abc"
    result = truncate(string, 10)
    assert result == string
    assert result is string


def test_truncate_shortens_long_string_with_ellipsis():
    string = "abcdefghijklmnopqrstuvwxyz"
    max_length = 10
    result = truncate(string, max_length)

    assert result != string
    assert len(result) == max_length
    assert "..." in result
    assert result.startswith(string[:3])
    assert result.endswith(string[-4:])
    assert result == "abc...wxyz"


def test_truncate_odd_max_length_splits_remainder_to_right():
    string = "0123456789abcdefghij"
    max_length = 11
    result = truncate(string, max_length)

    # left = (11 - 3) // 2 = 4, right = 11 - 3 - 4 = 4
    assert result == "0123...ghij"
    assert len(result) == max_length


def test_truncate_even_max_length_splits_evenly():
    string = "0123456789abcdefghij"
    max_length = 12
    result = truncate(string, max_length)

    # left = (12 - 3) // 2 = 4, right = 12 - 3 - 4 = 5
    assert result == "0123...fghij"
    assert len(result) == max_length


def test_truncate_minimal_max_length_keeps_only_tail():
    string = "abcdef"
    result = truncate(string, 4)

    # left = (4 - 3) // 2 = 0, right = 4 - 3 - 0 = 1
    assert result == "...f"
    assert len(result) == 4


def test_truncate_empty_string_is_returned_unchanged():
    result = truncate("", 5)
    assert result == ""
