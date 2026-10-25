# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

from f143 import words_in_sentence


def test_words_in_sentence_covers_word_length_branches():
    assert words_in_sentence("a to cat moon") == "to cat"


def test_words_in_sentence_with_empty_input():
    assert words_in_sentence("") == ""
