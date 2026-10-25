# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

from typing import List, Optional

from f012 import longest


def test_longest_empty_list_returns_none():
    result: Optional[str] = longest([])
    assert result is None


def test_longest_single_element():
    result = longest(["hello"])
    assert result == "hello"


def test_longest_returns_first_max():
    result = longest(["a", "abc", "xy", "abc"])
    assert result == "abc"


def test_longest_multiple_strings():
    result = longest(["one", "three", "four"])
    assert result == "three"
