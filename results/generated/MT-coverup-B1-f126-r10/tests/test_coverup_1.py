# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_true():
    assert is_sorted([1, 2, 3, 4]) is True


def test_is_sorted_false_unsorted():
    assert is_sorted([1, 3, 2, 4]) is False


def test_is_sorted_false_too_many_duplicates():
    assert is_sorted([1, 1, 1, 2]) is False


def test_is_sorted_empty_list():
    assert is_sorted([]) is True


def test_is_sorted_single_element():
    assert is_sorted([5]) is True


def test_is_sorted_duplicates_allowed():
    assert is_sorted([1, 1, 2, 2]) is True
