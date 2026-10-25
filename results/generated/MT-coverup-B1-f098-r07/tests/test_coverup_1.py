# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


def test_count_upper_empty_string():
    assert count_upper("") == 0


def test_count_upper_vowels_at_even_indices():
    # Indices 0, 2, 4 are 'A', 'I', 'U' - all counted.
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    # Indices 0, 2, 4 are 'a', 'e', 'e' - none in "AEIOU".
    assert count_upper("aXeXe") == 0


def test_count_upper_mixed_case():
    # Indices 0, 2, 4 are 'A', 'E', 'I' - all three counted.
    assert count_upper("AbEcI") == 3


def test_count_upper_single_char_vowel():
    assert count_upper("U") == 1


def test_count_upper_single_char_consonant():
    assert count_upper("b") == 0


def test_count_upper_odd_length_string():
    # Indices 0, 2 are 'x', 'A' - last even index is included.
    assert count_upper("xxA") == 1


def test_count_upper_vowel_at_odd_index_not_counted():
    # 'A' is at index 1; indices 0 and 2 are 'x', 'x'.
    assert count_upper("xAx") == 0
