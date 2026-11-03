# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

"""Tests for f117.select_words covering all lines and branches."""

from f117 import select_words


def test_select_words_empty_string_skips_loop():
    """Empty input: 'result = []' runs, the for-loop body never runs, return [] happens."""
    assert select_words("", 3) == []
    assert select_words("", 0) == []


def test_select_words_basic_counts():
    """Covers vowel branch (condition False), consonant branch (True), both branches
    of the n_consonants == n check, and result.append."""
    # 'Mary'  -> M, r, y            = 3 consonants
    # 'had'   -> h, d               = 2 consonants
    # 'a'     -> no consonants      = 0
    # 'little'-> l, t, t, l         = 4 consonants
    # 'lamb'  -> l, m, b            = 3 consonants
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("Mary had a little lamb", 2) == ["had"]
    assert select_words("Mary had a little lamb", 0) == ["a"]


def test_select_words_uppercase_vowels_lowered():
    """Covers the .lower() call mapping uppercase vowels into the vowel set."""
    # 'PYTHON' -> P, Y, T, H, N = 5 consonants ('O' is a vowel, case-insensitively)
    assert select_words("PYTHON", 5) == ["PYTHON"]
    # 'AEIOUxyz' -> x, y, z = 3 consonants (all uppercase vowels ignored)
    assert select_words("AEIOUxyz", 3) == ["AEIOUxyz"]


def test_select_words_no_matches_returns_empty_list():
    """Covers the False branch of the final equality check for every word."""
    assert select_words("a e i o u", 1) == []      # 0 consonants each
    assert select_words("hello world", 10) == []   # 3 and 4 consonants


def test_select_words_single_word_no_spaces():
    """Single word input still exercises the outer loop and append path."""
    assert select_words("cat", 2) == ["cat"]
    assert select_words("cat", 3) == []
