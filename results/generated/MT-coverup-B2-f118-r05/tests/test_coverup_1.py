# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

"""Tests for f118.get_closest_vowel, targeting lines 3-11.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
leaves no residual state behind.
"""

from f118 import get_closest_vowel


def test_words_shorter_than_three_characters_return_empty():
    # Lines 3-4: the len(word) < 3 early-return branch (True case).
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_vowel_with_consonant_neighbours_is_returned():
    # Lines 6-10: loop iterates, finds a vowel whose neighbours on both
    # sides are non-vowels, and returns it.
    assert get_closest_vowel("cat") == "a"
    assert get_closest_vowel("full") == "u"
    assert get_closest_vowel("strongest") == "e"


def test_uppercase_vowels_are_recognised():
    # Lines 6/8: uppercase letters are members of the vowels set.
    assert get_closest_vowel("cAt") == "A"
    assert get_closest_vowel("bESt") == "E"


def test_right_neighbour_vowel_rejects_candidate_and_loop_continues():
    # Line 9: (word[i+1] not in vowels) evaluates False, so the candidate
    # is skipped; the loop keeps running and a lower-index vowel qualifies.
    # "cataa": i=3 'a' rejected (right neighbour 'a'), i=1 'a' accepted.
    assert get_closest_vowel("cataa") == "a"


def test_left_neighbour_vowel_rejects_candidate_and_loop_continues():
    # Line 9: (word[i+1] not in vowels) is True but
    # (word[i-1] not in vowels) is False -> candidate skipped, loop
    # continues and eventually succeeds.
    # "cataac": i=4 'a' rejected (left neighbour 'a'),
    #           i=3 'a' rejected (right neighbour 'a'),
    #           i=1 'a' accepted.
    assert get_closest_vowel("cataac") == "a"


def test_no_vowels_at_all_returns_empty():
    # Line 11: loop exhausts without the inner if ever firing.
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("bcdfg") == ""


def test_interior_vowels_found_but_all_rejected_returns_empty():
    # Lines 7-9 exercised with vowels found yet every candidate rejected
    # (vowel neighbours), falling through to line 11.
    assert get_closest_vowel("aei") == ""   # i=1 'e': right neighbour 'i'
    assert get_closest_vowel("baa") == ""   # i=1 'a': right neighbour 'a'
    assert get_closest_vowel("baat") == ""  # i=2 'a': left neighbour 'a';
                                            # i=1 'a': right neighbour 'a'


def test_vowels_at_the_edges_are_never_considered():
    # Line 7: range(len(word)-2, 0, -1) excludes index 0 and the last
    # index, so vowels sitting at the boundaries cannot be returned.
    assert get_closest_vowel("aba") == ""   # only 'b' (index 1) inspected
    assert get_closest_vowel("eye") == ""   # only 'y' (index 1) inspected
