# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_empty_list():
    result = unique_digits([])
    assert result == []
    assert isinstance(result, list)


def test_unique_digits_all_odd_digits():
    assert unique_digits([1, 3, 5, 7, 9, 11, 99, 135]) == [1, 3, 5, 7, 9, 11, 99, 135]


def test_unique_digits_filters_even_digits():
    # 2, 4, 10, 12, 100 contain at least one even digit -> dropped
    assert unique_digits([1, 2, 3, 4, 10, 12, 100, 135]) == [1, 3, 135]


def test_unique_digits_returns_sorted():
    assert unique_digits([99, 1, 31, 7, 5]) == [1, 5, 7, 31, 99]


def test_unique_digits_no_matches():
    assert unique_digits([2, 4, 6, 8, 20, 246]) == []


def test_unique_digits_zero_is_even_digit():
    assert unique_digits([0, 1]) == [1]


def test_unique_digits_does_not_mutate_input():
    data = [31, 2, 5]
    snapshot = list(data)
    unique_digits(data)
    assert data == snapshot


def test_unique_digits_accepts_tuple_and_generator():
    assert unique_digits((3, 4, 57)) == [3, 57]
    assert unique_digits(i for i in [9, 8, 11]) == [9, 11]


def test_unique_digits_negative_raises_value_error():
    with pytest.raises(ValueError):
        unique_digits([-1])
