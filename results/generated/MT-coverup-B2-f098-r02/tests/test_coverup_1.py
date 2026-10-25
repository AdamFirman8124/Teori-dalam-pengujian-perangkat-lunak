# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_counts_uppercase_vowels_at_even_indices():
    value = "xYAE"
    assert count_upper(value) == 1


def test_count_upper_returns_zero_for_empty_input():
    assert count_upper("") == 0
