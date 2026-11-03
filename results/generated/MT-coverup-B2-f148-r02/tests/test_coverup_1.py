# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

"""Tests for f148.bf — covering lines 3-11 and all branches.

bf is a pure function (no I/O, no globals mutated), so no monkeypatching
or fixture-based cleanup is required; each test leaves no state behind.
"""

import pytest

from f148 import bf


def test_bf_invalid_planet1_returns_empty_tuple():
    # Line 4 (first disjunct true) -> line 5.
    assert bf("Pluto", "Earth") == ()


def test_bf_invalid_planet2_returns_empty_tuple():
    # Line 4 (second disjunct true, first false) -> line 5.
    assert bf("Earth", "Pluto") == ()


def test_bf_same_planet_returns_empty_tuple():
    # Line 4 (third disjunct true, first two false) -> line 5.
    assert bf("Earth", "Earth") == ()


def test_bf_planet1_before_planet2():
    # Lines 6-8 true-branch -> line 9.
    assert bf("Earth", "Jupiter") == ("Mars",)


def test_bf_planet1_after_planet2():
    # Lines 6-8 false-branch -> lines 10-11.
    assert bf("Jupiter", "Earth") == ("Mars",)


def test_bf_adjacent_planets_forward_empty_result():
    # Line 8 true-branch with empty slice (Earth idx 2 < Mars idx 3).
    assert bf("Earth", "Mars") == ()


def test_bf_adjacent_planets_backward_empty_result():
    # Line 8 false-branch with empty slice (Mars idx 3, Earth idx 2).
    assert bf("Mars", "Earth") == ()


def test_bf_full_range_forward():
    # Line 9 with a multi-element slice.
    assert bf("Mercury", "Neptune") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
    )


def test_bf_full_range_backward():
    # Lines 10-11 with a multi-element slice.
    assert bf("Neptune", "Mercury") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
    )


def test_bf_returns_tuple_type():
    # Postcondition: result is always a tuple, even when empty.
    assert isinstance(bf("Venus", "Uranus"), tuple)
    assert isinstance(bf("Venus", "Venus"), tuple)
    assert isinstance(bf("X", "Uranus"), tuple)


def test_bf_symmetry_of_results():
    # Postcondition: swapping arguments yields the same inner planets.
    forward = bf("Venus", "Saturn")
    backward = bf("Saturn", "Venus")
    assert forward == ("Earth", "Mars", "Jupiter")
    assert backward == ("Earth", "Mars", "Jupiter")
    assert forward == backward
