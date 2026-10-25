# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_strongest_extension_selects_highest_uppercase_score():
    assert Strongest_Extension("Codec", ["aA", "AbC", "ABC!1"]) == "Codec.ABC!1"


def test_strongest_extension_keeps_first_extension_on_tie():
    assert Strongest_Extension("Codec", ["AB", "CD", "abc"]) == "Codec.AB"
