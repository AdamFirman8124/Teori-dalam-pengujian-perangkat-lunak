# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

from f019 import sort_numbers


def test_sort_numbers_sorts_all_number_words_and_ignores_extra_spaces():
    numbers = " nine  zero five two eight one seven three six four "
    assert sort_numbers(numbers) == (
        "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_with_only_spaces_returns_empty_string():
    assert sort_numbers("   ") == ""
