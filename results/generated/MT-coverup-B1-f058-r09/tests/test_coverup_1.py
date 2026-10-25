# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_matches():
    result = common([1, 2, 3, 4], [3, 4, 5])
    assert result == [3, 4]


def test_common_without_matches():
    result = common([1, 2], [3, 4])
    assert result == []


def test_common_with_duplicates():
    result = common([2, 2, 1, 1], [1, 1, 2, 2])
    assert result == [1, 2]


def test_common_empty_lists():
    result = common([], [])
    assert result == []


def test_common_unsorted_input():
    result = common([9, 5, 1], [1, 9, 5])
    assert result == [1, 5, 9]
