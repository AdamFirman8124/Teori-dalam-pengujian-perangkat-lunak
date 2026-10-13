# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

from script_9 import rolling_max


def test_rolling_max_empty_input_covers_lines_10_to_21():
    result = rolling_max([])
    assert result == []


def test_rolling_max_single_element_exercises_first_iteration_branch():
    result = rolling_max([5])
    assert result == [5]


def test_rolling_max_docstring_example_exercises_both_branches():
    result = rolling_max([1, 2, 3, 2, 3, 4, 2])
    assert result == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_strictly_decreasing_list_postcondition():
    result = rolling_max([9, 8, 7, 6, 5])
    assert result == [9, 9, 9, 9, 9]


def test_rolling_max_with_negatives_exercises_max_branch():
    result = rolling_max([-3, -1, -7, -2])
    assert result == [-3, -1, -1, -1]


def test_rolling_max_result_length_matches_input():
    numbers = [4, 1, 4, 2, 9, 3]
    result = rolling_max(numbers)
    assert len(result) == len(numbers)
    assert result == [4, 4, 4, 4, 9, 9]


def test_rolling_max_does_not_mutate_input():
    numbers = [1, 3, 2, 5, 4]
    original = list(numbers)
    rolling_max(numbers)
    assert numbers == original
