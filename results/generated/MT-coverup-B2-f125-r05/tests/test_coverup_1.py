# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

"""Tests for f125.split_words covering all previously unexecuted lines (3-8).

The function under test is pure (it only inspects its argument and returns a
new value), so it mutates no state and needs no monkeypatching/teardown --
there is no possibility of state pollution between tests.
"""

from f125 import split_words


def test_split_words_with_space():
    # Exercises lines 3-4: space present -> txt.split()
    result = split_words("hello world")
    assert result == ["hello", "world"]


def test_split_words_with_space_takes_precedence_over_comma():
    # Exercises lines 3-4: even with a comma present, the space branch wins,
    # so no comma replacement happens.
    result = split_words("a,b c")
    assert result == ["a,b", "c"]


def test_split_words_with_comma():
    # Exercises lines 5-6: comma but no space -> comma replaced by space, split.
    result = split_words("one,two,three")
    assert result == ["one", "two", "three"]


def test_split_words_else_counts_lowercase_even_ord_chars():
    # Exercises line 8: no space and no comma.
    # 'a' -> ord 97 (odd, not counted), 'b' -> ord 98 (even, counted),
    # 'c' -> ord 99 (odd, not counted).
    result = split_words("abc")
    assert result == 1


def test_split_words_else_ignores_uppercase_and_nonletters():
    # Exercises line 8 branch conditions on the left (false) side:
    # 'B' uppercase -> islower() False; 'b' -> counted; '1' -> not lowercase.
    result = split_words("Bb1")
    assert result == 1


def test_split_words_else_empty_string():
    # Exercises line 8: empty string has neither space nor comma;
    # the comprehension yields an empty list, so the count is 0.
    assert split_words("") == 0
