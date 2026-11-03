# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


@pytest.mark.parametrize(
    "numbers, expected",
    [
        # Unsorted input exercises the value_map lookup and the sort.
        ("three one five", "one three five"),
        # Reverse-sorted input: every element must be reordered.
        (
            "nine eight seven six five four three two one zero",
            "zero one two three four five six seven eight nine",
        ),
        # Already-sorted input still exercises the full pipeline.
        ("zero one two", "zero one two"),
        # Single element.
        ("five", "five"),
        # Duplicates: sorted() is stable, so equal keys keep relative order.
        ("three one three", "one three three"),
        # Extra spaces: the comprehension's `if x` branch filters out
        # empty tokens produced by split(' ').
        ("two  one   three", "one two three"),
        # Empty string: split(' ') yields [''], filtered out -> empty result.
        ("", ""),
        ("   ", ""),
        # All ten words, shuffled.
        (
            "four nine one seven zero five two eight six three",
            "zero one two three four five six seven eight nine",
        ),
    ],
)
def test_sort_numbers(numbers, expected):
    result = sort_numbers(numbers)
    assert result == expected


def test_sort_numbers_output_is_valid_number_words():
    result = sort_numbers("nine one five")
    assert all(word in {"zero", "one", "two", "three", "four", "five",
                        "six", "seven", "eight", "nine"} for word in result.split(" "))


def test_sort_numbers_is_pure():
    # The function must not mutate its input or any shared state.
    original = "three one two"
    snapshot = original
    assert sort_numbers(original) == "one two three"
    assert original == snapshot
