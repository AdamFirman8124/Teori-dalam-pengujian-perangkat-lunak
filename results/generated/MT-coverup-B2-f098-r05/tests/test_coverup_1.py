# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f098 import count_upper


def test_count_upper_empty_string():
    # Covers the case where the for-loop body never executes (empty range),
    # exercising the loop-not-taken branch and the return on line 7.
    assert count_upper("") == 0


def test_count_upper_vowels_at_even_indices():
    # Covers lines 3-7: loop executes and the 'if' true branch increments count.
    # Even indices 0, 2, 4 hold 'A', 'I', 'U' -> all uppercase vowels.
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    # Covers the 'if' false branch (s[i] not in "AEIOU"), count stays 0.
    assert count_upper("BCDFG") == 0


def test_count_upper_mixed_characters():
    # Covers both branches of the 'if' within a single loop run.
    # Even indices 0, 2, 4 -> 'A', 'E', 'I' (uppercase vowels).
    assert count_upper("AbEcI") == 3


def test_count_upper_ignores_lowercase_vowels():
    # Lowercase vowels are not counted, exercising the false branch throughout.
    assert count_upper("aeiou") == 0


def test_count_upper_only_even_indices_counted():
    # Uppercase vowels at odd positions must be ignored; only even ones count.
    # "aEbEcIdU": even indices 0,2,4,6 -> 'a', 'b', 'c', 'd' -> none are uppercase vowels.
    assert count_upper("aEbEcIdU") == 0
    # "abEa": even indices 0,2 -> 'a', 'E' -> only 'E' (index 2) is an uppercase vowel;
    # the uppercase vowel 'E' at odd index 1 and lowercase 'a' at index 0 are ignored.
    assert count_upper("abEa") == 1
