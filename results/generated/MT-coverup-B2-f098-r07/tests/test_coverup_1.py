# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_counts_uppercase_vowels_at_even_indices():
    assert count_upper("AbCdE") == 2


def test_count_upper_returns_zero_when_no_even_indexed_character_is_an_uppercase_vowel():
    assert count_upper("bCd") == 0


def test_count_upper_returns_zero_for_an_empty_string():
    assert count_upper("") == 0
