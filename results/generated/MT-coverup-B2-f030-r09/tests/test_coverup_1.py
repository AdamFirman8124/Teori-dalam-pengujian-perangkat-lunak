# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f030 import get_positive


def test_get_positive_filters_and_preserves_order():
    result = get_positive([-1, 2, -4, 5, 6])
    assert result == [2, 5, 6]


def test_get_positive_empty_list():
    assert get_positive([]) == []


def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3]) == []


def test_get_positive_zero_excluded():
    assert get_positive([0, 1, -0.0, 0.5]) == [1, 0.5]
