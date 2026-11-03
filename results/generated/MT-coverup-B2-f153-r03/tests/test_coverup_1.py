# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    """No later extension strictly beats the first one, so the false branch
    of the comparison is taken on every iteration and lines 8-9 never run."""
    result = Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"])
    # Strengths: 'SErviNGSliCes' -> 6-7 = -1, 'Cheese' -> 1-5 = -4, 'StuFfed' -> 2-5 = -3
    assert result == "Slices.SErviNGSliCes"


def test_later_extension_is_strongest():
    """A later extension with strictly greater strength replaces the current
    strongest, executing the true branch (lines 8-9)."""
    result = Strongest_Extension("my_list", ["one", "TWO", "three"])
    # Strengths: 'one' -> -3, 'TWO' -> 3, 'three' -> -5; 'TWO' wins.
    assert result == "my_list.TWO"


def test_tie_keeps_first_extension():
    """Ties do not replace the current strongest because the comparison is
    strict ('>'), exercising the false branch again."""
    result = Strongest_Extension("Cls", ["aA", "Aa", "ZZzz"])
    # All strengths are 0, so the first extension must be kept.
    assert result == "Cls.aA"


def test_non_alpha_characters_ignored():
    """Non-alphabetic characters do not affect the strength computation."""
    result = Strongest_Extension("mod", ["1A_b!", "x"])
    # '1A_b!' -> 1 upper, 1 lower -> 0; 'x' -> -1; first still wins.
    assert result == "mod.1A_b!"


def test_empty_extensions_raises():
    """An empty extension list cannot select a strongest extension."""
    with pytest.raises(IndexError):
        Strongest_Extension("Cls", [])
