# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

from f105 import by_length


def test_by_length_basic_mapping_and_descending_order():
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    result = by_length(arr)
    assert result == [
        "Eight",
        "Five",
        "Four",
        "Three",
        "Two",
        "Two",
        "One",
        "One",
    ]
    # Postcondition: the input list is not mutated.
    assert arr == [2, 1, 1, 4, 5, 8, 2, 3]


def test_by_length_empty_array():
    # Covers the loop-exit branch with zero iterations.
    assert by_length([]) == []


def test_by_length_skips_numbers_outside_1_to_9():
    # Exercises the except branch (KeyError -> pass).
    assert by_length([10, 0, -1, 3]) == ["Three"]


def test_by_length_all_numbers_outside_range():
    # Every lookup fails; result must be empty.
    assert by_length([10, 0, -1]) == []


def test_by_length_single_element():
    assert by_length([9]) == ["Nine"]


def test_by_length_duplicates_preserved():
    assert by_length([5, 5, 5]) == ["Five", "Five", "Five"]


def test_by_length_unhashable_element_is_skipped():
    # Exercises the except branch via TypeError (unhashable dict key).
    assert by_length([[2], [1]]) == []
