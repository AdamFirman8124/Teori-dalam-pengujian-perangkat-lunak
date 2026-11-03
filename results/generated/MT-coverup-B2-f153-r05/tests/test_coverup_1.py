# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    """No later extension beats the first: covers lines 3-7 and 11-12,
    with the 'val > my_val' branch never taken."""
    # "SErviNGSliCes": 6 upper - 7 lower = -1 (best)
    # "Cheese": 1 - 5 = -4 ; "StuFfed": 2 - 5 = -3
    assert (
        Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"])
        == "Slices.SErviNGSliCes"
    )


def test_later_extension_is_strongest():
    """A later extension strictly beats earlier ones: covers lines 8-9
    (the branch taken, with 'strong' and 'my_val' updated)."""
    # "a": -1 ; "BB": 2 > -1 -> update ; "CCC": 3 > 2 -> update again
    assert Strongest_Extension("x", ["a", "BB", "CCC"]) == "x.CCC"


def test_tie_keeps_first():
    """Equal strength does not replace the current strongest
    (branch 'val > my_val' false inside the loop)."""
    # "Ab": 1 - 1 = 0 ; "Cd": 1 - 1 = 0 (not > 0, no update)
    assert Strongest_Extension("C", ["Ab", "Cd"]) == "C.Ab"


def test_non_alpha_characters_ignored():
    """Digits and symbols are ignored by the strength computation."""
    # "a1B2": 1 - 1 = 0 ; "c3D4": 1 - 1 = 0 (tie, first kept)
    assert Strongest_Extension("X", ["a1B2", "c3D4"]) == "X.a1B2"


def test_single_extension():
    """Single-element list: loop body runs once, no update possible."""
    assert Strongest_Extension("Solo", ["only"]) == "Solo.only"


def test_empty_string_extension_first():
    """An empty first extension has strength 0; a positive one replaces it."""
    # "": 0 ; "A": 1 > 0 -> update
    assert Strongest_Extension("E", ["", "A"]) == "E.A"
