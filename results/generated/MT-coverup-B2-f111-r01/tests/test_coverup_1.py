# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

import pytest

from f111 import histogram


def test_histogram_single_most_frequent_word():
    result = histogram("apple banana apple")
    assert result == {"apple": 2}


def test_histogram_ties_all_included():
    result = histogram("cat dog cat dog bird")
    assert result == {"cat": 2, "dog": 2}


def test_histogram_single_word():
    result = histogram("hello")
    assert result == {"hello": 1}


def test_histogram_empty_string_returns_empty_dict():
    result = histogram("")
    assert result == {}


def test_histogram_only_spaces_returns_empty_dict():
    result = histogram("   ")
    assert result == {}


def test_histogram_ignores_empty_tokens():
    result = histogram("a  a b")
    assert result == {"a": 2}
