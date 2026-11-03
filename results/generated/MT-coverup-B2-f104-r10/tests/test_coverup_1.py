# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_mixed_elements_covers_all_lines_and_branches():
    # Covers line 3 (list init), line 4 (loop), line 5 (both True and False
    # outcomes of the all(...) check), line 6 (append), and line 7 (return).
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]


def test_unique_digits_no_element_matches():
    # Loop body runs, all(...) is False for every element, append never runs.
    assert unique_digits([152, 323, 1423, 10]) == []


def test_unique_digits_empty_input():
    # Zero loop iterations; still exercises init (line 3) and return (line 7).
    assert unique_digits([]) == []


def test_unique_digits_sorts_ascending():
    # Matching elements supplied out of order must come back sorted (line 7).
    assert unique_digits([135, 7, 979, 31]) == [7, 31, 135, 979]


def test_unique_digits_single_even_digits():
    # Single-digit even numbers never satisfy the all(...) condition.
    assert unique_digits([0, 2, 4, 6, 8]) == []


def test_unique_digits_all_match():
    # Every element takes the True branch of the all(...) check (line 6).
    assert unique_digits([11, 3, 555]) == [3, 11, 555]


def test_unique_digits_does_not_mutate_input():
    # Postcondition: the input list is left untouched (no state pollution).
    original = [11, 20, 13]
    snapshot = list(original)
    result = unique_digits(original)
    assert original == snapshot
    assert result == [11, 13]
