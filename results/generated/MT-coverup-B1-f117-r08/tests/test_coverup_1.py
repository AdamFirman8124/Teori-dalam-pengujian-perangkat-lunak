# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_matches_requested_consonant_count():
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Hello world", 3) == ["Hello"]
    assert select_words("Hello world", 4) == ["world"]


def test_select_words_handles_vowels_case_and_empty_input():
    assert select_words("AEIOU sky bCd", 0) == ["AEIOU"]
    assert select_words("AEIOU sky bCd", 3) == ["sky", "bCd"]
    assert select_words("", 2) == []
