# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f030 import get_positive


def test_get_positive_filters_and_preserves_order():
    result = get_positive([-1, 2, -3, 4, 0, 5])
    assert result == [2, 4, 5]


def test_get_positive_all_negative_returns_empty():
    assert get_positive([-1, -2, -3]) == []


def test_get_positive_empty_list():
    assert get_positive([]) == []


def test_get_positive_all_positive():
    assert get_positive([1, 2, 3]) == [1, 2, 3]
