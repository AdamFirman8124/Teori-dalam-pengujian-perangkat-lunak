# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_empty_list():
    assert unique_digits([]) == []


def test_unique_digits_all_odd_digits():
    assert unique_digits([1, 3, 135, 975]) == [1, 3, 135, 975]


def test_unique_digits_mixed():
    assert unique_digits([15, 33, 1422, 1, 12, 135]) == [1, 15, 33, 135]


def test_unique_digits_no_odd_digit_numbers():
    assert unique_digits([2, 24, 100, 468]) == []


def test_unique_digits_negative_and_duplicates():
    # Negative numbers: str(-15) contains '-' which raises ValueError on int(c)
    # is not exercised here; only non-negative inputs are covered by the source.
    assert unique_digits([135, 135, 11]) == [11, 135, 135]


def test_unique_digits_result_is_sorted():
    result = unique_digits([971, 13, 5])
    assert result == [5, 13, 971]
    assert result == sorted(result)
