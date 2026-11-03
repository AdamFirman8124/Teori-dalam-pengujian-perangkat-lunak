# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

from f143 import words_in_sentence


def test_words_in_sentence_prime_length_words():
    # Words with prime lengths (2, 3, 5) are kept; words with length 1
    # (flg set immediately) or composite length (flg set in the loop,
    # and len != 2) are filtered out.
    sentence = "a is fun time again world"
    # lengths: a=1, is=2, fun=3, time=4, again=5, world=5
    result = words_in_sentence(sentence)
    assert result == "is fun again world"
    # Verify filtered-out words are truly absent
    assert "a" not in result.split()
    assert "time" not in result.split()


def test_words_in_sentence_single_prime_length_word():
    # A word of length 2 makes range(2, 2) empty (loop never entered)
    # but is still appended due to the len(word) == 2 branch.
    assert words_in_sentence("go") == "go"


def test_words_in_sentence_empty_sentence():
    # Sentence splitting yields no words: the for loop body never runs.
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""
