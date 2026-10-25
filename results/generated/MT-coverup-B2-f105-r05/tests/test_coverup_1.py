# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_full_mapping():
    # covers dict construction (lines 3-13), sorting (line 14),
    # loop and successful append (lines 16-18)
    result = by_length([2, 1, 1, 4, 5, 8, 2, 3])
    assert result == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]


def test_by_length_skips_out_of_range_values():
    # covers the except branch (lines 19-20) for values not in the dict
    result = by_length([10, 0, -1, 3])
    assert result == ["Three"]


def test_by_length_empty_input():
    # covers loop body never executing; still exercises lines 3-15, 21
    assert by_length([]) == []


def test_by_length_all_invalid():
    # covers only the except branch, then return
    assert by_length([100, 42]) == []


def test_by_length_reverse_order():
    # verifies descending sort of the input before mapping
    result = by_length([9, 1, 5])
    assert result == ["Nine", "Five", "One"]
