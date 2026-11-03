# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

"""Tests for f153.Strongest_Extension.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required; each test works only
on local data, avoiding any state pollution.
"""

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    """No later extension beats the first: loop runs, if-body never taken."""
    # "AAaa" -> 2 upper, 2 lower -> val 0; "Aa" -> 0; "a" -> -1.
    assert Strongest_Extension("Cls", ["AAaa", "Aa", "a"]) == "Cls.AAaa"


def test_later_extension_is_strongest():
    """A later extension has a strictly greater value: if-body executes."""
    # "a" -> -1; "AA" -> 2 (becomes strongest); "Aa" -> 0 (not greater).
    assert Strongest_Extension("Cls", ["a", "AA", "Aa"]) == "Cls.AA"


def test_middle_extension_is_strongest():
    """The strongest extension appears in the middle of the list."""
    # "AA" -> 2; "AAA" -> 3 (becomes strongest); "Aa" -> 0; "AA" -> 2.
    assert Strongest_Extension("my_class", ["AA", "AAA", "Aa", "AA"]) == "my_class.AAA"


def test_single_extension():
    """Single-element list: loop runs once, comparison branch not taken."""
    # "AbC" -> 2 upper, 1 lower -> val 1.
    assert Strongest_Extension("S", ["AbC"]) == "S.AbC"


def test_ties_keep_first():
    """Equal values must not replace the current strongest (false branch)."""
    # "AA" -> 2 and "BB" -> 2 tie, so the first one is kept.
    assert Strongest_Extension("T", ["AA", "BB"]) == "T.AA"


def test_non_alpha_characters_are_ignored():
    """Non-alphabetic characters do not affect the strength value."""
    # "!@#AAaa" -> 2 upper, 2 lower -> 0; "A!" -> 1 upper, 0 lower -> 1.
    assert Strongest_Extension("N", ["!@#AAaa", "A!"]) == "N.A!"
