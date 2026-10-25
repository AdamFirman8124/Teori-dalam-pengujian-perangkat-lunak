# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_empty_string():
    assert count_upper("") == 0


def test_count_upper_vowel_at_even_index():
    assert count_upper("A") == 1
    assert count_upper("E") == 1


def test_count_upper_non_vowel_at_even_index():
    assert count_upper("B") == 0
    assert count_upper("a") == 0


def test_count_upper_multiple_even_indices_mixed():
    assert count_upper("AXBY") == 1
    assert count_upper("ABEC") == 2
    assert count_upper("BXDX") == 0


def test_count_upper_odd_indices_ignored():
    assert count_upper("BA") == 0
    assert count_upper("aA") == 0
    assert count_upper("XAXE") == 0
