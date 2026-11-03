# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_mixed_input_covers_all_lines():
    # Covers: list init (line 3), loop (line 4), all() True/False branches (line 5),
    # append (line 6) and return sorted (line 7).
    x = [15, 20, 135, 1]
    result = unique_digits(x)
    # 15 -> digits 1,5 (all odd) kept; 20 -> digit 2 even, skipped;
    # 135 -> all odd, kept; 1 -> odd, kept. Result must be sorted.
    assert result == [1, 15, 135]
    # Postcondition: input list is not mutated (function is pure).
    assert x == [15, 20, 135, 1]


def test_unique_digits_empty_input():
    # Covers the loop-not-entered branch (line 4 with empty iterable).
    assert unique_digits([]) == []


def test_unique_digits_no_matches():
    # Covers the False branch of the all() check for every element,
    # including single-digit even numbers and zero.
    assert unique_digits([2, 24, 100, 0]) == []


def test_unique_digits_all_matches_sorted():
    # Every element passes the filter; verifies sorted output ordering.
    assert unique_digits([3, 111, 5, 9]) == [3, 5, 9, 111]


def test_unique_digits_duplicates_preserved():
    # sorted() is stable and keeps duplicates.
    assert unique_digits([11, 2, 11]) == [11, 11]
