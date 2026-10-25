# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    # Lines 3-4 execute; loop never updates (line 7 false branch).
    result = Strongest_Extension("MyClass", ["SErviCE"])
    assert result == "MyClass.SErviCE"


def test_later_extension_replaces_strongest():
    # Lines 5-9 all execute, including the update branch (lines 8-9).
    # "AAa" -> 2 upper - 1 lower = 1
    # "Abbb" -> 1 upper - 3 lower = -2
    # "AB"  -> 2 upper - 0 lower = 2  (strictly greater, so it replaces)
    result = Strongest_Extension("my_class", ["AAa", "Abbb", "AB"])
    assert result == "my_class.AB"


def test_tie_keeps_first_extension():
    # Loop runs but no val exceeds my_val (line 7 false branch each time).
    result = Strongest_Extension("Cls", ["Aa", "Bb"])
    assert result == "Cls.Aa"


def test_single_character_extensions():
    result = Strongest_Extension("C", ["a", "Z"])
    assert result == "C.Z"


def test_non_alpha_characters_ignored():
    result = Strongest_Extension("C", ["1!_Aa"])
    assert result == "C.1!_Aa"
