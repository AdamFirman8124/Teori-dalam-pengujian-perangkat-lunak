# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_counts_consonants_case_insensitively():
    assert select_words("Mary had A little lamb", 3) == ["Mary", "lamb"]


def test_select_words_handles_vowels_and_empty_input():
    assert select_words("a E IOU rhythm", 0) == ["a", "E", "IOU"]
    assert select_words("", 2) == []
