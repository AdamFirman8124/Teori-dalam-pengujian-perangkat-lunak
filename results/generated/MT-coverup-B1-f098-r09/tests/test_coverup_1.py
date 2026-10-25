# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


def test_count_upper_empty_string():
    # Executes lines 3-7 with a loop body that never runs.
    assert count_upper("") == 0


def test_count_upper_vowels_at_even_indices():
    # 'A' (0), 'I' (2), 'U' (4) are counted; 'E' (1) and 'O' (3) are skipped.
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    # Vowels only at odd indices must not be counted.
    assert count_upper("aXeXe") == 0


def test_count_upper_mixed_case():
    # Lowercase vowels at even indices are not counted (membership in "AEIOU").
    assert count_upper("aEiOu") == 0


def test_count_upper_single_char_vowel():
    assert count_upper("U") == 1


def test_count_upper_single_char_consonant():
    assert count_upper("b") == 0


def test_count_upper_odd_length_string():
    # Last character (even index) is included in the stride-2 range.
    assert count_upper("xOx") == 0


def test_count_upper_odd_length_string_with_vowel():
    # 'O' at index 2 is the final character and is counted.
    assert count_upper("abO") == 1
