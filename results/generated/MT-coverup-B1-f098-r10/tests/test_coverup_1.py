# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_empty():
    assert count_upper("") == 0


def test_count_upper_single_upper_vowel_at_even_index():
    assert count_upper("A") == 1
    assert count_upper("E") == 1


def test_count_upper_single_non_vowel_at_even_index():
    assert count_upper("B") == 0
    assert count_upper("a") == 0


def test_count_upper_mixed_even_odd_positions():
    # even indices 0,2,4 are A,I,U -> 3; odd indices ignored
    assert count_upper("AEIOU") == 3
    # vowel at odd index only should not count: index 0 is B
    assert count_upper("BA") == 0
    # lowercase vowels at even indices should not count
    assert count_upper("aeiou") == 0
    # multiple even positions: 0:A yes, 2:E yes, 4:I yes, 6:O yes, 8:U yes
    assert count_upper("ABECIDOFU") == 5
    # no vowel at even indices
    assert count_upper("BCDFG") == 0
