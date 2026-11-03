# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_all_odd_digits_sorted():
    """All elements consist only of odd digits; result must be sorted ascending."""
    result = unique_digits([15, 33, 1])
    assert result == [1, 15, 33]
    assert result == sorted(result)


def test_unique_digits_excludes_numbers_with_even_digits():
    """Every element contains at least one even digit, so nothing is kept."""
    assert unique_digits([152, 323, 1422, 10]) == []


def test_unique_digits_mixed_input_with_duplicates():
    """Mix of qualifying and non-qualifying numbers, including duplicates."""
    result = unique_digits([135, 103, 31, 135, 2, 7])
    assert result == [7, 31, 135, 135]


def test_unique_digits_empty_input():
    """Empty input yields an empty result (loop body never runs)."""
    assert unique_digits([]) == []


def test_unique_digits_single_element():
    assert unique_digits([9]) == [9]


def test_unique_digits_zero_and_even_digits_filtered():
    """0 is an even digit, so numbers containing it are filtered out."""
    assert unique_digits([0, 2, 4, 6, 8]) == []
