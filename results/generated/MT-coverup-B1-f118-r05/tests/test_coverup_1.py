# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import pytest

from f118 import get_closest_vowel


def test_short_word_returns_empty():
    # Covers lines 3-4: len(word) < 3 branch (True path)
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ca") == ""


def test_finds_closest_vowel():
    # Covers lines 6-10: vowel found with non-vowel neighbors
    assert get_closest_vowel("cat") == "a"
    assert get_closest_vowel("full") == "u"
    assert get_closest_vowel("easy") == ""
    # Uppercase vowel with non-vowel neighbors on both sides
    assert get_closest_vowel("qEck") == "E"


def test_no_vowel_returns_empty():
    # Covers line 11: loop completes without finding a vowel
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("bcdfg") == ""


def test_vowel_with_vowel_neighbor_skipped():
    # Covers line 9 False branch: vowel adjacent to another vowel is skipped
    assert get_closest_vowel("aei") == ""
    assert get_closest_vowel("quick") == ""
    # In "HEAD", 'A' has vowel 'E' before it and 'E' has vowel 'A' after it,
    # so no vowel qualifies and the result is ""
    assert get_closest_vowel("HEAD") == ""
