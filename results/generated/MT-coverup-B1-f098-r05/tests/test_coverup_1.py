# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_counts_vowels_at_even_indices():
    assert count_upper("AxExIxOxU") == 5


def test_count_upper_ignores_non_vowels_and_odd_indices():
    assert count_upper("aAeEiIoOuU") == 0


def test_count_upper_with_empty_string():
    assert count_upper("") == 0
