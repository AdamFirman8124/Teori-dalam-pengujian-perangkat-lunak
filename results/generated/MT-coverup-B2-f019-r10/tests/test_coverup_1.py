# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

from f019 import sort_numbers


def test_sort_numbers_sorts_all_number_words():
    numbers = "nine zero eight one seven two six three five four"

    assert sort_numbers(numbers) == (
        "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_ignores_empty_segments():
    assert sort_numbers("  three   one  two  ") == "one two three"
    assert sort_numbers("   ") == ""
