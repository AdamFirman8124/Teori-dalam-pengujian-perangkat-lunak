# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_all_odd_digit_numbers_are_kept_and_sorted():
    """Covers lines 3-7: init, loop, True branch of the all() check,
    append, and sorted return."""
    result = unique_digits([15, 33, 1357, 1])
    assert result == [1, 15, 33, 1357]
    assert result == sorted(result)


def test_numbers_with_even_digits_are_excluded():
    """Covers the False branch of the all() check on line 5."""
    result = unique_digits([152, 3231, 423, 410])
    assert result == []


def test_empty_input_returns_empty_list():
    """Covers line 3 and line 7 with the loop (line 4) executing zero times."""
    assert unique_digits([]) == []


def test_result_is_sorted_regardless_of_input_order():
    """Verifies the sorted() call on line 7 reorders unsorted input."""
    result = unique_digits([33, 1, 15, 111])
    assert result == [1, 15, 33, 111]
    assert result == sorted(result)


def test_mixed_input_keeps_only_all_odd_digit_numbers():
    """Exercises both branches of line 5 within a single call."""
    result = unique_digits([2, 13, 24, 35, 46, 57, 68, 79])
    assert result == [13, 35, 57, 79]


def test_input_list_is_not_mutated():
    """Postcondition: the function is pure and does not modify its argument."""
    original = [15, 152, 33]
    snapshot = list(original)
    result = unique_digits(original)
    assert original == snapshot
    assert result == [15, 33]
