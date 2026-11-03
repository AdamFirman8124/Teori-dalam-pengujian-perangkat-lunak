# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


def test_invalid_first_planet_returns_empty_tuple():
    """Line 5: planet1 not in planet_names -> return ()."""
    assert bf("Pluto", "Earth") == ()


def test_invalid_second_planet_returns_empty_tuple():
    """Line 5: planet2 not in planet_names -> return ()."""
    assert bf("Earth", "Pluto") == ()


def test_same_planet_returns_empty_tuple():
    """Line 5: planet1 == planet2 -> return ()."""
    assert bf("Earth", "Earth") == ()


def test_first_planet_before_second():
    """Lines 6-9: planet1_index < planet2_index -> planets strictly between."""
    assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Mercury", "Neptune") == (
        "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
    )


def test_first_planet_after_second():
    """Lines 10-11: else branch -> planets strictly between, reversed order."""
    assert bf("Jupiter", "Earth") == ("Mars",)
    assert bf("Neptune", "Mercury") == (
        "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
    )


def test_adjacent_planets_forward():
    """Line 9: adjacent planets, forward order -> empty tuple."""
    assert bf("Earth", "Mars") == ()


def test_adjacent_planets_backward():
    """Line 11: adjacent planets, backward order -> empty tuple."""
    assert bf("Mars", "Earth") == ()


def test_result_is_tuple_type():
    """Postcondition: result is always a tuple."""
    assert isinstance(bf("Venus", "Saturn"), tuple)
    assert isinstance(bf("Saturn", "Venus"), tuple)
    assert isinstance(bf("Venus", "Venus"), tuple)
    assert isinstance(bf("Venus", "Krypton"), tuple)
