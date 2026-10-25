# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest_distinct():
    assert next_smallest([4, 1, 3, 2]) == 2


def test_next_smallest_ignores_duplicates():
    assert next_smallest([1, 1, 1, 2]) == 2


def test_next_smallest_returns_none_for_single_element():
    assert next_smallest([5]) is None


def test_next_smallest_returns_none_for_duplicates_only():
    assert next_smallest([7, 7, 7]) is None


def test_next_smallest_returns_none_for_empty_list():
    assert next_smallest([]) is None
