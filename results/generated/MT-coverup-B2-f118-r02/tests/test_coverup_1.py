# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

from f118 import get_closest_vowel


def test_words_shorter_than_three_return_empty_string():
    # Exercises lines 3-4: early return when len(word) < 3.
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("B") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("xY") == ""


def test_returns_vowel_between_consonants():
    # Exercises lines 6-10: 'u' at index 3 of "yogurt" has consonants
    # ('g' and 'r') on both sides, so it is the closest qualifying vowel.
    assert get_closest_vowel("yogurt") == "u"
    # Boundary case: minimum length (3) that can return a vowel.
    assert get_closest_vowel("cat") == "a"
    # Uppercase vowel taken from the vowels set.
    assert get_closest_vowel("FULL") == "U"


def test_returns_empty_when_no_vowel_qualifies():
    # Exercises line 11: the loop finishes without finding a match.
    # In "quick": 'i' is preceded by the vowel 'u', and 'u' is followed
    # by the vowel 'i', so neither qualifies.
    assert get_closest_vowel("quick") == ""
    # All-consonant word: the inner branch on line 9 is never reached
    # (False branch of line 8), so the final return is used.
    assert get_closest_vowel("rhythm") == ""


def test_vowel_adjacent_to_vowel_is_skipped():
    # Covers the False outcomes of the condition on line 9.
    # "beat": 'a' is preceded by the vowel 'e'; 'e' is followed by the
    # vowel 'a' (short-circuits the first sub-condition).
    assert get_closest_vowel("beat") == ""
    # "baed": 'e' is followed by a consonant but preceded by the vowel
    # 'a' (False second sub-condition); 'a' is followed by the vowel 'e'.
    assert get_closest_vowel("baed") == ""
