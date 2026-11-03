# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    """No later extension beats the first: the branch at line 7 is never taken."""
    result = Strongest_Extension("Sli", ["SErviCS", "list"])
    assert result == "Sli.SErviCS"


def test_later_extension_is_strongest():
    """A later extension has a strictly greater value: branch at line 7 is taken."""
    result = Strongest_Extension("my_class", ["aB", "CC"])
    assert result == "my_class.CC"


def test_tie_keeps_first_extension():
    """Equal values never replace the current strongest (strict '>' comparison)."""
    result = Strongest_Extension("C", ["Ab", "Cd"])
    assert result == "C.Ab"


def test_single_extension():
    """Single-element list: loop body runs once, branch not taken."""
    result = Strongest_Extension("S", ["A"])
    assert result == "S.A"


def test_non_alpha_characters_ignored():
    """Digits and punctuation do not affect the strength computation."""
    result = Strongest_Extension("X", ["a1!", "B2?"])
    assert result == "X.B2?"


def test_all_negative_values():
    """A later extension with a less negative value still wins."""
    result = Strongest_Extension("N", ["abc", "ab"])
    assert result == "N.ab"
