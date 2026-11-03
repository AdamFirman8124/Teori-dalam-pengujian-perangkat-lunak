# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


def test_bf_invalid_first_planet_returns_empty_tuple():
    """Covers lines 3-5: planet1 not in planet_names."""
    assert bf("Pluto", "Earth") == ()
    assert bf("Sun", "Mars") == ()


def test_bf_invalid_second_planet_returns_empty_tuple():
    """Covers lines 3-5: planet2 not in planet_names."""
    assert bf("Earth", "Pluto") == ()
    assert bf("Mars", "Moon") == ()


def test_bf_same_planet_returns_empty_tuple():
    """Covers lines 3-5: planet1 == planet2."""
    assert bf("Earth", "Earth") == ()
    assert bf("Neptune", "Neptune") == ()


def test_bf_forward_order():
    """Covers lines 6-9: planet1_index < planet2_index."""
    assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Mercury", "Neptune") == (
        "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
    )
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")


def test_bf_backward_order():
    """Covers lines 6-7 and 11: planet1_index > planet2_index."""
    assert bf("Jupiter", "Earth") == ("Mars",)
    assert bf("Neptune", "Mercury") == (
        "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
    )
    assert bf("Saturn", "Venus") == ("Earth", "Mars", "Jupiter")


def test_bf_adjacent_planets_return_empty_tuple():
    """Both branches with adjacent planets yield an empty slice."""
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Earth") == ()
