# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

from f105 import by_length


def test_by_length_all_digits_sorted_reverse():
    result = by_length([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert result == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]


def test_by_length_unsorted_input_gets_sorted_descending():
    result = by_length([2, 1, 3])
    assert result == ["Three", "Two", "One"]


def test_by_length_filters_out_of_range():
    result = by_length([10, 0, -1, 2, 100])
    assert result == ["Two"]


def test_by_length_mixed_valid_and_invalid_preserves_sorted_order():
    result = by_length([1, 10, 9, 0, 5])
    # sorted reverse is [10, 9, 5, 1, 0], invalid 10 and 0 are skipped
    assert result == ["Nine", "Five", "One"]


def test_by_length_empty():
    assert by_length([]) == []


def test_by_length_duplicates():
    result = by_length([3, 3, 1])
    assert result == ["Three", "Three", "One"]


def test_by_length_only_invalid_returns_empty():
    assert by_length([0, 10, -5, 99]) == []
