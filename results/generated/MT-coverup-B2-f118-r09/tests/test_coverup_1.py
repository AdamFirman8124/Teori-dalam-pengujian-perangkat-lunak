# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

"""Tests for f118.get_closest_vowel, covering every line and branch.

The function under test is pure (no I/O, no global state), so no
monkeypatching or teardown is required to avoid state pollution.
"""

from f118 import get_closest_vowel


def test_words_shorter_than_three_return_empty_string():
    """Covers the `len(word) < 3` branch and its early `return ""`."""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_no_vowel_inside_scan_range_returns_empty_string():
    """Covers the loop body's 'not a vowel' branch and the final `return ""`."""
    assert get_closest_vowel("bcdfg") == ""


def test_returns_closest_vowel_scanning_from_the_right():
    """Covers the loop, both neighbour checks, and `return word[i]`."""
    assert get_closest_vowel("cat") == "a"
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("strength") == "e"
    # Uppercase vowels are in the vowel set; lowercase consonants are not.
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("fUlL") == "U"


def test_vowel_with_vowel_right_neighbour_is_skipped():
    """Covers `word[i + 1] not in vowels` evaluating to False."""
    # Only candidate vowel 'a' (index 1) has vowel 'a' as its right neighbour.
    assert get_closest_vowel("baa") == ""
    # The scan continues leftwards and can still succeed afterwards:
    # i=3 'a' fails (right neighbour is a vowel), i=2 'c' skipped,
    # i=1 'a' has consonant neighbours -> returned.
    assert get_closest_vowel("cacaa") == "a"


def test_vowel_with_vowel_left_neighbour_is_skipped():
    """Covers `word[i - 1] not in vowels` evaluating to False
    while the right-neighbour condition holds."""
    # i=2: 'a' has consonant 'b' on the right but vowel 'a' on the left.
    assert get_closest_vowel("baab") == ""


def test_vowel_between_two_vowels_is_skipped():
    """Covers both neighbour conditions failing across loop iterations."""
    # 'quick': i=2 'i' fails on left neighbour 'u'; i=1 'u' fails on right neighbour 'i'.
    assert get_closest_vowel("quick") == ""
