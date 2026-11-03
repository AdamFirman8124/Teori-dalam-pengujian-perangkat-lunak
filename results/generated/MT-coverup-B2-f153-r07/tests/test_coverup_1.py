# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_later_extension_stronger():
    """A later extension with a higher strength replaces the first one.

    Covers lines 3-9, in particular the True branch of 'if val > my_val'
    (lines 7-9).
    """
    # "aa" -> strength -2, "AA" -> strength 2, so "AA" must win.
    result = Strongest_Extension("S", ["aa", "AA"])
    assert result == "S.AA"


def test_first_extension_strongest():
    """The first extension stays the strongest (False branch of line 7)."""
    # "AA" -> strength 2, "aa" -> strength -2, so "AA" must win.
    result = Strongest_Extension("S", ["AA", "aa"])
    assert result == "S.AA"


def test_tie_keeps_first():
    """Ties do not replace the first extension (strict '>' comparison)."""
    # "AA" -> 2, "Be" -> 0, "CC" -> 2; "CC" ties but must not replace "AA".
    result = Strongest_Extension("my_class", ["AA", "Be", "CC"])
    assert result == "my_class.AA"


def test_non_alpha_characters_ignored():
    """Non-alphabetic characters do not affect the strength computation."""
    # "1A_b" -> 1 upper, 1 lower -> 0; "2c" -> -1, so "1A_b" wins.
    result = Strongest_Extension("C", ["1A_b", "2c"])
    assert result == "C.1A_b"


def test_single_extension():
    """A single-element list: loop body runs once, no replacement occurs."""
    # "xY" -> 1 upper, 1 lower -> 0; 0 > 0 is False, so "xY" stays.
    result = Strongest_Extension("Klass", ["xY"])
    assert result == "Klass.xY"
