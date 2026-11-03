# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    result = compare([1, 2, 3], [4, 5, 3])
    assert result == [3, 3, 0]


def test_compare_with_negative_differences():
    result = compare([5, 0, -2], [2, 3, 1])
    assert result == [3, 3, 3]


def test_compare_with_empty_lists():
    result = compare([], [])
    assert result == []
