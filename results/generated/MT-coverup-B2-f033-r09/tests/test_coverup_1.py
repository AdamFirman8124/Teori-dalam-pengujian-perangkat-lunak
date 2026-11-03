# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


@pytest.mark.parametrize(
    ("inp", "expected"),
    [
        # No element at an index divisible by 3 needs reordering.
        ([1, 2, 3], [1, 2, 3]),
        # Classic case: values at indices 0, 3, 6 are sorted, rest untouched.
        ([5, 6, 3, 4, 8, 9, 2], [2, 6, 3, 4, 8, 9, 5]),
        # List whose length is not a multiple of 3.
        ([5, 1, 3, 4, 2], [4, 1, 3, 5, 2]),
        # Full-length list, reversed.
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [3, 8, 7, 6, 5, 4, 9, 2, 1]),
        # Duplicates and negative numbers.
        ([3, -1, 0, 3, -1, 0, 1], [1, -1, 0, 3, -1, 0, 3]),
        # Non-numeric (string) elements.
        (["d", "a", "c", "b"], ["b", "a", "c", "d"]),
        # Degenerate inputs.
        ([], []),
        ([42], [42]),
    ],
)
def test_sort_third(inp, expected):
    result = sort_third(inp)
    assert result == expected
    # Postcondition: indices NOT divisible by 3 must be identical to the input.
    for i, (before, after) in enumerate(zip(inp, result)):
        if i % 3 != 0:
            assert before == after, f"index {i} must be unchanged"


def test_sort_third_does_not_mutate_input():
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = sort_third(original)
    # Postcondition: the input list is left untouched (l = list(l) copies it).
    assert original == snapshot, "input list must not be mutated"
    assert result is not original, "a new list must be returned"
    assert result == [2, 6, 3, 4, 8, 9, 5]


def test_sort_third_empty_returns_new_list():
    original = []
    result = sort_third(original)
    assert result == []
    assert result is not original, "even for an empty input a new list is returned"


def test_sort_third_only_third_positions_sorted():
    inp = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = sort_third(inp)
    # Postcondition: the slice at every third index is sorted...
    assert result[::3] == sorted(inp[::3])
    # ...and equals the expected full result.
    assert result == [3, 1, 2, 6, 4, 5, 9, 7, 8, 10]
