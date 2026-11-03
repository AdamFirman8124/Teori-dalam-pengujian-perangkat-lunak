# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest

from f148 import bf


def test_bf_invalid_first_planet_returns_empty_tuple():
    """Covers line 4-5: planet1 not in planet_names."""
    assert bf("Xanadu", "Earth") == ()


def test_bf_invalid_second_planet_returns_empty_tuple():
    """Covers line 4-5: planet2 not in planet_names."""
    assert bf("Earth", "Xanadu") == ()


def test_bf_same_planet_returns_empty_tuple():
    """Covers line 4-5: planet1 == planet2."""
    assert bf("Earth", "Earth") == ()


def test_bf_forward_order():
    """Covers lines 6-9: planet1_index < planet2_index."""
    result = bf("Mercury", "Neptune")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_reverse_order():
    """Covers lines 6-8 and 11: planet1_index > planet2_index."""
    result = bf("Neptune", "Mercury")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_adjacent_forward_returns_empty_tuple():
    """Adjacent planets in forward order yield an empty slice."""
    assert bf("Earth", "Mars") == ()


def test_bf_adjacent_reverse_returns_empty_tuple():
    """Adjacent planets in reverse order yield an empty slice."""
    assert bf("Mars", "Earth") == ()


def test_bf_single_planet_between():
    """Exactly one planet lies between the two given planets."""
    assert bf("Mercury", "Earth") == ("Venus",)
    assert bf("Earth", "Mercury") == ("Venus",)


def test_bf_result_is_tuple():
    """The result must always be a tuple, never a list."""
    assert isinstance(bf("Venus", "Saturn"), tuple)
    assert isinstance(bf("Saturn", "Venus"), tuple)
    assert isinstance(bf("Pluto", "Venus"), tuple)
