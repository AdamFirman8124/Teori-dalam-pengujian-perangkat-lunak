# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

"""Tests for f148.bf covering all lines and branches (lines 3-11).

bf is a pure function (no I/O, no globals mutated), so no monkeypatching
or fixture-based cleanup is required; each test leaves no state behind.
"""

import pytest

from f148 import bf


def test_bf_invalid_planet1_returns_empty_tuple():
    """Line 4 (first disjunct) -> line 5: unknown planet1 yields ()."""
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_planet2_returns_empty_tuple():
    """Line 4 (second disjunct) -> line 5: unknown planet2 yields ()."""
    assert bf("Earth", "Pluto") == ()


def test_bf_case_sensitive_lookup_returns_empty_tuple():
    """Line 4: membership test is case sensitive, so lowercase fails."""
    assert bf("earth", "Mars") == ()


def test_bf_same_planet_returns_empty_tuple():
    """Line 4 (third disjunct) -> line 5: identical planets yield ()."""
    assert bf("Earth", "Earth") == ()


def test_bf_forward_order_returns_planets_between():
    """Lines 6-9: planet1 before planet2 returns the planets in between."""
    result = bf("Earth", "Jupiter")
    assert result == ("Mars",)


def test_bf_forward_order_multiple_planets():
    """Lines 6-9: full span between first and last planet."""
    result = bf("Mercury", "Neptune")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_reverse_order_returns_planets_between():
    """Lines 6-8, 10-11 (else branch): planet1 after planet2."""
    result = bf("Jupiter", "Earth")
    assert result == ("Mars",)


def test_bf_reverse_order_multiple_planets():
    """Lines 10-11: reversed full span yields the same set in order."""
    result = bf("Neptune", "Mercury")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


def test_bf_adjacent_planets_forward_returns_empty_tuple():
    """Lines 6-9: adjacent planets have nothing between them."""
    assert bf("Mercury", "Venus") == ()


def test_bf_adjacent_planets_reverse_returns_empty_tuple():
    """Lines 10-11: adjacent planets in reverse order."""
    assert bf("Venus", "Mercury") == ()


def test_bf_returns_tuple_type():
    """Lines 3-11: result is always a tuple, never a list."""
    assert isinstance(bf("Earth", "Saturn"), tuple)
    assert isinstance(bf("Saturn", "Earth"), tuple)
    assert isinstance(bf("Sun", "Moon"), tuple)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__]))
