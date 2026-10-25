# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_with_at_least_two_distinct_values():
    assert next_smallest([5, 1, 4, 2]) == 2


def test_next_smallest_with_fewer_than_two_distinct_values():
    assert next_smallest([3, 3, 3]) is None


def test_next_smallest_with_empty_list():
    assert next_smallest([]) is None
