# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

from typing import List, Optional

from f012 import longest


def test_longest_empty_list_returns_none():
    result = longest([])
    assert result is None


def test_longest_single_element():
    result = longest(["hello"])
    assert result == "hello"


def test_longest_returns_first_of_max_length():
    result = longest(["a", "bb", "cc", "d"])
    assert result == "bb"


def test_longest_all_same_length_returns_first():
    result = longest(["ab", "cd", "ef"])
    assert result == "ab"
