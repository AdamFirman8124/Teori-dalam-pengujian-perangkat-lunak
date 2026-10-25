# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_empty_string():
    assert count_upper("") == 0


def test_single_upper_vowel_at_even_index():
    assert count_upper("A") == 1
    assert count_upper("E") == 1
    assert count_upper("U") == 1


def test_single_non_vowel_at_even_index():
    assert count_upper("B") == 0
    assert count_upper("a") == 0
    assert count_upper("e") == 0


def test_mixed_even_and_odd_positions():
    # indices 0, 2, 4 are checked: A, I, U -> 3
    assert count_upper("AEIOU") == 3
    # indices 0, 2, 4 are A, C, E -> A and E count -> 2
    assert count_upper("ABCDE") == 2
    # vowel at odd index only should not count: index 0 is 'b', index 1 is 'A'
    assert count_upper("bA") == 0
    # lowercase vowels at even indices should not count
    assert count_upper("aeiou") == 0
    # only index 0 checked for length 2
    assert count_upper("AA") == 1
