# file: project/f148/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

"""Tests for f148.bf -- cover all previously unexecuted lines 3-11.

bf is a pure function (no globals, no I/O, no mutable state), so no
monkeypatching or teardown is required; each test is self-contained and
leaves no state behind.
"""

import pytest

from f148 import bf


def test_bf_invalid_first_planet():
    # Line 4 short-circuits on "planet1 not in planet_names"; line 5 runs.
    assert bf("Krypton", "Earth") == ()


def test_bf_invalid_second_planet():
    # Second operand of the "or" chain on line 4.
    assert bf("Earth", "Krypton") == ()


def test_bf_both_invalid():
    assert bf("Krypton", "Vulcan") == ()


def test_bf_same_planet():
    # Third operand of the "or" chain on line 4 (planet1 == planet2).
    assert bf("Earth", "Earth") == ()


def test_bf_case_sensitive_lookup_is_rejected():
    # Names must match exactly; lowercase input hits the early return.
    assert bf("earth", "Mars") == ()


def test_bf_planet1_before_planet2():
    # Lines 6-7 compute indices; line 8 True branch; line 9 forward slice.
    result = bf("Jupiter", "Neptune")
    assert result == ("Saturn", "Uranus")
    assert isinstance(result, tuple)


def test_bf_planet1_after_planet2():
    # Line 8 False branch; line 11 reverse slice.
    result = bf("Earth", "Mercury")
    assert result == ("Venus",)
    assert isinstance(result, tuple)


def test_bf_wide_forward_range():
    assert bf("Mercury", "Uranus") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
    )


def test_bf_wide_reverse_range():
    assert bf("Neptune", "Mercury") == (
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
    )


def test_bf_adjacent_planets_forward_yields_empty_tuple():
    # Equal slice bounds in the forward branch (line 9).
    assert bf("Earth", "Mars") == ()


def test_bf_adjacent_planets_reverse_yields_empty_tuple():
    # Equal slice bounds in the else branch (line 11).
    assert bf("Mars", "Earth") == ()


@pytest.mark.parametrize(
    "planet1,planet2,expected",
    [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Neptune", "Jupiter", ("Saturn", "Uranus")),
        ("Mercury", "Mars", ("Venus", "Earth")),
        ("Mars", "Mercury", ("Venus", "Earth")),
        ("Uranus", "Uranus", ()),
        ("Pluto", "Mars", ()),
        ("Mars", "Pluto", ()),
    ],
)
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected
