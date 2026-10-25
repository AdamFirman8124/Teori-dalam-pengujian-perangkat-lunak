# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

import pytest

from f111 import histogram


def test_histogram_basic():
    result = histogram("a b a")
    assert result == {"a": 2}


def test_histogram_all_ties():
    result = histogram("a b")
    assert result == {"a": 1, "b": 1}


def test_histogram_empty_input():
    assert histogram("") == {}


def test_histogram_empty_tokens():
    result = histogram("  a a")
    assert result == {"": 2, "a": 2}


def test_histogram_single_word():
    result = histogram("hello")
    assert result == {"hello": 1}
