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
    # Even indices are 'a', 'e', 'e' - lowercase, not counted.
    assert count_upper("aXeXe") == 0


def test_count_upper_mixed_case():
    # Even indices are 'a', 'i', 'u' - lowercase, not counted.
    assert count_upper("aEiOu") == 0


def test_count_upper_single_char_vowel():
    assert count_upper("U") == 1


def test_count_upper_single_char_consonant():
    assert count_upper("b") == 0


def test_count_upper_odd_length_string():
    # Indices 0 and 2 are 'O', 'O' - both counted.
    assert count_upper("OxO") == 2


def test_count_upper_vowels_only_at_odd_indices():
    # Even indices are 'x', 'x', 'x' - vowels at odd indices not counted.
    assert count_upper("xAxEx") == 0
