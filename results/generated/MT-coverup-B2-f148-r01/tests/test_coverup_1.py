# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


def test_bf_forward_order_returns_planets_between():
    """Covers lines 3-9: valid inputs with planet1_index < planet2_index."""
    result = bf("Mercury", "Neptune")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert isinstance(result, tuple)


def test_bf_reverse_order_returns_planets_between():
    """Covers lines 3-8 and 10-11 (else branch): planet1_index > planet2_index."""
    result = bf("Neptune", "Mercury")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert isinstance(result, tuple)


def test_bf_invalid_first_planet_returns_empty_tuple():
    """Covers lines 3-5: planet1 not in planet_names."""
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_second_planet_returns_empty_tuple():
    """Covers lines 3-5: planet2 not in planet_names."""
    assert bf("Earth", "Pluto") == ()


def test_bf_same_planet_returns_empty_tuple():
    """Covers lines 3-5: planet1 == planet2."""
    assert bf("Earth", "Earth") == ()


def test_bf_adjacent_planets_returns_empty_tuple():
    """Covers lines 3-9: adjacent planets yield an empty slice."""
    assert bf("Earth", "Mars") == ()
