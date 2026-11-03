# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

"""Tests for f125.split_words covering all previously unexecuted lines 3-8.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
leaves no residual state behind.
"""

from f125 import split_words


def test_space_branch_returns_split_list():
    """Lines 3-4: input containing a space is split on whitespace."""
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a b c") == ["a", "b", "c"]
    # Multiple/leading/trailing spaces: str.split() drops empties.
    assert split_words("  hello   world  ") == ["hello", "world"]
    # A space takes precedence over a comma.
    assert split_words("one,two three") == ["one,two", "three"]


def test_comma_branch_replaces_commas_and_splits():
    """Lines 5-6: no space but a comma -> commas become split points."""
    assert split_words("one,two,three") == ["one", "two", "three"]
    # Commas are replaced by spaces, then split() runs with no separator,
    # which collapses consecutive separators and drops leading/trailing ones.
    assert split_words(",a,,b,") == ["a", "b"]
    assert split_words("a,b,c") == ["a", "b", "c"]
    # A single comma still takes the elif branch.
    assert split_words("x,y") == ["x", "y"]


def test_else_branch_counts_lowercase_even_ordinals():
    """Lines 7-8: no space, no comma -> count lowercase chars with even ord."""
    # b=98, d=100, f=102 are even; a=97, c=99, e=101 are odd.
    assert split_words("abcdef") == 3
    # Uppercase letters and non-letters are never counted.
    assert split_words("ABcD") == 0
    assert split_words("123!@#") == 0
    # Empty string takes the else branch and counts nothing.
    assert split_words("") == 0
    # Mixed case: b(98) and d(100) count; A, F do not.
    assert split_words("bAdF") == 2
