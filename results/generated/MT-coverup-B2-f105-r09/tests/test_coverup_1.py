# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_basic_mapping_and_sorting():
    result = by_length([2, 1, 3])
    assert result == ["Three", "Two", "One"]


def test_by_length_all_digits():
    result = by_length([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert result == [
        "Nine", "Eight", "Seven", "Six", "Five",
        "Four", "Three", "Two", "One",
    ]


def test_by_length_empty():
    assert by_length([]) == []


def test_by_length_out_of_range_triggers_exception_branch():
    # Values outside 1..9 hit the bare except and are skipped
    result = by_length([10, 3, 0, -1, 2])
    assert result == ["Three", "Two"]


def test_by_length_duplicates():
    result = by_length([1, 1, 2])
    assert result == ["Two", "One", "One"]


def test_by_length_all_invalid():
    assert by_length([0, 10, -5]) == []
