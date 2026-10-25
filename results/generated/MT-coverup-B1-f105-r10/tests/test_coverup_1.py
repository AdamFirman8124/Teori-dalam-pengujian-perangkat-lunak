# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_basic():
    result = by_length([2, 1, 1, 4, 5, 8, 2, 3])
    assert result == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]


def test_by_length_empty():
    assert by_length([]) == []


def test_by_length_out_of_range_ignored():
    # Values outside 1..9 are silently skipped (bare except branch)
    assert by_length([10, 0, -1, 5]) == ["Five"]


def test_by_length_all_digits():
    assert by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]


def test_by_length_does_not_mutate_input():
    arr = [3, 1, 2]
    by_length(arr)
    assert arr == [3, 1, 2]
